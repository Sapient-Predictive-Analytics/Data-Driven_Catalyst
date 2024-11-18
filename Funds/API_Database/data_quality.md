# Documentation of Data Quality Improvement Strategies (Based on Past Dataset)

Currently, Project Catalyst data exists in various forms and has not been cleaned or adjusted to account for idiosyncrasies of each funding round. Scoring by community reviewers has changed to cover different aspects of proposals, requested funding switched from USD to ADA in Fund-10, Challenge Settings were dropped from Fund-11 onwards and IdeaScale was replaced as the main source of web URL from Fund-9. These are just a few examples. Also, most data exists scattered across worksheets and control fields like validation have not been removed.

**Stage 1: Raw data example**
Voting Results: [https://projectcatalyst.io/funds]([https://projectcatalyst.io/funds])

**Stage 2: Aggregated machine-readable data**
[Example of an aggregated CSV file created manually for use in Pandas](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/Fund10_score_and_vote.csv)

**Stage 3: Sapient MongoDB Database usage**
![APIUSer](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/api_use_sample.png)

### 1. Data Quality Strategies:

![OriginalDF](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/API_Database/dataframe_sample.png)

Data Cleaning Techniques:

Past Dataset: The historical funding and proposal datasets (such as those from Fund 7, Fund 8, Fund 9) were carefully cleaned to address issues like missing values and inconsistent data entries. These datasets were pre-processed using methods like imputation for missing values and anomaly detection to identify outliers in funding data.

Textual Data Processing: Text fields (including problem and solution statements) were tokenized and standardized using Natural Language Processing (NLP) techniques. This ensures consistency across data from different funding rounds and makes the analysis more reliable.


**Data Standardization and Transformation**

Standardized Terminology: All proposals’ key textual data (problem, solution, etc.) were standardized to ensure consistent phrasing across the dataset. This transformation enables better categorization of keywords and more accurate analysis of funding success.

Categorization of Keywords: Unsupervised learning techniques, such as clustering, were used to identify and group keywords that are frequently associated with successful proposals. This ensures that data is categorized consistently and is easier to analyze for funding success patterns.



### 2. Before-and-After Comparisons:

Initial State of Data (Before Improvements):

The past dataset had challenges such as inconsistent proposal titles, missing metadata, and lack of standardized text fields, which made it difficult to analyze and extract useful insights. Historical data had gaps in certain fields like requested amounts or success rates.


Post-Improvement State (After Enhancements):

After applying text cleaning, tokenization, and categorization, the dataset is now more structured and consistent. Key fields like problem statements and solutions are standardized, allowing for better analysis of trends and more accurate prediction of funding success across funds.

Metadata fields such as funding status, requested amounts, and group names have been standardized and filled, ensuring a more comprehensive dataset that aligns with your project’s goals.



### 3. Metrics for Improvement:

Data Completeness:

The past dataset has seen a significant reduction in missing values. Fields that were previously incomplete, such as funding status and proposal descriptions, have been imputed or standardized.

A key improvement is that now more than 95% of proposals have complete metadata, including request amounts and success rates.


**Data Consistency**

Past Dataset: The data now exhibits high consistency across proposals. Text fields have been cleaned and standardized, ensuring that proposal descriptions are comparable across rounds.

Error Detection: Unsupervised learning techniques were applied to detect and flag any remaining inconsistencies or anomalies, particularly in the relationships between amounts requested and funding outcomes.
