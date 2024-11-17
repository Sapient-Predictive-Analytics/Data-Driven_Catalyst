# Sapient API Catalyst Fund Proposals Query Guide

This guide explains how to use any Linux/WSL command-line interface to query the Catalyst Fund Proposals Atlas MongoDB database. The tool provides flexible access to proposal data across all funds, with various filtering and search options.

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
