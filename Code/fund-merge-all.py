# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:56:18 2024

@author: tom
"""

import pandas as pd
import os

def merge_fund_csvs():
    # Define the required columns in the specified order
    required_columns = [
        'Fund', 'Proposal', 'Challenge', 'Link', 'Overall score', 
        'Votes cast', 'YES', 'ABSTAIN', 'NO', 'Result', 
        'Meets approval threshold', 'REQUESTED', 'STATUS', 
        'FUND DEPLETION', 'Reason for not funded status', 'Ccy'
    ]
    
    # List to store all dataframes
    dfs = []
    
    # Process each CSV file
    for fund_num in range(7, 13):
        filename = f"Fund{fund_num:02d}_score_and_vote.csv"
        
        # Check if file exists
        if not os.path.exists(filename):
            print(f"Error: {filename} not found!")
            return None
            
        # Read the CSV
        try:
            df = pd.read_csv(filename)
            
            # Check for required columns
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                print(f"Error: {filename} is missing required columns: {missing_columns}")
                return None
            
            # Reorder the required columns and keep additional columns
            other_columns = [col for col in df.columns if col not in required_columns]
            new_column_order = required_columns + other_columns
            
            # Reorder columns
            df = df[new_column_order]
            
            # Add source fund information if not present
            if 'Fund' not in df.columns:
                df['Fund'] = f"Fund {fund_num}"
                
            dfs.append(df)
            print(f"Successfully processed {filename}")
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            return None
    
    # Merge all dataframes
    if dfs:
        merged_df = pd.concat(dfs, axis=0, ignore_index=True)
        
        # Save to CSV
        output_file = "All_funds_combined.csv"
        merged_df.to_csv(output_file, index=False)
        print(f"\nSuccessfully created {output_file}")
        print(f"Total rows: {len(merged_df)}")
        print("\nColumns in final dataset:")
        print("Required columns:", required_columns)
        print("Additional columns:", [col for col in merged_df.columns if col not in required_columns])
        
        return merged_df
    
    return None

# Execute the merge
if __name__ == "__main__":
    result = merge_fund_csvs()