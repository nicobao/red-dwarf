import pandas as pl # For sake of clean diffs
from collections import defaultdict
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

class PolisClient():
    def __init__(self, is_strict_moderation=None) -> None:
        self.n_components = 2
        # Ref: https://hyp.is/8zUyWM5fEe-uIO-J34vbkg/gwern.net/doc/sociology/2021-small.pdf
        self.min_votes = 7
        self.votes = []
        self.comments_df = []
        # Ref: https://hyp.is/MV0Iws5fEe-k9BdY6UR1VQ/gwern.net/doc/sociology/2021-small.pdf
        self.vote_matrix = None
        # Ref: https://gist.github.com/patcon/fd9079a5fbcd533160f8ae211e975307#file-math-pca2-json-L2
        # Ref: https://github.com/compdemocracy/polis/blob/6d04f4d144adf9640fe49b8fbaac38943dc11b9a/math/src/polismath/math/conversation.clj#L217-L225
        self.user_vote_counts = defaultdict(int)
        self.meta_tids = []
        self.mod_in = []
        self.mod_out = []
        self.last_vote_timestamp = 0
        self.group_clusters = []
        self.base_clusters = {}
        # TODO: Make accessor methods for these?
        self.statement_count = None
        self.participant_count = None
        self.is_strict_moderation = is_strict_moderation
        # Also know as PCA coords, PCA components, or embeddings.
        self.eigenvectors = []
        # Also know as PCA explained variance.
        self.eigenvalues = []

    def get_participant_row_mask(self):
        raise NotImplementedError

    def get_active_statement_ids(self):
        if self.is_strict_moderation == None:
            raise ValueError('must set is_strict_moderation to properly filter for active statements')
        ACTIVE_MOD_STATES = [1] if self.is_strict_moderation else [1,0]
        active_statement_ids = sorted(self.comments_df.loc[self.comments_df["mod"].isin(ACTIVE_MOD_STATES)].index, key=int)

        return active_statement_ids

    def get_unvoted_statement_ids(self):
        null_column_mask = self.matrix.isnull().all()
        null_column_ids = self.matrix.columns[null_column_mask].tolist()

        return null_column_ids

    def apply_masks(self, participant_rows=True, statement_cols=True):
        raise NotImplementedError

    def add_votes_batch(self, votes_df):
        """Add multiple votes from a DataFrame"""
        # TODO: Use tuples instead of named columns later, for perf.
        for _, row in votes_df.iterrows():
            self.add_vote(row)

    def add_vote(self, vote_row):
        """Add a single vote to the system"""
        # If this is a new vote (not an update)
        self.user_vote_counts[vote_row['pid']] += 1

        if self.last_vote_timestamp < int(vote_row['modified']):
            self.last_vote_timestamp = int(vote_row['modified'])

        self.votes.append({
            'participant_id': vote_row['pid'],
            'statement_id': vote_row['tid'],
            'vote': vote_row['vote'],
        })
        # Matrix is now stale
        self.matrix = None
        self.statement_count = None
        self.participant_count = None

    def get_user_vote_counts(self):
        return self.user_vote_counts

    def get_meta_tids(self):
        return self.meta_tids

    def get_mod_in(self):
        return self.mod_in

    def get_mod_out(self):
        return self.mod_out

    def get_last_vote_timestamp(self):
        return self.last_vote_timestamp

    def get_group_clusters(self):
        return self.group_clusters

    # TODO: Refactor this to "process_matrix"?
    def get_matrix(self, is_filtered=False):
        if self.matrix is None:
            # Only generate matrix when needed.
            self.matrix = pl.DataFrame.from_dict(self.votes)
            self.matrix = self.matrix.pivot(
                values="vote",
                index="participant_id",
                columns="statement_id",
            )

            participant_count = self.matrix.index.max() + 1
            comment_count = self.matrix.columns.max() + 1
            self.matrix = self.matrix.reindex(
                index=range(participant_count),
                columns=range(comment_count),
                fill_value=float('nan'),
            )
            self.statement_count = self.matrix.notna().any().sum()
            self.participant_count = len(self.matrix)

        if is_filtered:
            self.filter_matrix()

        return self.matrix

    def filter_matrix(self):
        # Filter out moderated statements.
        self.matrix = self.matrix.filter(self.get_active_statement_ids(), axis='columns')
        # Filter out participants with less than 7 votes.
        # Ref: https://hyp.is/JbNMus5gEe-cQpfc6eVIlg/gwern.net/doc/sociology/2021-small.pdf
        self.matrix = self.matrix.dropna(thresh=self.min_votes, axis='rows')
        # TODO: What about statements with no votes? E.g., 53 in oprah. Filter out? zero?
        unvoted_filter_type = 'drop' # `drop` or `zero`
        if unvoted_filter_type == 'zero':
            self.matrix[self.get_unvoted_statement_ids()] = 0
        elif unvoted_filter_type == 'drop':
            self.matrix = self.matrix.drop(self.get_unvoted_statement_ids(), axis='columns')
        else:
            raise ValueError('unvoted_filter_type must be `drop` or `zero`')

    # Ref: https://hyp.is/8zUyWM5fEe-uIO-J34vbkg/gwern.net/doc/sociology/2021-small.pdf
    def impute_missing_votes(self):
        mean_imputer = SimpleImputer(missing_values=float('nan'), strategy='mean')
        matrix_imputed = pl.DataFrame(
            mean_imputer.fit_transform(self.matrix),
            columns=self.matrix.columns,
            index=self.matrix.index,
        )
        self.matrix = matrix_imputed

    def run_pca(self):
        pca = PCA(n_components=self.n_components) ## pca is apparently different, it wants
        pca = pca.fit(self.matrix.T) ## .T transposes the matrix (flips it)
        self.eigenvectors = pca.components_.T ## isolate the coordinates and flip
        self.eigenvalues = pca.explained_variance_

    def scale_pca_polis(self):
        num_comments = self.matrix.shape[1]
        # TODO: Get a more rigorous user_vote_count with moderated-out statements.
        non_na_counts = [self.get_user_vote_counts()[pid] for pid in sorted(self.get_user_vote_counts().keys()) if pid in self.matrix.index]
        non_na_counts = pl.DataFrame(non_na_counts, index=self.matrix.index)
        # Ref: https://hyp.is/x6nhItMMEe-v1KtYFgpOiA/gwern.net/doc/sociology/2021-small.pdf
        # Ref: https://github.com/compdemocracy/polis/blob/15aa65c9ca9e37ecf57e2786d7d81a4bd4ad37ef/math/src/polismath/math/pca.clj#L155-L156
        scaling_coeffs = np.sqrt(num_comments / non_na_counts).values
        # TODO: Why is this needed? It doesn't seem to do anything...
        # See: https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
        # Reshape scaling_coeffs to match the shape of embedding (needed for broadcasting)
        scaling_coeffs = np.reshape(scaling_coeffs, shape=(-1, 1))

        # TODO: Why was this happening?
        # self.eigenvectors -= self.eigenvectors.mean()
        self.eigenvectors = self.eigenvectors * scaling_coeffs

    def generate_figure(self):
        plt.figure(figsize=(7, 5), dpi=80)
        plt.scatter(
            x=self.eigenvectors[:,0],
            y=self.eigenvectors[:,1],
            s=10,
            alpha=0.25,
        )
        plt.colorbar()
        plt.show()

    def load_data(self, filepath):
        if filepath.endswith("votes.json"):
            self.load_votes_data(filepath)
        elif filepath.endswith("comments.json"):
            self.load_comments_data(filepath)
        else:
            raise ValueError("Unknown file type")

    def load_votes_data(self, filepath):
        votes_df = pl.read_json(filepath, dtype={'modified': 'int64'})
        # Convert pandas timestamp (nanoseconds) into unix time (milliseconds).
        # See: https://stackoverflow.com/a/52450463
        votes_df['modified'] = [(t // 10**6) for t in votes_df['modified']]
        self.add_votes_batch(votes_df)

    def load_comments_data(self, filepath):
        self.comments_df = pl.read_json(filepath).set_index('tid')
        for i, row in self.comments_df.iterrows():
            # TODO: Why does is_meta make this mod-in.
            # Maybe I don't understand what mod-in does...
            # Note: mod-in/mod-out doesn't seem to be actually used in the front-end, so a bug here wouldn't matter.
            # Ref: https://github.com/compdemocracy/polis/blob/6d04f4d144adf9640fe49b8fbaac38943dc11b9a/math/src/polismath/math/conversation.clj#L825-L842
            if row['is_meta'] or row['mod'] == 1:
                self.mod_in.append(i)

            if row['is_meta'] or row['mod'] == -1:
                self.mod_out.append(i)

            # Ref: https://github.com/compdemocracy/polis/blob/6d04f4d144adf9640fe49b8fbaac38943dc11b9a/math/src/polismath/math/conversation.clj#L843-L850
            if row['is_meta']:
                self.meta_tids.append(i)
