# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:26:35 2024

@author: tom
"""

import pandas as pd
import glob
import os

# Specify the path to your Excel files
excel_folder = os.path.expanduser("~/.spyder-py3")

# List of common columns we want to preserve
common_columns = [
    "Proposal", "Overall score", "Votes cast", "YES", "NO", "Result", 
    "Meets approval threshold", "REQUESTED", "STATUS", "Reason for not funded status"
]

def standardize_column_name(col):
    """Standardize column names to handle inconsistencies"""
    return col.strip().lower().replace(' ', '_')

def import_excel_data(file_pattern='Fund* Voting results.xlsx'):
    all_funds_data = []
    all_columns = set()

    full_pattern = os.path.join(excel_folder, file_pattern)

    for file_path in glob.glob(full_pattern):
        fund_name = os.path.basename(file_path).split()[0]
        print(f"Processing file: {file_path}")
        
        xlsx = pd.ExcelFile(file_path)
        
        for sheet_name in xlsx.sheet_names:
            df = pd.read_excel(xlsx, sheet_name)
            
            # Standardize column names
            df.columns = [standardize_column_name(col) for col in df.columns]
            
            # Add fund and category columns
            df['fund'] = fund_name
            df['category'] = sheet_name
            
            # Collect all unique column names
            all_columns.update(df.columns)
            
            all_funds_data.append(df)

    # Create a list of all columns we want in the final DataFrame
    final_columns = ['fund', 'category'] + [standardize_column_name(col) for col in common_columns] + list(all_columns)
    final_columns = list(dict.fromkeys(final_columns))  # Remove duplicates while preserving order

    # Combine all DataFrames
    combined_df = pd.concat(all_funds_data, ignore_index=True)

    # Reorder columns and fill missing ones with NaN
    combined_df = combined_df.reindex(columns=final_columns)

    return combined_df

# Usage
combined_data = import_excel_data()
print(combined_data.head())
print(combined_data.columns)

# Save to CSV
combined_data.to_csv('OUTPUT.csv', index=False)