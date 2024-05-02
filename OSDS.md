## The Open Source Data Science Ecosystem
***
>Sources: [Kaggle](https://www.kaggle.com/), [Github blog](https://github.blog/), [Anaconda blog](https://www.anaconda.com/blog?_topic=for-practitioners), [Open Data Science](https://odsc.medium.com/), [DataCamp](https://www.datacamp.com/blog/top-python-libraries-for-data-science), [Shopdev](https://shopdev.co/blog/python-libraries-for-data-science), [Simplilearn](https://www.simplilearn.com/top-python-libraries-for-data-science-article), [Knowledgehut](https://www.knowledgehut.com/blog/category/data-science), [Data Science Society](https://www.datasciencesociety.net/), [AI Business](https://aibusiness.com/data/ten-essential-data-science-packages-for-python), [DrivenData](https://drivendata.co/blog.html).
***

**[Python](https://www.python.org/)**’s ecosystem and communities offer the most accessible and broad open source data science entry point. It makes up for lack of performance (which is debatable but a common complaint) with powerful packages that leverage C. It is widely used in science and enterprise. With syntax that is very close to written English, it is popular for its readability and simplicity and is very often used in [IT books about Data Science](https://www.amazon.com/s?k=python+data+science) and arguably has the largest and most active open source community and support system, despite the enduring popularity of R, Go, Scala, Julia or Matlab in niche application or specialized fields. Over the last 15 years or so, the quantitative finance community has largely moved from C++ to Python for these reasons, especially among smaller players, academic publication or open source use.

### “The Big Four”
Some Python packages are so well established that they are de facto part of the “batteries included” scientific Python stack in most distributions. It is somewhat subjective to draw the line what is included in this definition. From our experience, **NumPy**, **Pandas**, **Matplotlib**, and **Jupyter Notebooks** are beyond doubt default data science packages and cannot be replaced wholesale by any other packages. Let’s take a quick look at their open source status, community and licenses.

* **[NumPy](https://numpy.org/)** is the package for numerical python in general and works much faster than pure Python because it has compiled C and C++ code under the hood, allowing large, multi-dimensional arrays, data vectorization and matrix algebra. Used by 2.2m on [Github](https://github.com/numpy/numpy) with 9.3k forks and 26.4k stars. Distributed under “a liberal BSD license”, NumPy is developed and maintained publicly on GitHub by a vibrant, responsive, and diverse community.

* **[Pandas](https://pandas.pydata.org/)** provides labeled data structures similar to R and spreadsheet - like data manipulation and statistical functions. This makes it ideal to import and export Excel-like tables. It began in 2008 inside quant hedge fund AQR Capital Management, by the end of 2009 it had been open sourced. Used by 1.6m on [Github](https://github.com/pandas-dev/pandas/) with 17.3k forks and 42k stars. Distributed under BSD-3-Clause license. Since 2015, pandas is a NumFOCUS sponsored project. This will help ensure the success of development of pandas as a “world-class open-source project”.
![Pandas Data Frame](https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1606929736/pandasdataframe_ihqxej.png)

* **[Matplotlib](https://matplotlib.org/)**: NumPy and Pandas both have data visualization functionality built in, but do not come near the capabilities of this essential library for any type of table, chart or diagram ranging from pretty to scientific. Used by 1.1m on [Github](https://github.com/matplotlib/matplotlib) with 7.4k forks and 19.3k stars. Matplotlib only uses BSD compatible code, and its license is based on the PSF license. 
![Matplotlib](https://matplotlib.org/stable/_images/users-project-history-2.2x.png)

* **Jupyter Notebooks**
Transcending the Python ecosystem, IPython notebooks have become a favorite for interactive code and contained showcases or tutorials. Code areas can be changed and executed by the user and allow inline plotting, charting or import of other packages. According to it's website "its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality. **Free software, open standards, and web services for interactive computing across all programming languages** "
Used by 279k on [Github](https://github.com/jupyter/notebook) with 4.6k forks and 11.2k stars. It is licensed under the terms of the 3-Clause BSD License also known as New or Revised or Modified BSD License, or the BSD-3-Clause license.
![Jupyter Notebooks](https://jupyter.org/assets/homepage/labpreview.webp)

### "The Next 12"
Chosen from the most used and most popular, but excluding complex Deep Learning, LLM and Machine Learning Optimization as our Catalyst datasets are likely small and we want to avoid black boxes when communicating data-driven insights to the wider community. Some packages that used to enjoy considerable popularity have been deprecated or neglected for others that are maintained by more active communities or seen are more suitable for the boom in generative AI. Theano and Chainer for deep learning are good examples.

* **[Seaborn](https://seaborn.pydata.org)**
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. It is particularly useful for making complex visualizations from data in pandas DataFrames.

`Installation:`
~~~~
pip install seaborn
~~~~
Open Source Status: Open source, BSD-3-Clause license.
GitHub Page: [Seaborn GitHub](https://github.com/mwaskom/seaborn)
![Seaborn Plots](https://seaborn.pydata.org/_images/scatterplot_sizes.png)

* **[SciKit Learn (SKL)](https://scikit-learn.org)**

* **[TensorFlow](https://www.tensorflow.org)**

* **[Statsmodels](https://www.statsmodels.org)**

* **[Keras](https://keras.io)**

* **[PyTorch](https://pytorch.org)**

* **[NLTK](http://www.nltk.org)**

* **[BeautifulSoup](https://pypi.org/project/beautifulsoup4/)**

* **[Gensim](https://radimrehurek.com/gensim/)**

* **[Spacy](https://spacy.io)**

* **[Plotly](https://plotly.com)**

* **[Gephi](https://gephi.org)**
