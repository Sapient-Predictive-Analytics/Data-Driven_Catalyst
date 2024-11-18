# Sapient API Catalyst Fund Proposals Database & API Query Guide

The documentation provided gives first a high level motivation of our chosen implementation, a User's Guide how to work with the data through the API, and some [high level](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/API_documentation.md#project-catalyst-database-technical-architecture) additional information about database schema, indexing strategies, and optimization techniques.

You'll learn how to use any Linux/WSL command-line interface to query the Catalyst Fund Proposals Atlas MongoDB database. The tool provides flexible access to proposal and voting outcome data across funds (F7 until most recent F12), with various filtering and search options. Fund-13 will be uploaded after the voting results are out.

First, let's understand why we opted to use a (*noSQL, document-oriented*) database instead of "just" Pandas CSV files in a S3 bucket (another simple way we used in the setup process and for the [20 data report examples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/examples.md)):

**Query Performance**
    
With about 7000 proposals across 6 funds, two different currencies and several non-recurring categories or unique methodologies between the fund iterations, every time someone wants to see "all proposals from Fund 8 with YES votes > 100000000", the retrieval function would need to: 
        
* Download the entire CSV 
            
* Load it into memory 
            
* Format, clean and filter the data 
            
*A database can do this much faster using indices*
        
**Data Integrity**
    
* CSVs can get corrupted 
        
* No built-in validation 
        
* No enforcement of data types 
        
* Databases provide *ACID* properties (Atomicity, Consistency, Isolation, Durability) 
        
**Scalability** 
    
* What if more funds get added and have much larger amount of proposals
        
* What if we need multiple stakeholders accessing the data
        
* Databases handle concurrent access well

* Future LLM integration may require storing much larger datasets like milestone data, review commentary or social engagement / chat histories.
        
**Flexibility** 
    
* Easy to update individual records 
        
* Can add new fields without modifying existing data 
        
* Can create relationships between different types of data 
        
The new database also added Fund-11 and Fund-12 voting results and contributed the cleaned data used for community-tasked [Deep Dives](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/deep-dive.md)

We have opted for MongoDB's Atlas cloud solution, which is very popular and has open source and free tier support. Other advantages of MongoDB are:

    • Document-based (stores data in JSON-like documents) 
    
    • Great for semi-structured data like Excel-format legacy funds, i.e. all data 
    
    • Natural fit for Python/JSON APIs 
    
    • Great performance for read operations 
    
    • Flexible schema (can handle the additional columns or switch of currency more easily) 

![MongoPic](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/mdb_setting_up.gif)

Some key advantages of this database approach:

1) Better Querying 
* Can filter by any field without loading all data 
* Can do complex aggregations (e.g., "average score by Challenge") 
* Can combine multiple conditions efficiently 
        
2) Data Enrichment 
* Easy to add metadata (like when records were imported) 
* Can update records (e.g., add status updates) 
* Can link to other collections (e.g., user comments) 
        
3) API Performance 
* Queries return only needed fields 
* Can limit results for pagination 
* Indexes make searches fast 


***

## Basic Usage

*Download the file provided in this Github folder* **[catalyst_query.py](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/catalyst_query.py)**

*Use a text editor to enter the API Key provided under API_KEY*


```bash
python3 catalyst_query.py [options]
```

## 📺 How-to-use video guide for API

[<img src="https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/thumbAPI.png" width="200" height="140" />](https://youtu.be/e3bVTXNqRZE)


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

## Project Catalyst Database: Technical Architecture

**Overview motivation, database schema, indexing strategies, and optimization techniques**

The Data-Driven Catalyst Database represents a community-funded effort to democratize data usage and hopefully contribute to the future evolution of the tech-stack and funding rules. Built on MongoDB Atlas with AWS Lambda integration, this system provides a flexible, scalable foundation for analyzing proposal data across funding rounds while enabling future integration with on-chain governance mechanisms such as Catalyst Voices.

## Database Schema

![Atlas](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/Atlas%20Indices.png)
*View of the Atlas MongoDB Dashboard showing indices and data uploaded from Project Catalyst IO and other sources.*

### Core Collections

The primary collection `proposals` implements a flexible document schema that accommodates evolving metadata requirements:

```json
{
  "Fund": "String",           // Fund identifier
  "Proposal": "String",       // Proposal title
  "Challenge": "String",      // Challenge category
  "Overall score": "Number",  // Assessment score
  "STATUS": "String",        // Funding status
  "REQUESTED": "Number",     // Requested amount
  "Challenge": "String",     // Challenge category
  "imported_at": "Date"      // Metadata timestamp
}
```

### Indexing Strategy

The database employs strategic indexes to optimize common query patterns:

```javascript
// Primary indexes for frequent access patterns
db.proposals.createIndex({ "Fund": 1 })
db.proposals.createIndex({ "Challenge": 1 })
db.proposals.createIndex({ "STATUS": 1 })

// Compound index for scoring analysis
db.proposals.createIndex({ "Overall score": -1, "Fund": 1 })
```

These indexes support:
- Rapid fund-specific queries
- Challenge category analysis
- Status-based filtering
- Score-based ranking and analysis

## Data Access Patterns

The API supports various query patterns essential for governance analysis:

### Fund Analysis
```bash
# Analyze fund performance
GET /funds?fund=Fund12&status=FUNDED
```

### Challenge Tracking
```bash
# Track challenge evolution
GET /funds?challenge=Developer%20Ecosystem
```

### Cross-Fund Analysis
```bash
# Compare funding patterns
GET /funds?min_score=4.5&status=FUNDED
```

## Optimization Techniques

### Aggregation Pipeline
The system uses MongoDB's aggregation pipeline for efficient statistical analysis:

```javascript
[
  {'$match': query},
  {'$group': {
    '_id': None,
    'total_count': {'$sum': 1},
    'avg_score': {'$avg': '$Overall score'},
    'funded_ratio': {
      '$avg': {'$cond': [{'$eq': ['$STATUS', 'FUNDED']}, 1, 0]}
    }
  }}
]
```

### Query Optimization
- Case-insensitive text search for challenge categories
- Efficient numerical range queries for scoring analysis
- Pagination support for large result sets

## Future Extensibility

### On-Chain Integration
The schema design anticipates future integration with on-chain data:
- Transaction hash fields for funded proposals
- Smart contract references
- Blockchain event timestamps

### Scaling Considerations
The system architecture supports:
- Cross-collection relationships for detailed voting data
- Shard key strategy for horizontal scaling
- Time-series optimization for historical analysis

### API Evolution
The REST API is designed for extensibility:
- Versioned endpoints
- Query parameter expansion
- Response format flexibility

## Performance Characteristics

### Query Performance
Typical response times for common operations:
- Single fund queries: < 100ms
- Cross-fund analysis: < 500ms
- Statistical aggregations: < 1s

### Data Volume Handling
Current implementation efficiently handles:
- ~10,000 proposals across funds
- Multiple daily statistical aggregations
- Concurrent API access patterns

## Integration Points

### AWS Lambda Integration
The serverless architecture provides:
- Automatic scaling
- Cost-effective operation
- Regional deployment options

### MongoDB Atlas Features
Leverages cloud database capabilities:
- Automated backups
- Performance monitoring
- Security compliance

## Usage Examples

### Basic Query
```python
response = requests.get(
    "API_ENDPOINT/funds",
    params={"fund": "Fund12", "status": "FUNDED"},
    headers={"x-api-key": "API_KEY"}
)
```

### Statistical Analysis
```python
# Get fund statistics
response = requests.get(
    "API_ENDPOINT/funds",
    params={
        "fund": "Fund12",
        "min_score": "4.0"
    },
    headers={"x-api-key": "API_KEY"}
)
```

## Future Development Areas

Some selected areas for future coverage across **Data Enrichment**, **Analytics Expansion** and (on-chain) **Governance Integration** to upgrade the Data-Driven Catalyst toolkit for the coming era of Voltaire and Catalyst Voices to soon replace IdeaScale and Excel Spreadsheets etc.

- Integration with assessment data
- Voter participation metrics
- Impact tracking metrics
- Time-series analysis capabilities
- Cross-challenge correlation studies
- Funding pattern prediction models
- Proposal state tracking
- Voting power calculations


## Conclusion

This technical architecture provides a foundation for evolving community-driven governance data management in Project Catalyst. The combination of flexible schema design, efficient indexing strategies, and scalable cloud infrastructure supports both current operational needs and future governance mechanisms.

For detailed API usage instructions, refer to the video walkthrough and API Documentation [above](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/API_documentation.md#basic-usage).
