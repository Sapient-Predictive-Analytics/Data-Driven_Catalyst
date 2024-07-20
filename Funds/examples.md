# 20 examples of Data-Driven Reports using Funds 7 to 10

Rationale: we want to showcase potential for useful community reporting based initially on 3 datasets. At later milestones, more data sources can be added, as "everything is data". This could include social media, Github, LinkedIn, the Milestone module, community-driven or catalyst-funded explorers, databases and APIs like Lido Nation, Wolfram, Cardano Cube and so on.

Based on these examples, much more in-depth analysis will be carried out for 7 directions provided by the community or stakeholders that have exceptional potential to improve decision making or help voters, proposers and governance functions in steering the Catalyst process towards better funding outcomes.

Deliberately leaving out F-11 and F-12 allows us to improve significantly on the in-depth analysis and preserve unused data to test assumptions and conclusions out of sample while maintaining a large enough dataset that includes mixed USD and ADA funding amounts.


## The Datasets

### Voting Results Dataset
We collected, cleaned and simplified public voting results data into a single voting results dataset.

### Community Reviewer Dataset
Based on the casestudy Community Reviewer files, this large dataset comprises all proposal assessments for scoring in the voting app.

### The LidoNation Dataset
This dataset is built from downloads of the publicly accessible [LidoNation Explorer](https://www.lidonation.com/en/catalyst-explorer/).


## The Reports

### 1. Keyword Occurrences vs Funding Ratio

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/keyword_status_analysis.png)

*This plot shows the success ratio of proposals containing a certain keyword, versus the benchmark funding ratio of 18.7% and plots the number of occurrences as well*

Proposals with *Africa* in the title performed a lot better than *DeFi* with similar occurrence in the 100 proposals ballpark. This shows the perception of Cardano strength on the continent and its importance for strategic differentiation compared to perceived weakness or undesirability of decentralized financial markets. Adding more similar keywords to the study, looking at more funds could improve this analysis further.

Useful for: voters (bias, funding direction, ecosystem growth), proposers (boosting chances), governance (understanding voting power)

### 2. Funding Request by Fund and Status

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/funding_request_bubble_plot_log_scale.png)

*This plot shows in green proposals that were funded from Fund7 through Fund10 and red those that were not funded plotted along a log scale of funding requested*

### 3. YES votes Required for Funding across Funds

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/yes_votes_bubble_plot.png)

*A similar data visualization with very different focus and on different data: how many YES votes were required from fund to fund to get voted in*

### 4. Treemap of Historical Challenges

![Thumbnail](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/treemap.jpg)

*Treemap showing as box height percentage of funded proposals and box length total funding rewarded* 

The detailed clickable treemap can be downloaded [here](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/category_funding_treemap.html) for use in your own browser (optimized for Chrome/Brave).

Treemaps are somewhat contoversial in the Data Science community as they are often showy and worse than a simple barchart or histogram for the same dataset. Here, the color coding of funds and meaningful box sizes and shapes are in our opinion a very good use of this complex data visualization technique and ideally suited for Catalyst analysis.

### 5. Distribution of Amount Requested

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/lnhist_python.png)

*The log-transformed histogram shows a concentrated range of requested amounts with a prominent peak around the log value of 10, and it also reveals the spread and occasional outliers in the data.* 
The peak around the log value of 10 suggests a significant number of proposals requested amounts in that range. This corresponds to a requested amount of approximately 𝑒10 or 22,026 in the original scale. The distribution tapers off on both sides, indicating fewer proposals requested significantly lower or higher amounts. There are very few proposals with extremely high log values (above 13), indicating that only a small number of requests are significantly larger than the majority.

### 6. Scatter Plot of Log-Transformed Amount Requested vs Amount Received with Clusters and Outliers (Spot exceptional proposals)

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/scatter_plot.png)

*A positive correlation between the amount requested and the amount received, with distinct clusters representing different ranges of funding. The outliers highlight exceptional cases that do not follow the general trend.*

Clusters:
Cluster 0 (Teal): This cluster predominantly occupies the lower left region of the plot, indicating proposals that requested and received relatively lower amounts.

Cluster 1 (Yellow): This cluster spans the middle range, showing proposals that requested and received moderate amounts.

Cluster 2 (Purple): This cluster is located towards the upper right region, indicating proposals that requested and received higher amounts.

The outliers, marked with a star and labeled in red, are proposals that significantly deviate from the general trend. These outliers have been identified using z-scores, with a threshold of 3 standard deviations from the mean.

The presence of an outlier in the upper right region suggests that there are a few proposals that requested and received much higher amounts compared to others. This could indicate exceptional cases or specific funding scenarios that need further investigation.

### 7. SpiderChart to Visualize Fund Growth

![SpiderChart](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/spiderChart.jpg)

*From Fund7 to Fund10, the fund size and number of proposals has grown exponentially. This Radar chart aka Spider chart shows this nicely*

Radar or Spider charts can visualize multiple dimensions on a 2D plot, with each dimension represented by a ray of the radar or line on web while the other 2 elements of the chart plot the axis. By normalizing the axis to the maximum amount, it allows comparison of number of proposals with the median requested amount. This reveals that the number of proposals submitted picked up even before the funding amount caught up. This chart type allows any kind of complex analysis to be easily understood. While there might be better use of this technique for fund data, keep in mind that this plot type exists in our open source plotting library as it may come in handy!

### 8. Removal of Challenge Categorization Visualized

![DonutChart](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund_category_donuts.png)

*In Fund7 and Fund8, niche challenge setting were encouraged to flourish whereas from Fund9 onwards, protection of specialized topics was greatly reduced.*

Using our Open Source Data Science stack introduced in Milestone-1 for advanced plotting allows four donut charts of Fund-7 to Fund-10 to appear in the same plot with their challenge settings / categories as % of the total fund shown inside.

### 9. Plotting Number of Submissions per Fund per Entity

*This report shows how many proposals were submitted by the most active Groups (entities submitting proposals for the Catalyst vote) prior to this number being limited to 5 in Fund-11 and then 6 in Fund-12*

![Fund10](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund10.png)

*Seeing the total number by some entities that may not necessarily have the capacity to close all proposals if funded makes it obvious why the rule of 6 was introduced. It also puts undue workload on community reviewers having to sift through large quantities instead of digesting a lower number of quality proposals.*

![Fund9](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund9.png)

* Fund-9 stood out mainly because of the large funding amount in one challenge setting, but the number per entity was also too large.*
  
![Fund8](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund9.png)

*And the same analysis for Fund-8, in between F7 and F9/F10 in terms of severity.*

![Fund7](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund9.png)

*Fund-7 was still early in the process with very little in terms of "abuse" being observed*
