import pandas as pd
import os

def read_and_transform_csv(file_path, column_mapping, fund_name):
    print(f"Processing file: {file_path}")
    
    # Read the CSV file with cp1252 encoding
    df = pd.read_csv(file_path, encoding='cp1252')
    
    print("Original columns:")
    print(df.columns.tolist())
    
    # Create a reverse mapping for easier lookup
    reverse_mapping = {v: k for k, v in column_mapping.items()}
    
    # Rename columns based on the mapping
    df = df.rename(columns=reverse_mapping)
    
    print("Columns after renaming:")
    print(df.columns.tolist())
    
    # Select only the columns we need
    columns_to_keep = ["Idea Title", "Assessor", "Impact Score", "Feasibility Score", 
                       "Value Score", "Impact Comment", "Feasibility Comment", "Value Comment"]
    
    # Check which columns are missing
    missing_columns = [col for col in columns_to_keep if col not in df.columns]
    if missing_columns:
        print(f"Warning: The following columns are missing: {missing_columns}")
        # Only keep the columns that are present in the DataFrame
        columns_to_keep = [col for col in columns_to_keep if col in df.columns]
    
    df = df[columns_to_keep]
    
    # Add the Fund column
    df["Fund"] = fund_name
    
    # Calculate the Agg Score if all required columns are present
    score_columns = ["Impact Score", "Feasibility Score", "Value Score"]
    if all(col in df.columns for col in score_columns):
        df["Agg Score"] = df[score_columns].mean(axis=1)
    else:
        print(f"Warning: Unable to calculate Agg Score for {fund_name}. Missing one or more score columns.")
        df["Agg Score"] = None
    
    return df

def create_condensed_df(df):
    # Create a copy of the DataFrame to avoid modifying the original
    condensed_df = df.copy()
    
    # Replace comment columns with word counts
    comment_columns = ["Impact Comment", "Feasibility Comment", "Value Comment"]
    for col in comment_columns:
        if col in condensed_df.columns:
            condensed_df[f"{col} Word Count"] = condensed_df[col].fillna("").apply(lambda x: len(str(x).split()))
            condensed_df = condensed_df.drop(columns=[col])
    
    # Calculate average comment length
    word_count_columns = [col for col in condensed_df.columns if "Word Count" in col]
    condensed_df["Avg Comment Length"] = condensed_df[word_count_columns].mean(axis=1)
    
    return condensed_df

# Define the column mappings for each fund
column_mappings = {
    "fund7.csv": {
        "Idea Title": "Idea Title",
        "Assessor": "Assessor",
        "Impact Score": "Impact / Alignment Rating",
        "Feasibility Score": "Feasibility Rating",
        "Value Score": "Auditability Rating",
        "Impact Comment": "Impact / Alignment Note",
        "Feasibility Comment": "Feasibility Note",
        "Value Comment": "Auditability Note"
    },
    "fund8.csv": {
        "Idea Title": "Idea Title",
        "Assessor": "Assessor",
        "Impact Score": "Impact / Alignment Rating",
        "Feasibility Score": "Feasibility Rating",
        "Value Score": "Auditability Rating",
        "Impact Comment": "Impact / Alignment Note",
        "Feasibility Comment": "Feasibility Note",
        "Value Comment": "Auditability Note"
    },
    "fund9.csv": {
        "Idea Title": "Idea Title",
        "Assessor": "Assessor",
        "Impact Score": "Impact / Alignment Rating",
        "Feasibility Score": "Feasibility Rating",
        "Value Score": "Auditability Rating",
        "Impact Comment": "Impact / Alignment Note",
        "Feasibility Comment": "Feasibility Note",
        "Value Comment": "Auditability Note"
    },
    "fund10.csv": {
        "Idea Title": "Proposal Title",
        "Assessor": "Reviewer",
        "Impact Score": "Impact Rating",
        "Feasibility Score": "Feasibility Rating",
        "Value Score": "Value for M Rating",
        "Impact Comment": "Impact Note",
        "Feasibility Comment": "Feasibility Note",
        "Value Comment": "Value for M Note"
    }
}

# List of CSV files
csv_files = ["fund7.csv", "fund8.csv", "fund9.csv", "fund10.csv"]

# Read and transform each CSV file, then concatenate them into a single DataFrame
dfs = []
for file in csv_files:
    fund_name = os.path.splitext(file)[0]  # Get the fund name without the .csv extension
    try:
        df = read_and_transform_csv(file, column_mappings[file], fund_name)
        dfs.append(df)
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")

# Concatenate all DataFrames
vca_final_df = pd.concat(dfs, ignore_index=True)

print("Final columns:")
print(vca_final_df.columns.tolist())

# Reorder columns to match the desired output
column_order = ["Idea Title", "Fund", "Assessor", "Impact Score", "Feasibility Score", 
                "Value Score", "Impact Comment", "Feasibility Comment", "Value Comment", "Agg Score"]
vca_final_df = vca_final_df.reindex(columns=column_order)

# Create the condensed DataFrame
vca_condensed_df = create_condensed_df(vca_final_df)

# Display the first few rows of both DataFrames
print("Full DataFrame:")
print(vca_final_df.head())
print("\nCondensed DataFrame:")
print(vca_condensed_df.head())

# Save both DataFrames to CSV files
vca_final_df.to_csv("vca_final_df.csv", index=False, encoding='cp1252')
vca_condensed_df.to_csv("vca_condensed_df.csv", index=False, encoding='cp1252')

print("Data processing complete. Results saved to 'vca_final_df.csv' and 'vca_condensed_df.csv'.")
