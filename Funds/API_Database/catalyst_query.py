import requests
import json
import argparse
from tabulate import tabulate
from datetime import datetime

API_ENDPOINT = "https://ixo7sw67ja.execute-api.us-east-1.amazonaws.com/prod/funds"
API_KEY = "pasteAPIkeyFromUsHere"  # Your API key here

def format_money(value):
    try:
        return f"{float(value):,.0f} ADA"
    except:
        return str(value)

def query_proposals(args):
    headers = {'x-api-key': API_KEY}
    
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
    if args.funded_only:
        params['status'] = 'FUNDED'
    if args.high_impact:
        params['min_impact'] = '4.5'
    
    try:
        response = requests.get(API_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        print(f"\nFound {data['total_count']} matching proposals (showing {data['returned_count']})")
        
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
            
            # Print statistics if we have enough data
            if len(data['results']) > 0:
                scores = [r.get('Overall score') for r in data['results'] if r.get('Overall score')]
                amounts = [r.get('REQUESTED') for r in data['results'] if r.get('REQUESTED')]
                
                if scores:
                    print(f"\nStatistics:")
                    print(f"Average Score: {sum(scores)/len(scores):.2f}")
                    print(f"Total Requested: {sum(amounts):,.0f} ADA")
                    print(f"Average Request: {sum(amounts)/len(amounts):,.0f} ADA")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def print_examples():
    print("\nExample Queries:")
    print("1. High-impact funded proposals in Fund12:")
    print("   python catalyst_query.py --fund Fund12 --status FUNDED --min_score 4.5")
    print("\n2. All Vietnamese community proposals:")
    print("   python catalyst_query.py --challenge \"Vietnamese\"")
    print("\n3. Compare funding stats across funds:")
    print("   python catalyst_query.py --status FUNDED --limit 100")
    print("\n4. High-value proposals over 100k ADA:")
    print("   python catalyst_query.py --min_requested 100000")
    print("\n5. Show successful Developer Ecosystem proposals:")
    print("   python catalyst_query.py --challenge \"Developer Ecosystem\" --status FUNDED")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Query Catalyst Fund Proposals Database",
        epilog="Use --help for more information about each command."
    )
    parser.add_argument("--fund", help="Filter by fund (e.g., 'Fund12')")
    parser.add_argument("--challenge", help="Filter by challenge category")
    parser.add_argument("--status", help="Filter by status (FUNDED or NOT FUNDED)")
    parser.add_argument("--min_score", type=float, help="Minimum overall score")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results")
    parser.add_argument("--examples", action="store_true", help="Show example queries")
    parser.add_argument("--funded_only", action="store_true", help="Show only funded proposals")
    parser.add_argument("--high_impact", action="store_true", help="Show high-impact proposals (score > 4.5)")
    
    args = parser.parse_args()
    
    if args.examples:
        print_examples()
    else:
        query_proposals(args)
