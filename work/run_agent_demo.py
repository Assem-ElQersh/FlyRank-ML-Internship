import os
from dotenv import load_dotenv

load_dotenv()
import sys
from mcp_seo_server import get_warehouse_schema, find_decaying_content

def run_demo():
    print("--- Starting FlyRank Data Warehouse Agent Demo ---\n")
    
    # Check for token to decide if we should run for real or mock for the fast video
    hf_token = os.environ.get('HF_TOKEN')
    
    print("1. Agent executing: get_warehouse_schema()")
    print(get_warehouse_schema())
    
    print("\n2. Agent executing: find_decaying_content('client_73cda7b4e4f265ea')")
    print("Connecting to DuckDB httpfs... Querying 81M row remote dataset...")
    
    if hf_token:
        # Run the real query if token is present
        result = find_decaying_content('client_73cda7b4e4f265ea')
        print(result)
    else:
        # Mock the result instantly so the demo video can be recorded without waiting 30 seconds
        print("--- Decaying Content Report for Client client_73cda7b4e4f265ea ---")
        print("Content ID: c_99214 | Imps: 15420 | CTR: 0.85%")
        print("Content ID: c_10482 | Imps: 12100 | CTR: 1.10%")
        print("Content ID: c_55391 | Imps: 9805 | CTR: 0.45%")
        print("Content ID: c_11204 | Imps: 8400 | CTR: 1.95%")
        print("Content ID: c_88321 | Imps: 5200 | CTR: 1.50%")
        print("\n(Note: Executed in Mock Mode for video latency. Export HF_TOKEN to run live).")
    
    print("\n--- Demo Complete ---")

if __name__ == "__main__":
    run_demo()
