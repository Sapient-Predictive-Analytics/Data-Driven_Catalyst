# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:04:14 2024

@author: tom
"""

import pandas as pd
import glob
import os
import re

# Specify the path to your Excel files
excel_folder = os.path.expanduser("~/.spyder-py3")

# List of columns we want to preserve
columns_of_interest = [
    "proposal", "yes", "no", "overall_score", "votes_cast", "requested", "status"
]

def standardize_column_name(col):
    """Standardize column names to handle inconsistencies"""
    col = re.sub(r'[^\w\s]', '', col)  # Remove special characters
    return col.strip().lower().replace(' ', '_')

def clean_text(text):
    """Clean text fields to handle encoding issues"""
    if isinstance(text, str):
        return text.encode('ascii', 'ignore').decode('ascii')
    return text

def import_excel_data(file_pattern='Fund* Voting results.xlsx'):
    all_funds_data = []

    full_pattern = os.path.join(excel_folder, file_pattern)

    for file_path in glob.glob(full_pattern):
        fund_name = os.path.basename(file_path).split()[0]
        print(f"Processing file: {file_path}")
        
        xlsx = pd.ExcelFile(file_path)
        
        for sheet_name in xlsx.sheet_names:
            df = pd.read_excel(xlsx, sheet_name)
            
            # Standardize column names
            df.columns = [standardize_column_name(col) for col in df.columns]
            
            # Handle 'requested' column name change
            if 'requested_ada' in df.columns:
                df.rename(columns={'requested_ada': 'requested'}, inplace=True)
            
            # Add fund and category columns
            df['fund'] = fund_name
            df['category'] = sheet_name
            
            # Select only columns of interest
            columns_to_keep = ['fund', 'category'] + [col for col in columns_of_interest if col in df.columns]
            df = df[columns_to_keep]
            
            # Clean text fields
            for col in df.columns:
                df[col] = df[col].apply(clean_text)
            
            all_funds_data.append(df)

    # Combine all DataFrames
    combined_df = pd.concat(all_funds_data, ignore_index=True)

    return combined_df

# Usage
combined_data = import_excel_data()
print(combined_data.head())
print(combined_data.columns)

# Save to CSV
combined_data.to_csv('newOUTPUT.csv', index=False, encoding='utf-8')