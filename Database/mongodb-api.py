import json
from pymongo import MongoClient
import os

def connect_to_mongodb():
    # In production, get this from AWS Secrets Manager
    MONGODB_URI = os.environ.get('MONGODB_URI')
    client = MongoClient(MONGODB_URI)
    return client.fund_proposals.proposals

def lambda_handler(event, context):
    try:
        # Parse query parameters
        params = event.get('queryStringParameters', {}) or {}
        
        fund = params.get('fund')
        challenge = params.get('challenge')
        min_score = float(params.get('min_score', 0))
        
        # Build query
        query = {}
        if fund:
            query['Fund'] = fund
        if challenge:
            query['Challenge'] = challenge
        if min_score:
            query['Overall score'] = {'$gte': min_score}
        
        # Connect to MongoDB
        collection = connect_to_mongodb()
        
        # Execute query
        results = list(collection.find(
            query,
            {'_id': 0}  # Exclude MongoDB ID
        ).limit(100))  # Limit results for API performance
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'count': len(results),
                'results': results
            }, default=str)  # Handle datetime serialization
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
