# Deep-dive Data Reports

# ### **Research Topic 7: Rotational Breaks for Big Winners: The Impact of Past Success on Current Funding**

#### **Objective**:
To analyze how the success of entities in previous funding rounds affects their chances in current and future rounds. The concept of "rotational breaks" explores whether taking a break from awarding funds to big winners could create a more equitable distribution of resources.

# Scenario 1: Big winners take rotational break

Generate synthetic historical funding data to simulate different scenarios where big winners take rotational breaks. This can help in understanding how the distribution of funds might change if certain entities are temporarily excluded from receiving funding. 

To explore **"Rotational Breaks for Big Winners"** and simulate scenarios where past successful applicants are given breaks or reduced priority, generative AI can help model and simulate various outcomes based on historical data. 

#### Methodology 
### **Step 1: Gather and Prepare Data**

First, collect your historical funding data, including:
- Proposal submission data.
- Amount requested and received.
- Success rates by proposer.
- Group/entity information.
- Time of submissions (to track when winners apply for funding).
  
### **Step 2: Define "Big Winners"**
Define criteria for "big winners" based on your dataset. This could be:
- Entities with a high success rate (e.g., winning more than 70% of the time).
- Entities that have won above a certain threshold (e.g., those who have received the highest percentage of total funds).
Create a binary flag in your dataset indicating whether a group is a big winner.

### **Step 3: Model Rotational Breaks for Big Winners**
Using **Generative AI**, we can simulate the effect of rotational breaks by generating various scenarios based on different rules. Here's a simplified structure of how you could implement this. In our simultion, we assume that big winners cannot apply for funding in consecutive rounds.

### **Step 4: Analyze the Impact of Rotational Breaks**
Using the simulation technique in Python, you can analyze:
- How funding distribution changes.
- Whether new entities (that were previously underfunded) receive more funds.
- Whether diversity in the winning groups increases.

### **Step 5: Visualization**
Visualize the difference in funding distribution with and without rotational breaks:
- **Bar charts** showing the amount of funding received by big winners before and after breaks.
- **Line charts** showing the success rate of big winners and other groups across different funding rounds.

# Scenario 2: Placing cap on total funding amount per team

Given that there is already a cap in place limiting the amount per proposal to no more than 10% of the budget in each funding category, you might wonder whether an additional cap on the "total funding" a team can receive is still useful or necessary. 

o	Without a total funding cap per team, big winners could consistently secure large amounts of funding in each round, even if no single proposal exceeds the 10% cap. This could lead to repeated monopolization over multiple funding rounds, limiting opportunities for smaller or newer teams.
o	By implementing a total funding cap per team, you create a system where the total allocation across all proposals submitted by a team is limited, ensuring a broader distribution of funds.
A total cap ensures that no single team can accumulate an excessive share of the funding, thereby opening the door for smaller, innovative teams that may have fewer proposals but are working on impactful projects.

# Effects of placing 10% cap


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund7capped10pc.png)

#Fund 7
•	Original distribution shows some groups, like Wolfram Blockchain Labs and Hippocrates, receiving large amounts of funding.

•	After applying the 10% cap, the distribution becomes more balanced, with larger recipients being brought down, allowing smaller groups like Protospace and RootsID to receive relatively higher amounts.


![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund8capped10pc.png)

#Fund 8
•	Clear dominance of groups like M Labs and Dandelion Inc in the original distribution, with very large amounts allocated.

•	The 10% cap reduces their share significantly, resulting in a more equitable distribution, allowing underfunded groups like NFT-DAO and Dynamic Strategies to receive more in comparison.

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund9capped10pc.png)


#Fund 9
•	Several groups, such as LIDO Nation and Wolfram Blockchain Labs, received large amounts in the original distribution.

•	With the cap applied, their funding is limited, leading to a more equal allocation, benefiting smaller groups like Hippocrates and The Art.

![Samples](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/fund10capped10pc.png)

#Fund 10
•	A standout large recipient is FLUID7, which received a significantly higher share in the original distribution.
•	After the cap is applied, the funding becomes more balanced, and groups like DAOGEN.AI and Andamio Platform see their shares increased relatively.

General Observations:
•	The 10% cap consistently reduces the dominance of the big winners across all four funds, promoting a more even distribution of funding.
•	Smaller groups that were overshadowed in the original funding allocations benefit from the cap, fostering a more equitable ecosystem.
•	The original distributions highlight the concentration of funding among a few dominant players, whereas the capped distribution aims for more diverse participation.


# ### **Research Topic 8: Scamming Catalyst: Cloned and Copied Ideas/Proposals Submitted Last Minute**

#### **Objective**:
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







