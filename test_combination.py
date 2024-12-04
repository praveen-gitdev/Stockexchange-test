from fetch_metadata import fetch_exchange_metadata
from recommend_sampling import recommend_samples

if __name__ == "__main__":
    # Step 1: Fetch metadata
    api_url = "https://api.stockexchangeinfo.com/exchanges"
    metadata = fetch_exchange_metadata(api_url)

    # Step 2: Recommend samples
    sampling_strategy = "proportional"  # Or "activity_based"
    recommendations = recommend_samples(metadata, sampling_strategy)

    # Output results
    for rec in recommendations:
        print(f"Exchange: {rec['exchange']}, Recommended Files to Sample: {rec['sample_count']}")
