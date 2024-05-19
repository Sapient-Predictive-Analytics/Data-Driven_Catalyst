import pandas as pd

def read_and_concatenate_csvs(csv_files):
    """
    Reads multiple CSV files, adds a "Fund" column to each DataFrame, and concatenates them.

    Parameters:
    csv_files (list of tuples): A list of tuples where each tuple contains the path to a CSV file (str)
                                and the corresponding fund number (int).

    Returns:
    pd.DataFrame: A concatenated DataFrame containing data from all CSV files.
    """
    dataframes = []
    
    for file_path, fund_number in csv_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Add the "Fund" column
        df['Fund'] = fund_number
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    # Check if all DataFrames have the same columns
    if all(dataframes[0].columns.equals(df.columns) for df in dataframes):
        # Concatenate all DataFrames
        concatenated_df = pd.concat(dataframes, ignore_index=True)
        return concatenated_df
    else:
        raise ValueError("Not all CSV files have identical columns.")

# Example usage:
csv_files = [
    ('path/to/csv1.csv', 1),
    ('path/to/csv2.csv', 2),
    ('path/to/csv3.csv', 3)
]

concatenated_df = read_and_concatenate_csvs(csv_files)
print(concatenated_df)
