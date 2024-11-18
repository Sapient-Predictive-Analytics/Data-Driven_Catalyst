# 7 Community-voted Deep-Dive Data Reports

We [asked](https://t.me/ProjectCatalystChat/80325) the Project Catalyst community to pick 7 out of our 20 [examples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/examples.md) for data-driven analysis and reporting. These will include more sophisticated machine learning and plotting approaches get into more detail to present our findings to the community.

For the toolkit of open source data science tools please refer to the [OSDS](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/OSDS.md) section. 

These are the ideas that were chosen by vote:


## **1.Proposal Keyword Occurrences vs Funding Success**

* Refinement: The dataset now includes all submitted valid proposals in funds from F-7 to F-12 except challenge settings and withdrawn proposals. Keywords with a minimum frequency (k: 20) where picked up and plotted for their success ratio, omitting non-technical words.
* Insight: "Cardano" serves as a benchmark, with 1632 proposals and 308 funded. The total funding ratio is around 19%, making it slightly less favorable to pick the keyword. This is likely due to the generic character, that discerning voters discount and not significant as a negative either. "Catalyst" fares a lot better, possibly because of challenge settings with limited scope to improve the funding mechanisms itself. Strikingly, putting the company name "MLabs" in the title resulted in success 28 out of 34 times - voters assume that this tag is genuinely only used by the company with that name and that their high standard of delivery beats giving new teams a shot. Given the high overall funding ratio, this is not surprising and future funds probably need to attract more proposals for the fund size or give reviewers and voters more tools to pick good proposals. Referencing new, up-and-coming tooling, like earlier "Marlowe" and later and more successfully, "Aiken", produced very good results regardless of the team or other keywords used. More surprising is the enduring success of keyword "Japan" which panders to the concentration of voting power in that country, and "SDK" used over 70 times with good success beating "Plutus" maybe hinting that there is a real need for the development of "low code" solutions. Readers can access the source code for the analysis in the repo and/or draw their own conclusion from our analysis. We hope that this example shows how datasets that are too large for human perusal can be simplified meaningfully using open source data analysis libraries to inspire and prompt fund design discussion.

![LogKeyword](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/keyword_funding_analysis.png)

Detailed results - in order of their funding ratio:

Keyword 'MLAB': 37 total occurrences, 37 proposals, 31 funded

Keyword 'Aiken': 36 total occurrences, 35 proposals, 24 funded

Keyword 'Japan': 68 total occurrences, 66 proposals, 42 funded

Keyword 'Hydra': 20 total occurrences, 20 proposals, 11 funded

Keyword 'Marlowe': 26 total occurrences, 23 proposals, 12 funded

Keyword 'Asia': 50 total occurrences, 49 proposals, 24 funded

Keyword 'SDK': 85 total occurrences, 83 proposals, 36 funded

Keyword 'Plutus': 71 total occurrences, 69 proposals, 29 funded

Keyword 'hack': 50 total occurrences, 50 proposals, 18 funded

Keyword 'Vietnam': 93 total occurrences, 92 proposals, 33 funded

Keyword 'CIP': 64 total occurrences, 62 proposals, 22 funded

Keyword 'agri': 22 total occurrences, 20 proposals, 7 funded

Keyword 'CIP': 64 total occurrences, 62 proposals, 22 funded

Keyword 'node': 49 total occurrences, 43 proposals, 15 funded

Keyword 'smart': 203 total occurrences, 201 proposals, 70 funded

Keyword 'contract': 203 total occurrences, 198 proposals, 68 funded

Keyword 'LatAm': 58 total occurrences, 58 proposals, 19 funded

Keyword 'template': 25 total occurrences, 25 proposals, 8 funded

Keyword 'Atala': 65 total occurrences, 63 proposals, 20 funded

Keyword 'NMKR': 33 total occurrences, 32 proposals, 10 funded

Keyword 'code': 63 total occurrences, 61 proposals, 19 funded

Keyword 'security': 33 total occurrences, 30 proposals, 9 funded

Keyword 'open': 289 total occurrences, 286 proposals, 86 funded

Keyword 'DeFi': 122 total occurrences, 121 proposals, 36 funded

Keyword 'identity': 61 total occurrences, 61 proposals, 18 funded

Keyword 'wallet': 193 total occurrences, 185 proposals, 54 funded

Keyword 'Catalyst': 248 total occurrences, 233 proposals, 65 funded

Keyword 'oracle': 35 total occurrences, 35 proposals, 9 funded

Keyword 'DAO': 330 total occurrences, 291 proposals, 72 funded

Keyword 'community': 347 total occurrences, 339 proposals, 76 funded

Keyword 'Cardano': 2295 total occurrences, 2158 proposals, 483 funded

Keyword 'DLT360': 47 total occurrences, 47 proposals, 10 funded

Keyword 'Africa': 171 total occurrences, 166 proposals, 34 funded

Keyword 'game': 210 total occurrences, 197 proposals, 40 funded

Keyword 'crypto': 129 total occurrences, 126 proposals, 25 funded

Keyword 'chain': 677 total occurrences, 636 proposals, 124 funded

Keyword 'SPO': 167 total occurrences, 155 proposals, 29 funded

Keyword 'impact': 123 total occurrences, 113 proposals, 20 funded

Keyword 'grow': 86 total occurrences, 77 proposals, 13 funded

Keyword 'NFT': 570 total occurrences, 514 proposals, 74 funded

Keyword 'women': 22 total occurrences, 21 proposals, 0 funded



## **2.Boxplot of Proposal Assessor Scores vs Funding Success**

* Approach: Aggregate assessor scores for each proposal and categorize them by
Funding success. Use Matplotlib or Seaborn to create boxplots that visualize the
distribution of scores across successful and unsuccessful proposals.

Refinement: add Funds-11&12 data, better visualization, better data composability and cleaning. Remove whole spectrum of scores in favor of clear quintiles and median line. 

![Quintiles Boxplot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/quintile_boxplot_f7-f12.png)

Unlike the original inspiration by Victor Corcino and the previous Example boxplot, not all proposals are shown to sacrifice some detail for a better top level overview. Data is shown in score quintiles with the median score marked inside the box as well. As more Community Reviewers were attracted to the ecosystem and clearer rules emerged how to score over time, the dispersion of scores was reduced from fund to fund. On the other hand, the introduction of new rules from Fund-10 onwards made the score much less decisive in the voting outcome. The analysis of this charts allows other interpretatios and data-insights, but more importantly covers six funds with close to 7000 total proposals and disregards outliers by using quintiles.

## **3.Votes Required Evolution: Funding Request by Fund and Status**

* Approach: Track the evolution of votes required for funding requests across different
funds and statuses. Use Pandas for data aggregation and Matplotlib to create time
series or bar charts showing the trend over time.

Tools: Pandas, plotting and machine learning libraries

![VotesRequests](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/funding_requests_f7_f12.png)


## **4.YES votes Required for Funding (by categories) across Funds**

* Approach: Calculate the number of YES votes required for funding across different
categories and funds. Visualize the data using stacked bar charts or line plots to
compare categories.

Tools: Pandas, plotting and machine learning libraries

![YesBubbles](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/yes_votes_bubble_plot_f7_f12_with_means_log.png)


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

## **Research Topic 5: Data-Processing of Milestone Module: Reading as JSON, tokenization, insights**

Due to the non-open-source nature of the Milestone Module, an API request could not be performed to access the necessary data. As a workaround, web scraping was employed to retrieve the required information from the portal. Given the technical complexity of the webpage, Selenium was chosen over BeautifulSoup as it allows for better interaction with dynamic elements on the page, such as JavaScript-rendered content.

The script we developed using Selenium performed as expected and successfully extracted the milestone data into a JSON format. This format will be invaluable for future analysis of each project's Catalyst journey, tracking milestones, performance reviews, and stakeholder feedback.

**Methodology**

Web scraping to gather milestone data, ensuring comprehensive data extraction despite the absence of API access.
Public documentation of project milestones, which were stored in GitHub repositories and GitBook, ensuring transparency and accessibility to the community.
Stakeholder involvement: Continuous feedback from key stakeholders—Catalyst Team, developers, AI experts, and community reviewers—was integrated into the project, ensuring alignment with governance improvement goals.
AI Integration: Discussions around the role of AI in Catalyst governance were a focal point, with explorations of both the risks and opportunities that AI presents.
This combination of technical data scraping, stakeholder engagement, and AI integration ensures that the analysis is robust and designed to evolve with future developments.

**Conclusion**

The Data-Driven Catalyst project has successfully laid the foundation for a transparent and collaborative data analytics framework. By overcoming technical challenges with web scraping and using Selenium to gather key milestone data, the project is equipped with the necessary information to analyze project performance and track the progression of various Catalyst initiatives.

The data retrieved will be used in future analyses to assess the success of governance improvements, the influence of AI on decision-making, and the impact of community feedback. Future milestones will build on this work, ensuring the continued integration of stakeholder input and the development of a robust data-driven governance model for Project Catalyst.

## **Research Topic 6: Rotational Breaks for Big Winners: The Impact of Past Success on Current Funding**

**Objective**:
To analyze how the success of entities in previous funding rounds affects their chances in current and future rounds. The concept of "rotational breaks" explores whether taking a break from awarding funds to big winners could create a more equitable distribution of resources.

### Scenario 1: Big winners take rotational break

Generate synthetic historical funding data to simulate different scenarios where big winners take rotational breaks. This can help in understanding how the distribution of funds might change if certain entities are temporarily excluded from receiving funding. 

To explore **"Rotational Breaks for Big Winners"** and simulate scenarios where past successful applicants are given breaks or reduced priority, generative AI can help model and simulate various outcomes based on historical data. 

**Methodology**
**Step 1: Gather and Prepare Data**

First, collect your historical funding data, including:
- Proposal submission data.
- Amount requested and received.
- Success rates by proposer.
- Group/entity information.
- Time of submissions (to track when winners apply for funding).
  
**Step 2: Define "Big Winners"**
Define criteria for "big winners" based on your dataset. This could be:
- Entities with a high success rate (e.g., winning more than 70% of the time).
- Entities that have won above a certain threshold (e.g., those who have received the highest percentage of total funds).
Create a binary flag in your dataset indicating whether a group is a big winner.

**Step 3: Model Rotational Breaks for Big Winners**
Using **Generative AI**, we can simulate the effect of rotational breaks by generating various scenarios based on different rules. Here's a simplified structure of how you could implement this. In our simultion, we assume that big winners cannot apply for funding in consecutive rounds.

**Step 4: Analyze the Impact of Rotational Breaks**
Using the simulation technique in Python, you can analyze:
- How funding distribution changes.
- Whether new entities (that were previously underfunded) receive more funds.
- Whether diversity in the winning groups increases.

**Step 5: Visualization**
Visualize the difference in funding distribution with and without rotational breaks:
- **Bar charts** showing the amount of funding received by big winners before and after breaks.
- **Line charts** showing the success rate of big winners and other groups across different funding rounds.

### Analysis Overview: Funding Distribution Before and After the Exclusion of Big Winners (Funds 7–10)

### **Fund 7**

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/BeforeExclusionF7.png)

- **Before Exclusion**: In Fund 7, we observed a highly concentrated distribution of funding, with groups like **Wolfram Blockchain Labs** and **ZenGate Global** dominating the funding received. Several other smaller groups received significantly less funding.


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/AfterExclusionF7.png)

- **After Exclusion**: Once the big winners were excluded, the funding became more evenly distributed among smaller groups such as **RootsID**, **dcSpark**, and **LATAM Cardano Community**, who previously had lower shares of funding. **dcSpark** emerged as a top recipient, showcasing the ability for other groups to secure funding when dominant players are removed.
---

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/BeforeExclusionF8.png)

### **Fund 8**
- **Before Exclusion**: In Fund 8, the distribution before exclusion was again dominated by a few major players, including **ZenGate Global**, **Wolfram Blockchain Labs**, and **VIPER Staking**, which received large amounts of funding. Smaller groups struggled to receive substantial shares of the total funding available.


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/AfterExclusionF8.png)

- **After Exclusion**: After excluding the big winners, groups like **PolyCrypt**, **MigMake Pte Ltd**, and **LATAM Cardano Community** saw a marked increase in their share of funding. **Wada** and **PolyCrypt** emerged as significant beneficiaries after the exclusion, reinforcing the fact that removing dominant players opens up opportunities for smaller or less-represented groups.

---

### **Fund 9**


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/BeforeExclusionF9.png)

- **Before Exclusion**: In Fund 9, the distribution pattern was similar, with **ZenGate Global** and **Wolfram Blockchain Labs** again receiving a significant portion of the total available funding. Smaller groups, while present, had comparatively lower levels of funding.


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/AfterExclusionF9.png)
  
- **After Exclusion**: Post-exclusion, the removal of dominant players like **ZenGate Global** allowed groups such as **SWARM**, **LATAM Cardano Community**, and **Hippocrates** to secure larger portions of funding. **Geneva** also emerged as a major recipient in this fund. The exclusion process demonstrated that smaller players could access more resources when larger ones were removed from the equation.

---

### **Fund 10**


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/BeforeExclusionF10.png)

- **Before Exclusion**: In Fund 10, funding was even more concentrated, with **ZenGate Global** and **Wolfram Blockchain Labs** dominating the total amount received. Smaller groups were again overshadowed by the large players.
- 

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/AfterExclusionF10.png)

- **After Exclusion**: After the big winners were excluded, we observed a dramatic shift. Groups like **dcSpark**, **LATAM Cardano Community**, and **Wolfram Blockchain Labs** saw significant improvements in their relative share of funding. Smaller groups that were previously underfunded gained a more equitable share of the available resources.


---

### Key Insights:
1. **Impact of Exclusion**: Across all funds, excluding big winners resulted in a more **equitable distribution of funding**. Groups that had previously received small portions of the available funding were able to secure more significant shares once dominant players were removed.
   
2. **Rebalancing the Ecosystem**: Excluding big winners allows for the rebalancing of the ecosystem, promoting diversity and giving smaller, underrepresented groups a better chance to secure resources. In all four funds (7 through 10), the exclusion of top recipients led to a more balanced funding landscape, which could promote innovation and encourage wider participation.

3. **Dominant Players**: Before exclusion, dominant players like **ZenGate Global** and **Wolfram Blockchain Labs** received large portions of the funding across multiple funds. The consistent dominance of these groups highlights the potential challenge of monopolization in funding rounds, and how policies like exclusions can provide relief to smaller groups.

### Conclusion:
The analysis of Funds 7 through 10 demonstrates that excluding big winners results in more diverse funding outcomes and provides opportunities for a broader range of participants to benefit. These findings highlight the importance of considering policies that prevent the same groups from monopolizing funding rounds, thus fostering a healthier and more inclusive ecosystem.

---

### Scenario 2: Placing cap on total funding amount per team

Given that there is already a cap in place limiting the amount per proposal to no more than 10% of the budget in each funding category, you might wonder whether an additional cap on the "total funding" a team can receive is still useful or necessary. 

o	Without a total funding cap per team, big winners could consistently secure large amounts of funding in each round, even if no single proposal exceeds the 10% cap. This could lead to repeated monopolization over multiple funding rounds, limiting opportunities for smaller or newer teams.
o	By implementing a total funding cap per team, you create a system where the total allocation across all proposals submitted by a team is limited, ensuring a broader distribution of funds.
A total cap ensures that no single team can accumulate an excessive share of the funding, thereby opening the door for smaller, innovative teams that may have fewer proposals but are working on impactful projects.

### Effects of placing 10% cap


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund7capped10pc.png)

* Fund 7
•	Original distribution shows some groups, like Wolfram Blockchain Labs and Hippocrates, receiving large amounts of funding.

•	After applying the 10% cap, the distribution becomes more balanced, with larger recipients being brought down, allowing smaller groups like Protospace and RootsID to receive relatively higher amounts.


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund8capped10pc.png)

* Fund 8
•	Clear dominance of groups like M Labs and Dandelion Inc in the original distribution, with very large amounts allocated.

•	The 10% cap reduces their share significantly, resulting in a more equitable distribution, allowing underfunded groups like NFT-DAO and Dynamic Strategies to receive more in comparison.

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund9capped10pc.png)


* Fund 9
•	Several groups, such as LIDO Nation and Wolfram Blockchain Labs, received large amounts in the original distribution.

•	With the cap applied, their funding is limited, leading to a more equal allocation, benefiting smaller groups like Hippocrates and The Art.

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund10capped10pc.png)

* Fund 10
•	A standout large recipient is FLUID7, which received a significantly higher share in the original distribution.
•	After the cap is applied, the funding becomes more balanced, and groups like DAOGEN.AI and Andamio Platform see their shares increased relatively.

General Observations:
•	The 10% cap consistently reduces the dominance of the big winners across all four funds, promoting a more even distribution of funding.
•	Smaller groups that were overshadowed in the original funding allocations benefit from the cap, fostering a more equitable ecosystem.
•	The original distributions highlight the concentration of funding among a few dominant players, whereas the capped distribution aims for more diverse participation.


# **Research Topic 7: Scamming Catalyst: Cloned and Copied Ideas/Proposals Submitted Last Minute**

## **Objective**:
To identify and analyze the phenomenon of cloned or copied proposals submitted close to the deadline in a funding environment. The goal is to understand the prevalence, characteristics, and impact of such fraudulent activities on the integrity of the funding process and to develop strategies for detecting and mitigating these practices.

**Textual Analysis and Similarity Detection**:
**Unsupervised Learning**: Apply natural language processing (NLP) techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) or word embeddings to measure the similarity between proposals. This can help in identifying cases where proposals are not just similar in content but potentially identical or minimally altered.
**Generative AI**: Generate paraphrased versions of original proposals to simulate potential cloning attempts. This can improve the robustness of detection algorithms by training them to recognize both direct copies and slightly altered clones.

The shortest and simplest approach to detect cloned proposals while still providing effective results would be using TF-IDF (Term Frequency-Inverse Document Frequency) combined with **Cosine Similarity**. This approach is computationally efficient, easy to implement, and provides reliable results for detecting text similarities without requiring complex models or extensive preprocessing.
- **TF-IDF**: Captures the importance of terms in each proposal (titles, problems, solutions) and transforms the text into numerical vectors.
- **Cosine Similarity**: Measures how similar two proposals are based on their TF-IDF vectors. It’s a quick and effective way to compare textual data.

We used a **TF-IDF + Cosine Similarity** approach to measure the textual similarity between proposals. The analysis was based on the following key components of each proposal:
1. **Title**
2. **Problem Statement**
3. **Solution Statement**

**Steps**:
1. **Data Preprocessing**: We combined the title, problem, and solution statements of each proposal into a single text field.
2. **Text Vectorization**: The combined text for each proposal was vectorized using **TF-IDF** (Term Frequency-Inverse Document Frequency), which converts the text into numerical vectors based on the importance of words.
3. **Cosine Similarity Calculation**: We calculated the cosine similarity between the vectors to determine how similar each proposal was to every other proposal.
4. **Threshold for Cloning Detection**: A similarity score threshold of **0.85** was set to flag potential clones, with scores closer to 1.0 indicating near-identical proposals.

#### **Key Findings**
The analysis identified several pairs of proposals with high similarity scores. These pairs are considered **potential cloned proposals**. Below are the top findings:
- **Top Similarity Scores**: Some proposals had perfect or near-perfect similarity scores of **1.0**, indicating that they may be identical or only slightly modified versions of each other. This could be due to moving proposal across different challenges or categories. 
  Examples of highly similar proposal pairs:
  - Proposal with index `30` and Proposal with index `416` had a similarity score of **1.0**.
  - Proposal with index `33` and Proposal with index `367` had a similarity score of **0.865**.
  
- **Multiple Cloning**: Several proposals appeared in multiple high-similarity pairs, suggesting the presence of **duplicated or highly similar proposals submitted by the same or different groups**.

 
#### **Visualization of Results**
##### **1. Heatmap of Cosine Similarities**
A heatmap was generated to visualize the overall **cosine similarity** between proposals. This allowed us to quickly identify clusters of similar proposals.
**Key Insights**:
- The heatmap revealed distinct clusters of highly similar proposals, indicated by darker colors.
- These clusters represent groups of proposals that are likely cloned or heavily borrowed from each other.

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/heatmapclone_fund7.png)

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/heatmapclone_fund8.png)

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/heatmapclone_fund9.png)

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/heatmapclone_fund10.png)

##### **2. Network Graph of Similar Proposals**
A network graph was used to visualize the relationships between highly similar proposals (similarity > 0.85).

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/similarity_network_fund7.png)

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/similarity_network_fund8.png)

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/similarity_network_fund9.png)

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/similarity_network_fund10.png)

**Key Insights**:
- Nodes represented individual proposals, and edges (connections) indicated high similarity between proposals.
- The network graph highlighted several **densely connected groups**, indicating potential cloning activities.

Based on the analysis, several proposals have been flagged as potential clones. Here are the recommended next steps:

1. **Manual Review**:
   - A manual review of the flagged proposals should be conducted, especially for pairs with similarity scores greater than **0.85**. This review will help confirm whether the proposals are indeed clones.
2. **Policy Review**:
   - Consider introducing stricter **guidelines and checks** to detect and prevent the submission of cloned proposals in future funding rounds.
   - Implement an automated system to flag similar proposals before the final submission deadline to avoid cloning issues.
3. **Further Exploration**:
   - **Investigate Proposer Networks**: Analyze the proposers' connections to see if the same teams or individuals are submitting multiple similar proposals.
   - **Expand the Analysis**: Apply the same method across other funds to detect cloning trends over time.

***

### 📽 Presentation slides for the community-tasked Data Reports can be downloaded from this [Google Drive Presentation Link](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/deep-dive.md)
