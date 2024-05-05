## The Open Source Data Science Ecosystem

>Sources: [Kaggle](https://www.kaggle.com/), [Github blog](https://github.blog/), [Anaconda blog](https://www.anaconda.com/blog?_topic=for-practitioners), [Open Data Science](https://odsc.medium.com/), [DataCamp](https://www.datacamp.com/blog/top-python-libraries-for-data-science), [Shopdev](https://shopdev.co/blog/python-libraries-for-data-science), [Simplilearn](https://www.simplilearn.com/top-python-libraries-for-data-science-article), [Knowledgehut](https://www.knowledgehut.com/blog/category/data-science), [Data Science Society](https://www.datasciencesociety.net/), [AI Business](https://aibusiness.com/data/ten-essential-data-science-packages-for-python), [DrivenData](https://drivendata.co/blog.html).

**[Python](https://www.python.org/)**’s ecosystem and communities offer the most accessible and broad open source data science entry point. It makes up for lack of performance (which is debatable but a common complaint) with powerful packages that leverage C. It is widely used in science and enterprise. With syntax that is very close to written English, it is popular for its readability and simplicity and is very often used in [IT books about Data Science](https://www.amazon.com/s?k=python+data+science) and arguably has the largest and most active open source community and support system, despite the enduring popularity of R, Go, Scala, Julia or Matlab in niche application or specialized fields. Over the last 15 years or so, the quantitative finance community has largely moved from C++ to Python for these reasons, especially among smaller players, academic publication or open source use.

### “The Big Four”
Some Python packages are so well established that they are de facto part of the “batteries included” scientific Python stack in most distributions. It is somewhat subjective to draw the line what is included in this definition. From our experience, **NumPy**, **Pandas**, **Matplotlib**, and **Jupyter Notebooks** are beyond doubt default data science packages and cannot be replaced wholesale by any other packages. Let’s take a quick look at their open source status, community and licenses.

* **[NumPy](https://numpy.org/)** is the package for numerical python in general and works much faster than pure Python because it has compiled C and C++ code under the hood, allowing large, multi-dimensional arrays, data vectorization and matrix algebra. Used by 2.2m on [Github](https://github.com/numpy/numpy) with 9.3k forks and 26.4k stars. Distributed under “a liberal BSD license”, NumPy is developed and maintained publicly on GitHub by a vibrant, responsive, and diverse community. In the context of Project Catalyst, larger datasets like Community Advisor / Reviewer scores across different funding amounts and categories could be presented as multidimensional and fit into machine learning or AI tools that take vectors or matrixes but not spreadsheets as inputs.

* **[Pandas](https://pandas.pydata.org/)** provides labeled data structures similar to R and spreadsheet - like data manipulation and statistical functions. This makes it ideal to import and export Excel-like tables. It began in 2008 inside quant hedge fund AQR Capital Management, by the end of 2009 it had been open sourced. Used by 1.6m on [Github](https://github.com/pandas-dev/pandas/) with 17.3k forks and 42k stars. Distributed under BSD-3-Clause license. Since 2015, pandas is a NumFOCUS sponsored project. This will help ensure the success of development of pandas as a “world-class open-source project”. For Catalyst, DataFrames would be an elegant alternative to Excel spreadsheets as the C-powered vectorization allows much faster data analysis, inbuilt plotting and direct access from other data science packages.
![Pandas Data Frame](https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1606929736/pandasdataframe_ihqxej.png)

* **[Matplotlib](https://matplotlib.org/)**: NumPy and Pandas both have data visualization functionality built in, but do not come near the capabilities of this essential library for any type of table, chart or diagram ranging from pretty to scientific. Used by 1.1m on [Github](https://github.com/matplotlib/matplotlib) with 7.4k forks and 19.3k stars. Matplotlib only uses BSD compatible code, and its license is based on the PSF license. As this covers graphs the most basic line charts ("number of proposals from Fund-7 to Fund-11") to complex 3-dimensional scatterplots (showing relationships between Reviewer Scores, funds requested and funds awarded for example) it is highly relevant to Catalyst.
![Matplotlib](https://matplotlib.org/stable/_images/users-project-history-2.2x.png)

* **[Jupyter Notebooks](https://jupyter.org/)**
Transcending the Python ecosystem, IPython notebooks have become a favorite for interactive code and contained showcases or tutorials. Code areas can be changed and executed by the user and allow inline plotting, charting or import of other packages. According to it's website "its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality. **Free software, open standards, and web services for interactive computing across all programming languages** "
Used by 279k on [Github](https://github.com/jupyter/notebook) with 4.6k forks and 11.2k stars. It is licensed under the terms of the 3-Clause BSD License also known as New or Revised or Modified BSD License, or the BSD-3-Clause license. Jupyter Notebooks have been used by IOG from its Haskell Course to Atala Prism Pioneer program and are a great way for anyone to present code-based application interactively and simply.
![Jupyter Notebooks](https://jupyter.org/assets/homepage/labpreview.webp)

### "The Next 12"
Chosen from the most used and most popular, but excluding complex Deep Learning, LLM and Machine Learning Optimization as our Catalyst datasets are likely small and we want to avoid black boxes when communicating data-driven insights to the wider community. Some packages that used to enjoy considerable popularity have been deprecated or neglected for others that are maintained by more active communities or seen are more suitable for the boom in generative AI. Theano and Chainer for deep learning are good examples.

Not all of these packages come pre-installed with all scientific Python distributions (such as [Anaconda](https://www.anaconda.com/)) but can normally be installed quite easily through package management. As the main Anaconda repository can be slow to add new releases, it can be preferable to use conda-forge such as:

`conda install seaborn -c conda-forge`

For those who prefer to install using the command line, we have provided the [pip](https://pypi.org/project/pip/) command in the listings below such as:

`pip install seaborn` 

or pip3 for Linux and WSL if working with Python 3 (as we do).

***

**1. [Seaborn](https://seaborn.pydata.org)**
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. It is particularly useful for making complex visualizations from data in pandas DataFrames. Seaborn arguably looks better and requires less code than Matplotlib, but lacks some cutomization features of its older sibling. When DataFrames are used instead of spreadsheets for Fund data, plotting with Seaborn would be particularly easy and attractive.

`Installation:`
~~~~
pip install seaborn
~~~~
Open Source Status: BSD-3-Clause license.

[Seaborn GitHub](https://github.com/mwaskom/seaborn)

`Example of a scatterplot:`

![Seaborn Plots](https://seaborn.pydata.org/_images/scatterplot_sizes.png)

***

**2. [SciKit Learn (SKL)](https://scikit-learn.org)**
Scikit-learn is a machine learning library for Python. It features various classification, regression, and clustering algorithms, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. For pure machine learning, this is the go-to workhorse that can easily benefit Catalyst by looking for clusters in data or understand relationships that go beyond spreadsheet (linear) regression but do not need or benefit from "emergent" AI treatment. k-nearest neighbors algorithm is a perfect example of where SKL shines.

`Installation:`
~~~~
pip install scikit-learn
~~~~
Open Source Status: BSD license.

[GitHub Page](https://github.com/scikit-learn/scikit-learn)

`Example of KNN visualization from SciKit Learn:`

![KNN](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_001.png)

***

**3. [TensorFlow](https://www.tensorflow.org)**
TensorFlow is an end-to-end open source platform for machine learning that works across platforms and programming languages. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML, and developers easily build and deploy ML-powered applications. For the multi-faceted Catalyst ecosystem with decentralized, community-powered apps and analytics, it can be used integrating various different sources and endpoints. It is somewhat more cutting-edge and heavyweight than "oldie-but-goldie" SKL. It was developed by the Google Brain team for Google's internal use in research and production. For Catalyst, if you have the right idea, TF is likely to be able to help. It can be used to develop models for various tasks including natural language processing, image recognition, similarity recognition, and different computational-based simulations covering unsupervised, supervised and black-box modelss.

`Installation:`
~~~~
pip install tensorflow
~~~~
Open Source Status: Apache 2.0 license.

[GitHub Page](https://github.com/tensorflow/tensorflow)

Example of TF flow from [Simplilearn](https://www.simplilearn.com/tutorials/deep-learning-tutorial/tensorflow-2):

![TensorFlow](https://www.simplilearn.com/ice9/free_resources_article_thumb/TensorFlow2.0Architecture.PNG)

***

**4. [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)**
BeautifulSoup is the classic webscraping package for Python data applications. This lets users define and run scraping "bots" to collect data anywhere accessible on the web, either static data as part of a larger scale (re)search operation, or the same data as it is updated periodically to keep track of change. In a decentralized ecosystem like Catalyst, this is extremely usesful as it can bypass APIs requirements or simply access data that is in their own silo or community while being highly relevant to the overall truth discovery (such as community governance projects and DAOs). It works by allowing parsing HTML and XML documents. It creates a parse tree for parsed web pages based on specific criteria that can be used to extract, navigate, search, and modify data from HTML.

`Installation:`
~~~~
pip install beautifulsoup4
~~~~
Open Source Status: MIT license.

Uses [Libraries.io](https://libraries.io/pypi/beautifulsoup4) instead of Github.

![Fun Image](https://proxyway.com/wp-content/uploads/2023/05/web-scraping-with-beautiful-soup.png)

***

**5. [Scrapy](https://scrapy.org/)**
Scrapy is a comprehensive web scraping framework, perfect for large-scale data extraction projects and offers built-in support for crawling, whereas Beautiful Soup is a parsing library best suited for smaller, more straightforward scraping tasks without the built-in crawling capabilities. Scrapy allows defining "Items", a data structure that holds the user's data. Instead of yielding scraped data in the form of a dictionary for example, it allows defining an Item schema beforehand in an items.py file and use this schema when scraping data. This enables quickly and easily checking what structured data are  being collected in the project, and will raise exceptions if incorrect data is used with the Item.

`Installation:`
~~~~
pip install Scrapy
~~~~
`Or ideally using Conda:`
~~~~
conda install -c conda-forge scrapy
~~~~

Open Source Status: BSD-3-Clause license.

[GitHub Page](https://github.com/scrapy/scrapy)

***

**6. [NLTK](http://www.nltk.org)**
Natural Language Toolkit (NLTK) is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in Python. It is the best known natural language processing tool and various books and tutorials exists how to use it. Needless to say, a lot of Project Catalyst data is text like CA/CR reviews, proposal bodies, Github readmes and so on so this package is crucial to convert text into numbers, which Machine Learning models can then easily work with. It is also powerful for sentiment analysis parsing Twitter/X posts. If text suddenly becomes numbers, a whole new universe of possibilities for analysis opens up. This makes NLTK one of the most useful packages - but this isn't trivial. Careful production planning from ideation over signal processing to dimensionality reduction need to be considered, making this a science onto itself. We will try to open up as much Catalyst text to analysis as possible, but expect the first steps to be quite basic before deeper insights can be gained from large datasets of free-form text such as the entirety of proposal reviews in one Fund.

`Installation:`
~~~~
pip install nltk
~~~~

Open Source Status: Apache 2.0 license.

GitHub Page: [NLTK GitHub](https://github.com/nltk/nltk)

`How NLTK works (DataCamp):`

![NLTK](https://images.datacamp.com/image/upload/v1679592730/text_preprocessing_steps_in_sequence_1bcfc50bd0.png)

***

7. **[Statsmodels](https://www.statsmodels.org)**

8. **[Keras](https://keras.io)**

9. **[PyTorch](https://pytorch.org)**

10. **[Gensim](https://radimrehurek.com/gensim/)**

11. **[Spacy](https://spacy.io)**

12. **[Plotly](https://plotly.com)**


### More experimental packages
A few more to experiment with “next level” applications. We have a separate section for AI, but for high level, statistical and prediction machine learning, there is a rich sophisticated, niche package ecosystem for any need and any task. Some areas however increasingly rely on expensive non-open source APIs like OpenAI's. If there is a need for a deeper dive as we come across more use cases and community requests, we may expand on this section.

1. [**LightGBM**](https://github.com/microsoft/LightGBM)

2. [**cadCAD**](https://github.com/cadCAD-org/cadCAD)
   
3. [**NetworkX**](https://github.com/networkx)

4. **[Gephi](https://gephi.org)**

5. [**LangChain**](https://github.com/LangChain/langchain)
