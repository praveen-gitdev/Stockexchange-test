def recommend_samples(metadata, sampling_strategy="proportional"):
    recommendations = []
    for exchange in metadata:
        if sampling_strategy == "proportional":
            sample_count = int(exchange["companies"] * 0.01)
        elif sampling_strategy == "activity_based":
            sample_count = int(exchange["avg_trading_volume"] / 1_000_000)
        else:
            raise ValueError("Unknown sampling strategy")
        recommendations.append({"exchange": exchange["exchange"], "sample_count": sample_count})
    return recommendations
