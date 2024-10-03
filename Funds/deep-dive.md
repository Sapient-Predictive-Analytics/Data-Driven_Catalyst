## Voting Outcome to Select 7 Deep-Dive Data Reports

We [asked](https://t.me/ProjectCatalystChat/80325) the Project Catalyst community to pick 7 out of our 20 [examples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/examples.md) for data-driven analysis and reporting. These will include more sophisticated machine learning and plotting approaches get into more detail to present our findings to the community.

For the toolkit of open source data science tools please refer to the [OSDS](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/OSDS.md) section. 

These are the ideas that were chosen by vote:


**1.Proposal Keyword Occurrences vs Funding Success**

* Approach: Use Natural Language Processing (NLP) with Pandas and Machine learning library to
analyze keyword frequency in proposals. Compare keyword occurrences with funding
success rates using statistical correlations or machine learning models.

Refinement: add Fund-11 data, more keywords and smart algorithm


**2.Boxplot of Proposal Assessor Scores vs Funding Success**

* Approach: Aggregate assessor scores for each proposal and categorize them by
Funding success. Use Matplotlib or Seaborn to create boxplots that visualize the
distribution of scores across successful and unsuccessful proposals.

Refinement: add Fund-11 data, better visualization, better data composability and cleaning

**3.Votes Required Evolution: Funding Request by Fund and Status**

* Approach: Track the evolution of votes required for funding requests across different
funds and statuses. Use Pandas for data aggregation and Matplotlib to create time
series or bar charts showing the trend over time.

Tools: Pandas, plotting and machine learning libraries

**4.YES votes Required for Funding (by categories) across Funds**

* Approach: Calculate the number of YES votes required for funding across different
categories and funds. Visualize the data using stacked bar charts or line plots to
compare categories.

Tools: Pandas, plotting and machine learning libraries


**5. Data-Processing of Milestone Module: Reading as JSON, tokenization, insights**
Submitted idea by community lead Intersect Japan (Yuta) and [GitHub issue](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/issues/6) logged by funded proposer saigonbitmaster

* Approach: Read and process milestone data from JSON files. Tokenize text data to
extract insights, such as milestone completion trends or common challenges. Use
Pandas for data manipulation and NLTK or SpaCy for tokenization.

Tools: Pandas, NLTK or SpaCy, JSON module.

**6. Rotational Breaks for Big Winners: The Impact of Past Success on Current Funding**

* Approach: Analyze the relationship between a team's past funding successes and their
chances of receiving current funding. Use Pandas to track historical funding data, and
apply statistical analysis or logistic regression to assess the impact of past wins on new
funding opportunities.

Tools: Pandas, Scikit-learn (for regression analysis), Matplotlib or Seaborn (for
visualizations)

**7. Scamming Catalyst: Cloned and Copied Ideas/Proposals Submitted Last Minute**
Please refer to [GitHub issue](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/issues/8) that was logged by a community member (Udai Solanki)

* Approach: Use Natural Language Processing (NLP) techniques to detect similarities
between proposals, especially those submitted close to deadlines. Compare these
proposals with earlier ones to identify potential cloning or plagiarism.

Tools: Pandas, NLTK or SpaCy (for NLP and similarity detection), FuzzyWuzzy (for
string matching), Matplotlib (for reporting findings).
