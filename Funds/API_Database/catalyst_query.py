import requests
import json
import argparse
from tabulate import tabulate

API_ENDPOINT = "https://ixo7sw67ja.execute-api.us-east-1.amazonaws.com/prod/funds"
API_KEY = "paste_actual_key_here"  # Your API key

# Add debug logging
print(f"Using API Key: {API_KEY[:5]}...{API_KEY[-5:]}")  # Show first/last 5 chars

def query_proposals(fund=None, challenge=None, status=None, min_score=None, limit=10):
    headers = {
        'x-api-key': API_KEY
    }
    
    # Build query parameters, converting all values to strings
    params = {}
    if fund:
        params['fund'] = str(fund)
    if challenge:
        params['challenge'] = str(challenge)
    if status:
        params['status'] = str(status)
    if min_score is not None:
        params['min_score'] = str(min_score)
    if limit is not None:
        params['limit'] = str(limit)
    
    print(f"Sending request to: {API_ENDPOINT}")
    print(f"With parameters: {json.dumps(params, indent=2)}")
    
    try:
        response = requests.get(API_ENDPOINT, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nFound {data['total_count']} matching records (showing {data['returned_count']})")
            
            if data['results']:
                table_data = []
                for record in data['results']:
                    table_data.append([
                        record.get('Fund', 'N/A'),
                        record.get('Title', 'N/A')[:50] + '...',
                        record.get('Challenge', 'N/A')[:30] + '...',
                        f"{record.get('Overall score', 'N/A'):.2f}" if record.get('Overall score') is not None else 'N/A',
                        record.get('STATUS', 'N/A'),
                        record.get('REQUESTED', 'N/A'),
                    ])
                
                headers = ['Fund', 'Title', 'Challenge', 'Score', 'Status', 'Requested']
                print("\n" + tabulate(table_data, headers=headers, tablefmt='grid'))
            else:
                print("No results found matching your criteria.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error accessing API: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query Catalyst Fund Proposals")
    parser.add_argument("--fund", help="Filter by fund (e.g., 'Fund12')")
    parser.add_argument("--challenge", help="Filter by challenge")
    parser.add_argument("--status", help="Filter by status (FUNDED or NOT FUNDED)")
    parser.add_argument("--min_score", type=float, help="Minimum overall score")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results")
    
    args = parser.parse_args()
    query_proposals(args.fund, args.challenge, args.status, args.min_score, args.limit)