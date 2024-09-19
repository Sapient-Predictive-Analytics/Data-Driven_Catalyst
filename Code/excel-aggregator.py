import pandas as pd
import os
from typing import List, Dict

def read_excel_file(file_path: str, sheet_name: str = None) -> Dict[str, pd.DataFrame]:
    """
    Read an Excel file and return a dictionary of DataFrames, one for each sheet.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

def process_dataframe(df: pd.DataFrame, fund_name: str, columns_map: Dict[str, str]) -> pd.DataFrame:
    """
    Process a single DataFrame by adding a Fund column and renaming columns.
    """
    df['Fund'] = fund_name
    df.rename(columns=columns_map, inplace=True)
    return df[list(columns_map.values()) + ['Fund']]

def aggregate_excel_files(directory: str, columns_map: Dict[str, Dict[str, str]]) -> pd.DataFrame:
    """
    Aggregate Excel files from a directory into a single DataFrame.
    """
    all_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_path = os.path.join(directory, filename)
            fund_name = os.path.splitext(filename)[0]
            
            # Read all sheets in the Excel file
            sheets = read_excel_file(file_path)
            
            for sheet_name, df in sheets.items():
                # Process each sheet
                processed_df = process_dataframe(df, fund_name, columns_map[fund_name])
                all_data.append(processed_df)

    # Concatenate all processed DataFrames
    return pd.concat(all_data, ignore_index=True)

# Example usage
if __name__ == "__main__":
    # Directory containing Excel files
    excel_directory = "path/to/excel/files"

    # Mapping of original column names to standardized names for each fund
    columns_map = {
        "Fund1": {"Original Col1": "Standardized Col1", "Original Col2": "Standardized Col2"},
        "Fund2": {"Diff Col1": "Standardized Col1", "Diff Col2": "Standardized Col2"},
        # Add mappings for other funds as needed
    }

    # Aggregate the Excel files
    result_df = aggregate_excel_files(excel_directory, columns_map)

    # Display the result
    print(result_df.head())

    # Optionally, save the result to a new Excel file
    result_df.to_excel("aggregated_data.xlsx", index=False)
