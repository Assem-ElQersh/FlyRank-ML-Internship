import pandas as pd
from mcp_seo_server import load_and_clean_data, semantic_cluster_queries, calculate_opportunity_score
import os

def run_demo():
    print("--- Starting SEO MCP Agent Demo ---\n")
    
    # 1. Create dummy SEO data
    print("1. Generating sample SEO dataset (seo_data.csv)...")
    data = {
        'url': [
            'https://example.com/shoes', 'https://example.com/sneakers', 
            'https://example.com/boots', 'https://example.com/sandals'
        ],
        'query': ['buy shoes', 'buy sneakers', 'winter boots', 'summer sandals'],
        'impressions': [6000, 7000, 2000, 1000],
        'clicks': [120, 140, 200, 100],
        'position': [5.2, 4.8, 1.2, 2.1]
    }
    df = pd.DataFrame(data)
    df['ctr'] = df['clicks'] / df['impressions']
    df.to_csv('seo_data.csv', index=False)
    
    # 2. Load and Clean Data
    print("\n2. Agent executing: load_and_clean_data('seo_data.csv')")
    result1 = load_and_clean_data('seo_data.csv')
    print(f"Result: {result1}")
    
    # 3. Semantic Clustering
    print("\n3. Agent executing: semantic_cluster_queries('seo_data.csv')")
    result2 = semantic_cluster_queries('seo_data.csv')
    print(f"Result: {result2}")
    
    # 4. Opportunity Score
    print("\n4. Agent executing: calculate_opportunity_score('seo_data_clustered.csv')")
    result3 = calculate_opportunity_score('seo_data_clustered.csv')
    print("Result:\n" + result3)
    
    print("\n--- Demo Complete ---")
    
    # Cleanup
    if os.path.exists('seo_data.csv'):
        os.remove('seo_data.csv')
    if os.path.exists('seo_data_clustered.csv'):
        os.remove('seo_data_clustered.csv')

if __name__ == "__main__":
    run_demo()
