import requests
import json
import argparse
from tabulate import tabulate

API_ENDPOINT = "https://ixo7sw67ja.execute-api.us-east-1.amazonaws.com/prod/funds"
API_KEY = "pasteYourAPIkeyHere"  # Your API key

def format_money(value):
    try:
        return f"{int(float(value)):,} ADA"
    except:
        return str(value)

def display_statistics(data):
    stats = data.get('statistics', {})
    if not stats:
        return
    
    print("\nSummary Statistics:")
    print(f"Total Proposals: {stats['total_count']:,}")
    print(f"Average Score: {stats['avg_score']:.2f}")
    print(f"Average Requested: {stats['avg_requested']:,.0f} ADA")
    print(f"Funded Ratio: {stats['funded_ratio']}%")
    
    if 'fund_distribution' in stats:
        print("\nDistribution by Fund:")
        for fund, details in stats['fund_distribution'].items():
            print(f"{fund}: {details['count']} proposals (avg score: {details['avg_score']})")

def query_proposals(args):
    headers = {
        'x-api-key': API_KEY
    }
    
    # Build query parameters
    params = {}
    if args.fund:
        params['fund'] = args.fund
    if args.challenge:
        params['challenge'] = args.challenge
    if args.status:
        params['status'] = args.status
    if args.min_score:
        params['min_score'] = str(args.min_score)
    if args.limit:
        params['limit'] = str(args.limit)
    
    print("\nSending query with parameters:", json.dumps(params, indent=2))
    
    try:
        response = requests.get(API_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        metadata = data.get('metadata', {})
        print(f"\nFound {metadata['total_count']} matching proposals (showing {metadata['returned_count']})")
        
        if data['results']:
            # Prepare data for table
            table_data = []
            for record in data['results']:
                title = record.get('Title', record.get('Proposal', 'N/A'))
                table_data.append([
                    record.get('Fund', 'N/A'),
                    title[:50] + '...' if len(title) > 50 else title,
                    record.get('Challenge', 'N/A')[:30] + '...',
                    f"{record.get('Overall score', 'N/A'):.2f}",
                    format_money(record.get('REQUESTED')),
                    record.get('STATUS', 'N/A')
                ])
            
            # Print table
            headers = ['Fund', 'Title', 'Challenge', 'Score', 'Requested', 'Status']
            print("\n" + tabulate(table_data, headers=headers, tablefmt='grid'))
            
            # Display statistics
            display_statistics(data)
            
        else:
            print("No results found matching your criteria.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error accessing API: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def print_examples():
    print("\nExample Queries:")
    print("\n1. View funded proposals from Fund12:")
    print("   python3 catalyst_query.py --fund Fund12 --status FUNDED")
    
    print("\n2. Find high-scoring proposals:")
    print("   python3 catalyst_query.py --min_score 4.5")
    
    print("\n3. Search within a specific challenge:")
    print("   python3 catalyst_query.py --challenge \"Developer Ecosystem\"")
    
    print("\n4. Combine multiple filters:")
    print("   python3 catalyst_query.py --fund Fund12 --status FUNDED --min_score 4.0")
    
    print("\n5. View more results:")
    print("   python3 catalyst_query.py --fund Fund12 --limit 20")
    
    print("\nNote: Use --help to see all available options.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Query Catalyst Fund Proposals Database",
        epilog="Use --examples to see example queries."
    )
    
    parser.add_argument("--fund", help="Filter by fund (e.g., 'Fund12')")
    parser.add_argument("--challenge", help="Filter by challenge category")
    parser.add_argument("--status", help="Filter by status (FUNDED or NOT FUNDED)")
    parser.add_argument("--min_score", type=float, help="Minimum overall score")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results")
    parser.add_argument("--examples", action="store_true", help="Show example queries")
    
    args = parser.parse_args()
    
    if args.examples:
        print_examples()
    else:
        query_proposals(args)
