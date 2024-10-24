import pandas as pd
from difflib import SequenceMatcher

def clean_title(s):
    """
    Clean proposal title by removing emoticons, quotes, and standardizing spaces
    """
    s = str(s)
    return ' '.join(s.replace('"', '').replace("'", "").strip().split())

def find_matching_title(title, titles_list, similarity_threshold=0.95):
    """
    Find matching title from a list, returns exact match or high similarity match
    """
    clean_target = clean_title(title)
    
    # Try exact match first
    for t in titles_list:
        if clean_title(t) == clean_target:
            return t
    
    # Try similarity match
    for t in titles_list:
        if SequenceMatcher(None, clean_title(t), clean_target).ratio() >= similarity_threshold:
            return t
    
    return None

def merge_proposal_data(voting_file, proposals_file, output_file):
    """
    Merge voting data with proposal data, handling column conflicts
    """
    # Load the datasets
    voting_df = pd.read_csv(voting_file)
    proposals_df = pd.read_csv(proposals_file)
    
    print(f"Loaded {len(voting_df)} voting records and {len(proposals_df)} proposals")
    
    # Create a mapping of clean titles to original voting data rows
    voting_titles = voting_df['Proposal'].tolist()
    
    # Prepare for merged data
    merged_rows = []
    matched_count = 0
    
    # Get column lists
    voting_columns = list(voting_df.columns)
    proposals_columns = list(proposals_df.columns)
    
    # Create renamed columns mapping for conflicts
    column_mapping = {}
    for col in proposals_columns:
        if col in voting_columns and col != 'Proposal':  # Don't rename Proposal column
            new_col = f"{col}+1"
            while new_col in voting_columns or new_col in column_mapping.values():
                new_col = f"{new_col}+1"
            column_mapping[col] = new_col
    
    # Rename conflicting columns in proposals_df
    proposals_df = proposals_df.rename(columns=column_mapping)
    
    # Process each proposal
    for _, proposal_row in proposals_df.iterrows():
        matching_title = find_matching_title(proposal_row['Proposal'], voting_titles)
        
        if matching_title:
            matched_count += 1
            # Get the voting data row
            voting_row = voting_df[voting_df['Proposal'] == matching_title].iloc[0]
            
            # Combine the data
            merged_row = {}
            # First add voting data
            for col in voting_df.columns:
                merged_row[col] = voting_row[col]
            # Then add proposal data (with renamed columns where necessary)
            for col in proposals_df.columns:
                if col != 'Proposal':  # Skip the proposal title from proposals_df
                    merged_row[col] = proposal_row[col]
            
            merged_rows.append(merged_row)
    
    # Create final DataFrame
    final_df = pd.DataFrame(merged_rows)
    
    # Save to CSV
    final_df.to_csv(output_file, index=False, encoding='utf-8')
    
    # Calculate added columns (excluding renamed ones)
    common_columns = set(voting_columns) & set(proposals_df.columns)
    added_columns = len(proposals_df.columns) - len(common_columns)
    
    # Print summary
    print(f"\nMerge Summary:")
    print(f"Total proposals processed: {len(proposals_df)}")
    print(f"Matched and merged: {matched_count}")
    print(f"Original voting columns: {len(voting_columns)}")
    print(f"Added proposal columns: {added_columns}")
    print(f"Renamed columns due to conflicts: {len(column_mapping)}")
    print(f"\nColumn mapping for renamed columns:")
    for old_col, new_col in column_mapping.items():
        print(f"'{old_col}' → '{new_col}'")
    
    # Print final column list
    print(f"\nFinal columns in merged file:")
    for col in final_df.columns:
        print(f"- {col}")
    
    print(f"\nOutput saved to: {output_file}")
    
    return final_df

if __name__ == "__main__":
    voting_file = "Fund11_voting_data.csv"
    proposals_file = "Fund11 Proposals.csv"
    output_file = "Fund11_score_and_vote.csv"
    
    final_df = merge_proposal_data(voting_file, proposals_file, output_file)
