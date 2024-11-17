# Sapient API Catalyst Fund Proposals Query Guide

This guide explains how to use any Linux/WSL command-line interface to query the Catalyst Fund Proposals Atlas MongoDB database. The tool provides flexible access to proposal data across all funds, with various filtering and search options.

First, let's understand why we suggest to use a database instead of just Pandas CSV files in a S3 bucket (another simple way we used in the setup process):

1. Query Performance 
    
With 7000 rows, every time someone wants to see "all proposals from Fund 8 with YES votes > 100000000", the retrieval function would need to: 
        
            ▪ Download the entire CSV 
            
            ▪ Load it into memory 
            
            ▪ Filter the data 
            
A database can do this much faster using indexes 
        
2. Data Integrity 
    
        ◦ CSVs can get corrupted 
        
        ◦ No built-in validation 
        
        ◦ No enforcement of data types 
        
        ◦ Databases provide ACID properties (Atomicity, Consistency, Isolation, Durability) 
        
 3. Scalability 
    
        ◦ What if our data grows to 100,000 proposals? 
        
        ◦ What if we need multiple Lambdas accessing the data? 
        
        ◦ Databases handle concurrent access well 
        
4. Flexibility 
    
        ◦ Easy to update individual records 
        
        ◦ Can add new fields without modifying existing data 
        
        ◦ Can create relationships between different types of data 
        
We have opted for MongoDB's Atlas cloud solution, which is very popular and has open source and free tier support. Other advantages of MongoDB are:

    • Document-based (stores data in JSON-like documents) 
    
    • Great for semi-structured data like yours 
    
    • Natural fit for Python/JSON APIs 
    
    • Free open-source version 
    
    • Great performance for read operations 
    
    • Flexible schema (can handle those additional columns easily) 

Some key advantages of this database approach:

    1. Better Querying 
        ◦ Can filter by any field without loading all data 
        ◦ Can do complex aggregations (e.g., "average score by Challenge") 
        ◦ Can combine multiple conditions efficiently 
        
    2. Data Enrichment 
        ◦ Easy to add metadata (like when records were imported) 
        ◦ Can update records (e.g., add status updates) 
        ◦ Can link to other collections (e.g., user comments) 
        
    3. API Performance 
        ◦ Queries return only needed fields 
        ◦ Can limit results for pagination 
        ◦ Indexes make searches fast 
        
Potential drawbacks:
    1. More complex setup than S3 
    2. Needs database management/maintenance 
    3. Could be more expensive than simple file storage 
    4. Requires database connection management in Lambda 

***

## Basic Usage

```bash
python3 catalyst_query.py [options]
```

## Available Options

### Core Filters
- `--fund FUND`: Filter by fund name (e.g., "Fund12")
- `--challenge CHALLENGE`: Filter by challenge category
- `--status STATUS`: Filter by status ("FUNDED" or "NOT FUNDED")
- `--min_score SCORE`: Filter by minimum score (e.g., 4.5)
- `--limit NUMBER`: Limit number of displayed results (default: 10)

### Examples

1. Get funded proposals from Fund12:
```bash
python3 catalyst_query.py --fund Fund12 --status FUNDED
```

2. Find high-scoring proposals (≥4.5) in any fund:
```bash
python3 catalyst_query.py --min_score 4.5
```

3. Search for proposals in a specific challenge:
```bash
python3 catalyst_query.py --challenge "Developer Ecosystem"
```

4. Combine multiple filters:
```bash
python3 catalyst_query.py --fund Fund12 --status FUNDED --min_score 4.0
```

## Query Rules and Tips

1. **Case Sensitivity**:
   - Fund names are case-sensitive (use "Fund12" not "fund12")
   - Challenge names are case-insensitive
   - Status must be "FUNDED" or "NOT FUNDED" (uppercase)

2. **Partial Matches**:
   - Challenge names support partial matches
   - For example, "--challenge Developer" will match "Developer Ecosystem"

3. **Numbers**:
   - Score filters accept decimals (e.g., 4.5)
   - Limit must be a whole number

4. **Results**:
   - Default limit is 10 results
   - Statistics are calculated on the entire matching dataset
   - Results are sorted by default order in database

## Understanding Output

The query results show:
1. Total number of matching proposals
2. Number of displayed results
3. Table with key proposal information
4. Statistics for the entire result set:
   - Average score
   - Total requested funding
   - Average requested funding
   - Minimum and maximum scores

## Common Use Cases

1. **Finding High-Impact Proposals**:
```bash
python3 catalyst_query.py --min_score 4.5 --status FUNDED
```

2. **Analyzing Fund Performance**:
```bash
python3 catalyst_query.py --fund Fund12 --limit 100
```

3. **Challenge Analysis**:
```bash
python3 catalyst_query.py --challenge "Ecosystem" --status FUNDED
```

## Tips for Effective Querying

1. Start broad, then narrow down:
   - Begin with a single filter
   - Add additional filters to refine results

2. Use appropriate limits:
   - Small limits (5-10) for quick overview
   - Larger limits (50-100) for detailed analysis

3. Check statistics:
   - Statistics always reflect the entire matching dataset
   - Use them to understand broader patterns

4. Combine filters wisely:
   - More filters = more specific results
   - Too many filters might yield no results

## Error Messages

- "Invalid status": Check STATUS is "FUNDED" or "NOT FUNDED"
- "Invalid score": Ensure min_score is a valid number
- "No results found": Try broadening your search criteria

Need more examples or have questions? Use:
```bash
python3 catalyst_query.py --examples
```
