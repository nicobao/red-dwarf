from reddwarf.implementations import base


# This is to not break things.
# TODO: Adde deprecation warning.
def run_clustering(**kwargs) -> base.PolisClusteringResult:
    return run_pipeline(**kwargs)


def run_clustering_typed(**kwargs) -> base.TypedPolisClusteringResult:
    return run_pipeline_typed(**kwargs)


def run_pipeline(**kwargs) -> base.PolisClusteringResult:
    kwargs = {
        "reducer": "pca",
        "clusterer": "kmeans",
        "consensus_mode": "legacy",
        **kwargs,
    }
    return base.run_pipeline(**kwargs)


def run_pipeline_typed(**kwargs) -> base.TypedPolisClusteringResult:
    kwargs = {
        "reducer": "pca",
        "clusterer": "kmeans",
        "consensus_mode": "legacy",
        **kwargs,
    }
    return base.run_pipeline_typed(**kwargs)
