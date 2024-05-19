## Working with Fund Data
This section will demonstrate from simple examples to complex ones how past fund data can be collected, cleaned, aggregated and analyzed using the [Open Source Data Science Stack](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/OSDS.md) to yield insights. The basis for this is the Pandas Python library used for working with data sets that combines elements of Excel spreadsheet, the R language and SQL to offer an accessible framework that across our typical workload is more convenient or powerful than each of these tools on its own. Most importantly, it runs order of magnitude faster than an Excel worksheet would - which is the current format of presenting and analyzing Catalyst data for most users. Although Excel can be "forced" to perform statistical analysis and even machine learning as shown in John Foreman's excellent book [Data Smart](https://www.amazon.com/Data-Smart-Science-Transform-Information/dp/111866146X), it cannot do so without hogging resources and crashing if the datasets get too large.

### Fund-8 "CA/VCA Sheet"
[Zipped CSV File of Aggregated Community Reviews Raw Data Fund-8](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund8.zip)

### Fund-9 "CA/VCA Sheet"
[Zipped CSV File of Aggregated Community Reviews Raw Data Fund-9](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund9.zip)

### Fund-10 "CA/VCA Sheet"
[Zipped CSV File of Aggregated Community Reviews Raw Data Fund-10](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund10.zip)

### The Pandas DataFrame
Pandas is a an essential Python package (see OSDS) that we use a lot. It was designed for data manipulation and analysis by Wes McKinney in 2008, and has become an essential tool for data scientists and analysts due to its ability to handle diverse types of data and its rich in-built functionality. McKinney, who at the time worked in quantitative finance at quant hedge fund AQR Capital Management, developed Pandas to address the need for a more efficient and state of the art tool for data analysis in Python. His motivation was to enable more streamlined data manipulation, allowing users to spend less time on data preparation and more on deriving insights. He also wrote the excellent book [Python for Data Analysis](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662) that was one of the first stepping stones for our own quant finance journey over the last decade. The 2nd edition is not great for integrating the newest ML and plotting packages but gives an outstanding start with Pandas from its very creator. For analyzing our initial demo datasets from Catalyst funds 8 to 10, where proposers submitted close to 1000 proposals each and several hundred community reviewers scored them and wrote scoring ratione, Pandas offers several key features:

**Data Structures**
Pandas provides two primary data structures – Series (1-dimensional) and DataFrame (2-dimensional). These structures are optimized for performance and ease of use, enabling seamless handling of both numerical and textual data.

**Data Cleaning and Preparation**
With Pandas, you can easily clean and prepare data by handling missing values, transforming data types, and performing operations like merging, reshaping, and filtering data.

**Text and Numerical Analysis**
Pandas supports a variety of operations for both text and numerical data. It allows the user to leverage functions for text processing, such as string manipulation and applying regular expressions, alongside numerical operations like aggregation, descriptive statistics, and more.

**GroupBy Functionality** 
One of the most powerful features of Pandas is the groupby functionality. This allows splitting the data into groups based on some criteria, apply a function to each group independently, and then combine the results. For example, in analyzing Project Catalyst aggregate VCA/CA data, we can group proposals by proposers, reviewers, or other criteria, and then calculate average scores, count the length of comments by category, or perform other aggregations.

**Integration with Other Libraries**
Pandas integrates well with other Python libraries such as NumPy for numerical operations, Matplotlib and Seaborn for data visualization, and Scikit-learn for machine learning, enhancing its utility for comprehensive data analysis. See section [OSDS](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/OSDS.md) for the complete stack and how it builds nicely on Pandas.

Here is a simplified example of how to use Pandas to analyze Catalyst data to introduce the syntax:

~~~
# Import Pandas library
import pandas as pd

# Load data into a DataFrame
data = pd.read_csv('fundX.csv')

# Group by proposer and calculate the mean score for each proposer (assumes prior data cleaning or giving instructions to read_csv above)
mean_scores = data.groupby('proposer')['score'].mean()

# Group by reviewer and count the number of assessments each reviewer made
assessment_counts = data.groupby('reviewer')['assessments'].count()

# Display the results
print(mean_scores)
print(assessment_counts)
~~~

### Aggregation and Pandas Groupby Operations
As shown above, the Groupby object is a very useful data preparation step to avoid resource-consuming iteration and work database-like with our spreadsheet data. The first parameter to .groupby() can accept several different arguments:
* A column or list of columns
* A dict or pandas Series
* A NumPy array or pandas Index, or an array-like iterable of these
  
We can take advantage of the latter to group by for example bins of average scores etc.

A more detailed breakdown of how groupby works:

* **Split**: The data is divided into groups based on some criteria. This criteria can be one or more columns in your DataFrame. When we call groupby on a DataFrame, we specify which column(s) we want to group by. This divides the DataFrame into multiple groups based on unique values in the specified column(s).

* **Apply**: A function is applied to each group independently. This function can be a built-in aggregation function (such as sum, mean, count, etc.), a custom function, or even a combination of multiple functions. We apply various functions to each group. Common functions include aggregation: calculating a single value for each group, such as mean, sum, count, etc. Transformation: returning an object that's the same size as the group, typically used for normalization or other element-wise operations. Filtration: Returning subsets of the original object based on some group-wise criteria.

* **Combine**: The results of the function applications are combined into a new DataFrame or Series. The results of the applied functions are combined into a new DataFrame or Series, which can be used for further analysis or visualization.

**Similarity to SQL**
The groupby functionality in Pandas is conceptually similar to the GROUP BY clause in SQL. In SQL, GROUP BY is used to group rows that have the same values in specified columns into summary rows, like calculating the sum or average of each group.
For example, in SQL, to calculate the average score per proposer:

`SELECT proposer, AVG(score)`

`FROM data`

`GROUP BY proposer;`

Similar to Pandas, SQL's GROUP BY clause splits the data into groups based on the specified column(s) and then applies aggregation functions to each group.

### Visualizing Data from DataFrame
One of the major advantages of working with the Pandas DataFrame for this project is the ability to plot directly from the native dataset using Seaborn, Plotly, Matplotlib etc. Any changes, improvements or additional data happening in the DataFrame will immediately update our plots if we work with an interactive IPython notebook or an IDE like Spyder. If you want to take a deeper dive into the many possibilities of this, we can recommend [RealPython](https://realpython.com/pandas-plot-python/) as an entry to intermediate level free resource but there are countless MOOCs and ebooks on the subject thanks to Python's large scientific data community.
![RealPandas](https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/How-to-Plot-With-Pandas_Watermarked.5bb0299e061b.jpg)


### Interactive IPython Notebook
We start by importing Pandas, and loading the 3 available VCA files from the Funds data. The imports attempt to streamline the column names across different fund formats and category names, and try to cope with different language formats that may throw errors such as Vietnamese reviewer commentary etc.

~~~
"""
Case Study: Working with fund data.
Catalyst funds VCA sheet F8, F9, F10.
"""

# Import libraries
import pandas as pd

# Load data into a DataFrames for each Fund
fund8 = pd.read_csv('fund8.csv', names=['ID', 'Title', 'Challenge', 'Link', 'Reviewer',
                                          'Impact', 'Score_i', 'Feasibility', 'Score_ii', 'Cat3', 'Score_iii',                                         
                                          'Rationale', 'Exc', 'Good', 'FO'], header=None, encoding='cp1252')
fund9 = pd.read_csv('fund9.csv', names=['ID', 'Challenge', 'Title', 'Link', 'Reviewer',
                                          'xID1', 'xID2', 'xID3', 'Impact', 'Score_i', 'Feasibility', 
                                          'Score_ii', 'Cat3', 'Score_iii', 'Mark', 'Rationale'], header=None, 
                                            encoding='cp1252')
fund10 = pd.read_csv('fund10.csv', names=['ID', 'Reviewer', 'Impact', 'Score_i', 'Feasibility', 'Score_ii',
                                            'Cat3', 'Score_iii', 'Level', 'Alloc', 'xID1', 'Link', 'Title', 'Tot',
                                            'Valid', 'Pct', 'In'], header=None, encoding='cp1252')

# Add Fund column, remove idiosyncracies
fund8['Fund'] = 'Fund8'
fund9['Fund'] = 'Fund9'
fund10['Fund'] = 'Fund10'
fund8 = fund8.drop(labels=['Challenge', 'Exc', 'Good', 'FO', 'Rationale'], axis=1)
fund9 = fund9.drop(labels=['Challenge', 'xID1', 'xID2', 'xID3', 'Mark', 'Rationale'], axis=1)
fund10 = fund10.drop(labels=['Level', 'Alloc', 'xID1', 'Tot', 'Valid', 'Pct', 'In'], axis=1)

# Concatenate funds and save to new file (to save resources)
frames = [fund8, fund9, fund10]
masterfile = pd.concat(frames, ignore_index=True)
masterfile.to_csv('fund_agg.csv')
~~~
