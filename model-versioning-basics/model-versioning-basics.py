def promote_model(models: list) -> str:
    return max(
        models,
        key=lambda x: (x["accuracy"], -x["latency"], x["timestamp"])
    )["name"]