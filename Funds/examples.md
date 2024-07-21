# 20 examples of Data-Driven Reports using Funds 7 to 10

Rationale: we want to showcase potential for useful community reporting based initially on 3 datasets. At later milestones, more data sources can be added, as "everything is data". This could include social media, Github, LinkedIn, the Milestone module, community-driven or catalyst-funded explorers, databases and APIs like Lido Nation, Wolfram, Cardano Cube and so on.

Based on these examples, much more in-depth analysis will be carried out for 7 directions provided by the community or stakeholders that have exceptional potential to improve decision making or help voters, proposers and governance functions in steering the Catalyst process towards better funding outcomes.

Deliberately leaving out F-11 and F-12 allows us to improve significantly on the in-depth analysis and preserve unused data to test assumptions and conclusions out of sample while maintaining a large enough dataset that includes mixed USD and ADA funding amounts.

This section was collated by combining various team inputs. If you have feedback, suggestions or requests for data reports, please submit an [Issue](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/issues) (which we "abuse" like a simplified Slack Channel) or send us a [DM or Tweet](https://x.com/SapientSwarm).


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

### 2. Boxplot of Proposal Assessor Scores and Funding Success

![Boxplot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund_boxplot.png)

*Inspired by OG community member Victor Corcino's post on the Community Advisor Telegram channel and teased in our Fund-11 proposal submission* 

This chart is a good way to visualized the increasing and then dropping influence of the CA/CR/PA score for the voter. In Fund-10, maybe partially motivated by Victor's findings, but mainly to counter the incentive for "fake" or "friendly" reviews, some changes were introduce to blunt, but not remove, the importance of community scoring: the voting app no longer sorts automatically by score, and the pay per review was also reduced to "encourage" shorter proposal reviews.

### 3. Funding Request by Fund and Status

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/funding_request_bubble_plot_log_scale.png)

*This plot shows in green proposals that were funded from Fund7 through Fund10 and red those that were not funded plotted along a log scale of funding requested*

### 4. YES votes Required for Funding across Funds

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/yes_votes_bubble_plot.png)

*A similar data visualization with very different focus and on different data: how many YES votes were required from fund to fund to get voted in*

### 5. Treemap of Historical Challenges

![Thumbnail](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/treemap.jpg)

*Treemap showing as box height percentage of funded proposals and box length total funding rewarded* 

The detailed clickable treemap can be downloaded [here](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/category_funding_treemap.html) for use in your own browser (optimized for Chrome/Brave).

Treemaps are somewhat contoversial in the Data Science community as they are often showy and worse than a simple barchart or histogram for the same dataset. Here, the color coding of funds and meaningful box sizes and shapes are in our opinion a very good use of this complex data visualization technique and ideally suited for Catalyst analysis.

### 6. Distribution of Amount Requested

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/lnhist_python.png)

*The log-transformed histogram shows a concentrated range of requested amounts with a prominent peak around the log value of 10, and it also reveals the spread and occasional outliers in the data.* 
The peak around the log value of 10 suggests a significant number of proposals requested amounts in that range. This corresponds to a requested amount of approximately 𝑒10 or 22,026 in the original scale. The distribution tapers off on both sides, indicating fewer proposals requested significantly lower or higher amounts. There are very few proposals with extremely high log values (above 13), indicating that only a small number of requests are significantly larger than the majority.

### 7. Scatter Plot of Log-Transformed Amount Requested vs Amount Received with Clusters and Outliers (Spot exceptional proposals)

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/scatter_plot.png)

*A positive correlation between the amount requested and the amount received, with distinct clusters representing different ranges of funding. The outliers highlight exceptional cases that do not follow the general trend.*

Clusters:
Cluster 0 (Teal): This cluster predominantly occupies the lower left region of the plot, indicating proposals that requested and received relatively lower amounts.

Cluster 1 (Yellow): This cluster spans the middle range, showing proposals that requested and received moderate amounts.

Cluster 2 (Purple): This cluster is located towards the upper right region, indicating proposals that requested and received higher amounts.

The outliers, marked with a star and labeled in red, are proposals that significantly deviate from the general trend. These outliers have been identified using z-scores, with a threshold of 3 standard deviations from the mean.

The presence of an outlier in the upper right region suggests that there are a few proposals that requested and received much higher amounts compared to others. This could indicate exceptional cases or specific funding scenarios that need further investigation.

### 8. SpiderChart to Visualize Fund Growth

![SpiderChart](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/spiderChart.jpg)

*From Fund7 to Fund10, the fund size and number of proposals has grown exponentially. This Radar chart aka Spider chart shows this nicely*

Radar or Spider charts can visualize multiple dimensions on a 2D plot, with each dimension represented by a ray of the radar or line on web while the other 2 elements of the chart plot the axis. By normalizing the axis to the maximum amount, it allows comparison of number of proposals with the median requested amount. This reveals that the number of proposals submitted picked up even before the funding amount caught up. This chart type allows any kind of complex analysis to be easily understood. While there might be better use of this technique for fund data, keep in mind that this plot type exists in our open source plotting library as it may come in handy!

### 9. Removal of Challenge Categorization Visualized

![DonutChart](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund_category_donuts.png)

*In Fund7 and Fund8, niche challenge setting were encouraged to flourish whereas from Fund9 onwards, protection of specialized topics was greatly reduced.*

Using our Open Source Data Science stack introduced in Milestone-1 for advanced plotting allows four donut charts of Fund-7 to Fund-10 to appear in the same plot with their challenge settings / categories as % of the total fund shown inside.

### 10. Plotting Number of Submissions per Fund per Entity

*This report shows how many proposals were submitted by the most active Groups (entities submitting proposals for the Catalyst vote) prior to this number being limited to 5 in Fund-11 and then 6 in Fund-12*

![Fund10](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund10.png)

*Seeing the total number by some entities that may not necessarily have the capacity to close all proposals if funded makes it obvious why the rule of 6 was introduced. It also puts undue workload on community reviewers having to sift through large quantities instead of digesting a lower number of quality proposals.*

![Fund9](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund9.png)

*Fund-9 stood out mainly because of the large funding amount in one challenge setting, but the number per entity was also too large.*
  
![Fund8](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund8.png)

*And the same analysis for Fund-8, in between F7 and F9/F10 in terms of severity.*

![Fund7](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/groupsFund7.png)

*Fund-7 was still early in the process with very little in terms of "abuse" being observed*

### 11. Heatmap of Community Reviewer Note Length and Score (Refined)

![Previous](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/heatmap.png)

*For Milestone 1 we presented this simple heatmap and suggested that rule changes to CR can alter their behavior from fund to fund.*

This heatmap has now been refined (see below) to take full advantage of the capability of the open source data science libraries introduced.

![Revamp](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/revampedHeatmap.png)

As per our "exercise" in the Casestudy, this adds Fund-7 data, plots more smoothly and uses a score aggregate instead of only the Impact score which is consistent across funds. This visualized dramatically how changing the Filtered Out features of community reviews changed over time. Fund7 was permissive, then CRs were not paid for proposer filtered scored that violate the rules so comment length skyrocketed. Relaxing the filtering out process reversed some of this. Later analysis of Fund-11 and Fund-11 will very likely show a dramatic decline in word count, regardless of scoring given, as the filtering out was completely dropped and the pay lowered. Also noteworthy is the length of negative comments, which are especially prone to proposer complaint (F8 and F9).


### 12. Converting Milestone Tool Data to JSON

Reports do not necessary have to be executive data visualization reports for decision makers like voters, assessors or governance to glance over and make more informed decisions. There are a lot of examples where Catalyst ecosystem data can be made into reports and data can be retrieved that is meaningful to certain tools or communities and allow them in turn to improve the process. One member of the community sent us this special request and we have created a script and example output for it. If this report is voted into the Top-7, a lot more can be done to prepare data for example from the Milestone Module for use with open source data science tools.

![JSON](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Milestones/json.jpg)

We have scraped out own Milestone 1 with Selenium, which has the ability to produce more robust scripts than BeautifulSoup4 to deal with the interactive widgets of the Milestone Module. The outputs are shared in a new [folder](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/tree/main/Funds/Milestones) on this repo.

![Thumbnail](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Milestones/json.png)


### 13. Project Funding and Completion Rates Across Catalyst Funds 7-10

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/CompletedProject.png)

*The completion rate appears to decrease in later funds, particularly in Fund 10, which could be due to ongoing projects or changes in the funding process.
The number of funded projects varies between funds, with Fund 8 showing the highest number of funded projects.*

Further Analysis Opportunity: This data suggests the potential for an in-depth investigation into project completion patterns. Specifically, it may be valuable to identify teams that have proposed projects but failed to complete them prior to Fund 9. Such an analysis could provide insights into factors affecting project completion rates and inform future funding decisions.

### 14. Analysis of Top 3 Dominating Groups by Amount Requested Across Funds for Each Challenge/Category

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/stacked_f7_group.png)

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/stacked_f8_group.png)

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/stacked_f9_group.png)

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/stacked_f10_group.png)

*The stacked bar chart shows the total amount requested by the top 3 groups in each fund.
It highlights how a few groups dominate the funding requests, potentially overshadowing smaller or newer teams.*

The need for "Cap the Total Amount Requested by Each Group per Challenge/Category"
Currently, the rules only limit the amount that can be requested per individual proposal within each challenge/category. However, this analysis reveals a critical issue: groups can still dominate by submitting multiple proposals, effectively circumventing the cap on individual proposals. This creates an uneven playing field where a few established groups with strong reputations can submit 5-6 proposals, making it difficult for other teams to compete fairly.


### 15. Plotly Interactive Column Chart of all Scoring by PA per Fund

![JPG](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/PAscoresStack.jpg)

*Some of the plotting packages introduced in our OSDS section allow interactive plots that the user can twist and turn. This makes hard to read multi-dimensional analysis easier to understand.*

[Download](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/pa_3d_stacked_column_chart.html) the HTML file to play with in your own brower.

This analysis shows total number of reviews per fund color-coded by the bin of the average score across 3 category. This may help governance functions to understand how gaming of average scores occurs or what policy changes did to CA/PA/CR behavior. What this plot shows quite clearly is how policy changes affect assessor "kindness" resulting in a spike of friendly reviews (the only way to get paid) in Fund-9. Corrective measures of this undesired effect have already been taken by the Catalyst Team / rulebook.

### 16. Rotational Breaks for Big Winners: The Impact of Past Success on Current Funding

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/pastsuccessyaxis.png)

*To sustain a vibrant and diverse innovation ecosystem, it's crucial to prevent a few dominant players from monopolizing funding opportunities.*

By encouraging high-success groups to take a break between funding rounds, we create space for new and underrepresented teams to shine. This rotational approach not only nurtures fresh ideas and perspectives but also mitigates the risk of stagnation, fostering a more inclusive and dynamic environment for all innovators. 


### 17. Identifying Proposal Assessor "Factories" and Clusters of Low/High Scores

![Plot](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/assessorFactories.jpg)

*There is too much going on om this plot, but as a comprehensive plot covering all funds, all assessors and all scores it can give the observer a lot of ideas.*

Excessive amounts of reviews per assessor and inactive reviewers giving very high and very low scores for tactical reasons are both huge problems of decentralized ranking and have been addressed by fine-tuning the allocation of proposals to reviewers and changing filtering and moderation rules from fund to fund. Although gaming among proposals increased over the funds, the reviewers have arguably become more well-behaved.

### 18. Getting Started with NLP: Proposal Title Wordcloud

![Wordcloud](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/expanded_keyword_wordcloud.png)

*Although advanced natural language processing will only start with the next Milestone, here is a sneak-preview showing the most popular words appearing in 6000 proposal titles in the funds dataset.*

This wordcloud goes beyond beautiful optics of what you may expect people to proposed about. If applied by fund, for example, it can show how themes and directions change over time and can allow governance functions to encourage certain areas that may fall out of favor but require urgent attention, like DeFi, DAO and multi-sig.


### 19. Interactive Massive Scatterplots

*Only looking at F9 data*

![F9](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/PAdispesionF9.png)

*All funds selected*

![All funds](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/PAdispesionFx.png)

Plotly allows output as dynamic HTML files, here allowing the dispersion metric (how far apart are the scores in Impact, Value and Feasibility rating measured by Sigma) versus average scores for each assessor. You can play with this yourself if you download the [HTML output](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/PA_score_dispersion_plot.html) and view in your Chrome browser.
