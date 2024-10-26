from pymongo import MongoClient
import pandas as pd
from datetime import datetime

def setup_mongodb():
    # Connect to MongoDB (assumes local installation)
    client = MongoClient('mongodb://localhost:27017/')
    
    # Create/access database
    db = client['fund_proposals']
    
    # Create collection
    proposals = db['proposals']
    
    # Create indexes for common queries
    proposals.create_index('Fund')
    proposals.create_index('Challenge')
    proposals.create_index([('Overall score', -1)])  # -1 for descending
    
    return proposals

def import_data(collection, csv_path):
    # Read CSV
    df = pd.read_csv(csv_path)
    
    # Convert DataFrame to list of dictionaries
    records = df.to_dict('records')
    
    # Add metadata
    for record in records:
        record['imported_at'] = datetime.utcnow()
        
        # Convert numeric fields to proper types
        for field in ['Overall score', 'Votes cast', 'YES', 'ABSTAIN', 'NO', 'REQUESTED']:
            if field in record and pd.notna(record[field]):
                record[field] = float(record[field])
    
    # Insert into MongoDB
    result = collection.insert_many(records)
    
    return len(result.inserted_ids)

def query_examples(collection):
    # Example queries
    print("\nExample queries:")
    
    # Count proposals by fund
    pipeline = [
        {"$group": {"_id": "$Fund", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    print("\nProposals per fund:")
    for result in collection.aggregate(pipeline):
        print(f"{result['_id']}: {result['count']} proposals")
    
    # Average score by challenge
    pipeline = [
        {"$group": {
            "_id": "$Challenge",
            "avg_score": {"$avg": "$Overall score"},
            "count": {"$sum": 1}
        }},
        {"$sort": {"avg_score": -1}},
        {"$limit": 5}
    ]
    print("\nTop 5 challenges by average score:")
    for result in collection.aggregate(pipeline):
        print(f"{result['_id']}: {result['avg_score']:.2f} (n={result['count']})")

if __name__ == "__main__":
    # Setup MongoDB
    collection = setup_mongodb()
    
    # Import data
    csv_path = 'All_funds_combined.csv'
    inserted = import_data(collection, csv_path)
    print(f"\nSuccessfully imported {inserted} records")
    
    # Run example queries
    query_examples(collection)
