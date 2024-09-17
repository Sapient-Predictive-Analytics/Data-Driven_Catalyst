# Deep-dive Data Reports

# Placing cap on total funding amount per team

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



