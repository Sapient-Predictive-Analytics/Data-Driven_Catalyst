## Voting Outcome to Select 7 Deep-Dive Data Reports

We [asked](https://t.me/ProjectCatalystChat/80325) the Project Catalyst community to pick 7 out of our 20 [examples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/examples.md) for data-driven analysis and reporting. These will include more sophisticated machine learning and plotting approaches get into more detail to present our findings to the community.

For the toolkit of open source data science tools please refer to the [OSDS](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/OSDS.md) section. 

These are the ideas that were chosen by vote:


**1.Proposal Keyword Occurrences vs Funding Success**

* Refinement: The dataset now includes all submitted valid proposals in funds from F-7 to F-12 except challenge settings and withdrawn proposals. Keywords with a minimum frequency (k: 20) where picked up and plotted for their success ratio, omitting non-technical words.
* Insight: "Cardano" serves as a benchmark, with 1632 proposals and 308 funded. The total funding ratio is around 19%, making it slightly less favorable to pick the keyword. This is likely due to the generic character, that discerning voters discount and not significant as a negative either. "Catalyst" fares a lot better, possibly because of challenge settings with limited scope to improve the funding mechanisms itself. Strikingly, putting the company name "MLabs" in the title resulted in success 28 out of 34 times - voters assume that this tag is genuinely only used by the company with that name and that their high standard of delivery beats giving new teams a shot. Given the high overall funding ratio, this is not surprising and future funds probably need to attract more proposals for the fund size or give reviewers and voters more tools to pick good proposals. Referencing new, up-and-coming tooling, like earlier "Marlowe" and later and more successfully, "Aiken", produced very good results regardless of the team or other keywords used. More surprising is the enduring success of keyword "Japan" which panders to the concentration of voting power in that country, and "SDK" used over 70 times with good success beating "Plutus" maybe hinting that there is a real need for the development of "low code" solutions. Readers can access the source code for the analysis in the repo and/or draw their own conclusion from our analysis. We hope that this example shows how datasets that are too large for human perusal can be simplified meaningfully using open source data analysis libraries to inspire and prompt fund design discussion.

![LogKeyword](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/log_keyword_funding_analysis_optimized.png)


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
