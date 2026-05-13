from reddwarf.implementations import base


# This is to not break things.
# TODO: Adde deprecation warning.
def run_clustering(**kwargs) -> base.TypedPolisPipelineResult:
    return run_pipeline(**kwargs)


def run_pipeline(**kwargs) -> base.TypedPolisPipelineResult:
    kwargs = {
        "reducer": "pca",
        "clusterer": "kmeans",
        "consensus_mode": "legacy",
        **kwargs,
    }
    return base.run_pipeline(**kwargs)
