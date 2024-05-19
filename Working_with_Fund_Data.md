## Working with Fund Data
This section will demonstrate from simple examples to complex ones how past fund data can be collected, cleaned, aggregated and analyzed using the [Open Source Data Science Stack](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/OSDS.md) to yield insights. The basis for this is the Pandas Python library used for working with data sets that combines elements of Excel spreadsheet, the R language and SQL to offer an accessible framework that across our typical workload is more convenient or powerful than each of these tools on its own. Most importantly, it runs order of magnitude faster than an Excel worksheet would - which is the current format of presenting and analyzing Catalyst data for most users. Although Excel can be "forced" to perform statistical analysis as shown in John Foreman's excellent book [Data Smart](https://www.amazon.com/Data-Smart-Science-Transform-Information/dp/111866146X), it cannot do so without hogging resources and crashing if the datasets get too large.

### Fund-8 "CA/VCA Sheet"
[Zipped CSV File of Aggregated Community Reviews Raw Data Fund-8](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund8.zip)

### Fund-9 "CA/VCA Sheet"
[Zipped CSV File of Aggregated Community Reviews Raw Data Fund-9](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund9.zip)

### Fund-10 "CA/VCA Sheet"
[Zipped CSV File of Aggregated Community Reviews Raw Data Fund-10](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/fund10.zip)

### The Pandas DataFrame
Pandas is a powerful and flexible Python package designed for data manipulation and analysis. Created by Wes McKinney in 2008, Pandas has become an essential tool for data scientists and analysts due to its ability to handle diverse types of data and its rich functionality. McKinney, who at the time worked in quantitative finance at quant hedge fund AQR Capital Management, developed Pandas to address the need for a more efficient and state of the art tool for data analysis in Python. His motivation was to enable more streamlined data manipulation, allowing users to spend less time on data preparation and more on deriving insights. For analyzing datasets from Project Catalyst, where proposers submit proposals and community reviewers score them and write comments, Pandas offers several key features:

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
import pandas as pd

# Load data into a DataFrame
data = pd.read_csv('fundX.csv')

# Group by proposer and calculate the mean score for each proposer
mean_scores = data.groupby('proposer')['score'].mean()

# Group by reviewer and count the number of assessments each reviewer made
assessment_counts = data.groupby('reviewer')['assessments'].count()

# Display the results
print(mean_scores)
print(assessment_counts)
~~~

### Aggregation and Pandas Groupby Operations

### Plotting Data from our DataFrame

### Interactive IPython Notebook
