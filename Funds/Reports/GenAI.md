## **Section 1: Integrating Generative AI and Unsupervised Learning for Project Catalyst Insights**

Generative AI and unsupervised learning are transformative technologies that offer significant advantages in analyzing complex datasets and generating insights across various domains. These methodologies are particularly effective in identifying underlying patterns, simulating potential outcomes, and automating content generation, which are essential for advanced data-driven decision-making processes. In this section, we focus on the theoretical foundations, which areas have promise for Project Catalyst from a governance and rule-making perspective, and how advances in generative AI can benefit the ecosystem as a whole, covering a Chatbot-type LLM deployment to improve onboarding experiences, to post-funding assistance and general data queries that may benefit a wide range of stakeholders like voters and their dReps, proposing developers and enterprises, community support functions like reviews and moderation, to improved milestone, performance and track record management. Another area we will cover briefly is the identification and mitigation of malicious actors taking advantage of AI - the other side of the same coin where score manipulation, reward skimming and other adversarial behavior can be mitigated.

### **Applications in Research**
- **Pattern Recognition and Anomaly Detection**: Unsupervised learning algorithms like clustering and principal component analysis (PCA) are instrumental in identifying unusual patterns or anomalies in data without prior labeling. This is crucial for detecting fraudulent activities or duplicated content in large datasets.
- **Predictive Analytics and Simulation**: Generative AI can simulate various scenarios based on historical data, providing foresight into potential future outcomes. This is particularly useful in strategic planning, such as anticipating the effects of policy changes or new regulations on proposal submissions and funding distributions.
- **Automated Content Generation**: Generative models can be trained to produce textual content that mimics human writing, which can be used to generate reports, summaries, or even draft proposals based on a set dataset, reducing manual effort and increasing efficiency.

### **Benefits**
- **Efficiency and Scalability**: Automating the extraction of insights and generation of content with these technologies significantly speeds up research processes and allows for scaling analysis to larger datasets.
- **Depth of Insight**: These methods can delve deeper into data, uncovering complex relationships and patterns that might not be evident through manual analysis.
- **Adaptability**: Both generative AI and unsupervised learning can be adapted and fine-tuned to specific needs of different research domains, providing customized solutions that enhance the accuracy and relevance of the research outcomes.

### **Challenges**
- **Data Quality and Preparation**: The effectiveness of both generative AI and unsupervised learning heavily depends on the quality and granularity of the data. Poor data quality can lead to misleading insights and ineffective outcomes.
- **Interpretability**: Models, especially in unsupervised learning, often suffer from a lack of interpretability, which can make it difficult to trust or understand their decisions and outputs.
- **Ethical and Security Concerns**: There's a potential risk of misuse of generative AI, particularly in creating misleading or false information. Additionally, ensuring the security and privacy of data used in these models is paramount to prevent breaches and unauthorized access.

### **Strategic Integration Recommendations**

- **Robust Data Governance**: Implementing strict data quality controls and governance to ensure the data used is accurate, comprehensive, and secure.
- **Model Transparency and Validation**: Developing methods to increase the transparency of the models and routinely validating them against new data to ensure their continued accuracy and reliability.
- **Ethical Guidelines and Usage Protocols**: Establishing ethical guidelines and usage protocols for the deployment of generative AI to safeguard against its potential misuse and to ensure it aligns with organizational and societal norms.

The integration of generative AI and unsupervised learning provides a powerful toolkit for enhancing the breadth and depth of research across various domains. By addressing the associated challenges and strategically leveraging their capabilities, these technologies can significantly contribute to more informed decision-making and innovative solutions in research.

Unsupervised learning is a branch of **machine learning** where the model learns patterns from **unlabeled data**. Unlike supervised learning (where you know the correct output), unsupervised learning works on data where you don’t have labels or explicit outcomes to predict.

#### **How it Works**:
- **Goal**: The model tries to identify hidden structures or patterns in the data without any predefined labels.
- **Examples of Unsupervised Learning Techniques**:
  - **Clustering**: Grouping data points into clusters based on similarity (e.g., K-means clustering, hierarchical clustering).
  - **Dimensionality Reduction**: Reducing the number of features while preserving the most important information (e.g., PCA – Principal Component Analysis).
  - **Anomaly Detection**: Identifying unusual patterns or outliers that don’t fit into the normal data.

#### **Real-World Use Case**:
- **Customer Segmentation**: In marketing, unsupervised learning can help identify different customer groups based on their behavior, without knowing what the customer groups are in advance.

---

Generative AI refers to models that can generate new data that is similar to the data they were trained on. It’s part of a broader category called **generative models**, which learn the distribution of the data and can then generate new data points from that distribution.

#### **How it Works**:
- **Goal**: To create or "generate" new data based on the training data.
- **Examples of Generative AI Models**:
  - **Generative Adversarial Networks (GANs)**: Two neural networks, a generator and a discriminator, work together to create realistic data, such as images or videos.
  - **Variational Autoencoders (VAEs)**: A type of neural network that learns to compress data and then generate new data from that compressed representation.
  - **Transformer Models (GPT, BERT, etc.)**: These models, especially in language, are used to generate text, images, or even music.

#### **Real-World Use Case**:
- **Text Generation**: Models like GPT-3 can generate human-like text based on a prompt. This can be used to write articles, answer questions, or even generate creative content.

#### **Key Point**:
- **Generative AI** focuses on creating new, synthetic data that mimics the real data, often used in text, image, and video generation.

---

Large Language Models (LLMs) are a specific application of **Generative AI** that focus on processing and generating natural language. LLMs, such as **GPT-3**, are based on **transformer architecture** and are trained on vast amounts of text data to understand and generate human language.

#### **How it Works**:
- **Training**: LLMs are trained on enormous datasets of text (from books, websites, articles) using a **transformer** architecture, which allows them to understand the context and relationships between words over long sequences.
- **Goal**: To generate meaningful text based on a given prompt, answer questions, or even carry on a conversation.
  
#### **Real-World Use Case**:
- **Chatbots**: LLMs like **GPT-3** power chatbots that can understand and respond to user queries in a conversational manner.
- **Content Generation**: LLMs are used to generate blog posts, summarize articles, and create conversational agents.

---

### **Relationship Between LLMs, Generative AI, and Unsupervised Learning**

#### **How They Are Related**:
1. **Generative AI**: This is the broad category that includes models designed to generate new data, such as text, images, or even sound.
   - **LLMs** (like GPT-3) are a **specific subset of Generative AI** focused on language generation.
  
2. **Unsupervised Learning**: This is a type of learning where the model tries to find patterns in data without labeled outcomes.
   - **LLMs** and **Generative AI** can be trained using **unsupervised learning**, especially in pre-training phases. For instance, when training GPT models, the model reads and learns patterns from large corpora of text without explicit labels (i.e., unsupervised learning).

#### **How They Differ**:
- **LLMs**: Focus specifically on language and text generation.
- **Generative AI**: Can be applied to various types of data (text, images, sound, etc.) and includes models like GANs, VAEs, and transformer-based models like GPT.
- **Unsupervised Learning**: Is more general and can apply to any dataset, aiming to uncover patterns without labels. It can be used as part of the training process for generative models but also has broader applications (e.g., clustering).

#### **Visual Example**:
| **Technology**          | **Focus**                 | **Methodology**                            | **Examples**                         |
|-------------------------|---------------------------|--------------------------------------------|--------------------------------------|
| **Unsupervised Learning**| Discovering hidden patterns in data | Clustering, Dimensionality Reduction      | K-means, PCA               |
| **Generative AI**        | Generating new data       | Neural Networks (GANs, VAEs, Transformers) | GPT, BERT, GANs                     |
| **LLMs**                 | Language understanding and generation | Transformer models (trained on text)      | GPT-3, BERT              |

---

- **LLMs (Generative AI for Text)**: generate alternate or improved versions of proposals, reviewer rationales, or even reports. This can help identify inconsistencies, automate content creation, and suggest improvements.
  
- **Unsupervised Learning for Data Clustering**:  group similar proposals together or identify trends in past successes and failures without requiring labels. It’s particularly useful for tasks like detecting anomalies or common patterns among successful proposals.

- **Generative AI** and **Unsupervised Learning** are broad and powerful concepts that overlap, especially in modern machine learning applications like **LLMs**.
- **LLMs** are a subset of **Generative AI** and focus on generating language and understanding context in text-based tasks.
- **Unsupervised Learning** helps in discovering patterns from unlabelled data and can be used alongside or within generative models to extract insights without prior knowledge of the data's structure.

Integrate generative AI and unsupervised learning into our current Python script for detecting cloned proposals

### Current Approach:
Our existing script uses **TF-IDF** and **cosine similarity** to detect cloned proposals by measuring the textual similarity between them. This is a solid foundation using unsupervised learning for proposal comparison.

### Enhancing with Generative AI:
To integrate **Generative AI**, we could build upon script in the following ways:

1. **Variational Autoencoder (VAE)** or **Generative Adversarial Network (GAN)**:
   - You could use a VAE or a GAN to generate synthetic proposals based on the features learned from the existing dataset. This will help you analyze if certain proposals are too close to artificially generated ones, indicating a lack of originality.
   
   - For example, you can train a VAE to generate text embeddings of proposals, and compare existing proposals against these generated examples. Proposals that are too close to the generated versions may indicate cloning.

2. **Anomaly Detection**:
   - By training a VAE to learn the normal patterns in proposal data, you can use it to detect anomalies. Proposals that significantly deviate from the generated proposal patterns (or fall within highly similar generated patterns) may be flagged as cloned or suspicious.

3. **Advanced Clustering**:
   - You could combine generative AI with clustering techniques (such as **DBSCAN** or **K-Means**) to group proposals based on their learned embeddings. Proposals within the same cluster may be more likely to be duplicates or clones.


### Suggested Generative AI and Unsupervised Learning

#### Generative AI Integration for Clone Detection
After identifying potential clones through TF-IDF and cosine similarity, we integrated **generative AI** techniques to enhance our analysis. A **Variational Autoencoder (VAE)** was trained on the proposal text to generate synthetic proposals. These generated proposals allowed us to:
   - **Compare originality**: By comparing real proposals to the generated ones, we were able to identify proposals that closely mirrored the generated samples, suggesting potential cloning.
   - **Detect anomalies**: Using the latent space representation from the VAE, we identified anomalies or unusual patterns in proposal similarities that further indicated cloning.

#### Unsupervised Learning Clustering
We then applied unsupervised learning techniques to group similar proposals into clusters. Using **DBSCAN** on the VAE-generated embeddings allowed us to detect clusters of proposals that were nearly identical. Proposals within these clusters were flagged for further manual review.

***

## Section 2: Getting Started with Simple, Private LLM on local Machine

Here, we have two favorites among the multitude of options in a dynamic and fast-evolving space. First, we cover **OpenWebUI** that allows a secure setup on an "airgapped"/offline local machine like our own laptop with a fully downloaded, minimum viable LLM and Catalyst training data. Second, we look at the Meta provided "open source" **Llama** family - this is a wildly popular if not entirely uncontroversial choice that comes closest to proprietary heavy-weights like ChatGPT, Gemini or Claude.

## Step 1: Download and Install Docker

Download and install Docker from: https://docs.docker.com/desktop/install/windows-install/

*What Could Go Wrong?*

Docker runs on Windows, but performance and compatibility are better when using "Windows Subsystem for Linux" (WSL). Therefore, you should install WSL before installing Docker. (Recommendation: Select Ubuntu and use the same username and password as in Windows, then configure automatic login to WSL when logging into Windows.)

WSL installation guide: [https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)

**Open source alternatives:**
- Instead of Docker: Kubernetes or Singularity
- Instead of Windows + WSL: Ubuntu Linux

## Step 2: Download Container with Ollama and Open WebUI

Enter "cmd" in the Windows search bar (bottom left) to open the Command Prompt. Enter one of these commands:

### For Systems with NVIDIA Graphics Card:
```bash
docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

### For Systems without NVIDIA Graphics Card:
```bash
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

This will result in the following Docker progress if working correctly:
![DockerDesktop](https://github.com/Sapient-Predictive-Analytics/Data-Driven_Catalyst/blob/main/Funds/Reports/image001.png)

Both commands will download and install the appropriate container with the correct settings.

After installation, you can start WebUI by either:
- Clicking the blue "3000:8080" under Port(s) in Docker
- Entering this address in your browser: http://localhost:3000

The Open WebUI interface should then appear in your browser.

*What Could Go Wrong?*

If you encounter an error message, either:
- The container in Docker hasn't started yet (click the "play" button next to the Docker container)
- You need to install and start Windows WSL first

## Step 3: Set Up WebUI

You'll need to create an account in WebUI first. All account information is stored locally. The first account automatically becomes the administrator. Additional accounts are users whose permissions can be managed by the admin.

## Step 4: Download Models

1. Click on your account (bottom left in WebUI)
2. Click on "Admin Panel"
3. Click on "Settings" at the top of the Admin Panel
4. Click on "Models" under Settings
5. Enter one of the following German-capable models in "Pull a model from Ollama.com". Download times vary as models range from 3 to 9 GB.

### Llama Family Models (trained by Meta/Facebook)
- Large and powerful: `llama3.1:8b-instruct-q8_0`
- Medium size, still good: `llama3.1:8b-instruct-q6_K`
- Small and fast: `llama3.2:3b-text-q8_0`

### Qwen Family Models (trained by Alibaba)
- Large and powerful: `qwen2.5:7b-instruct-q8_0`
- Medium size, still good: `qwen2.5:7b-instruct-q6_K`
- Small and fast: `qwen2.5:3b-instruct-q8_0`

### Gemma Family Models (trained by Google)
- Large and powerful: `gemma2:9b-instruct-q8_0`
- Medium size, still good: `gemma2:9b-instruct-q5_K_M`
- Small and fast: `gemma2:2b-text-q8_0`

### Phi Family Models (trained by Microsoft)
- Small and fast: `phi3.5:3.8b-mini-instruct-q8_0`

For example, `phi3.5:3.8b-mini-instruct-q8_0` runs very smoothly. The "large and powerful" models also work but require longer response times. However, they provide better quality responses. If even the small models run too slowly, you can opt for even smaller ones. You can find the complete model catalog here:

[Ollama Library](https://ollama.com/library)

Note: If you plan to use these models commercially, review the licenses first. Most have very liberal license terms that include free commercial use.

For answers to frequently asked questions (e.g., what data is stored where), visit: https://docs.openwebui.com/faq/

*Happy chatting!* 🚀


## Llama with Langchain

~~~
conda install langchain langchain_community langchain_chroma -c conda-forge
pip install llama-toolchain
llama download --source meta --model-id Meta-Llama3.1-8B
conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia
jupyter notebook
~~~

The user can obtain a free license from [Meta](https://www.llama.com/llama-downloads). Paste Meta Llama customer URL when prompted and allow entire download to finish. Opinions vary a lot and new models are released often, so this is evolving fast. It is highly recommended to choose a relatively fast model if the purpose is to focus on a very narrow area of expertise like Cardano and Project Catalyst where responsiveness to queries is more important than conversational prowess or reasoning skills at the expense of learning and chatting without delays.

***

## Section 3: How to process Cardano & Catalyst data for AI and LLMs

Creativity is key in how to obtain the necessary amounts of data that are required to train a local generative AI or unsupervised learning system. We are currently experimenting with the official Project Catalyst Documentation, voting result PDF booklets, the Cardano Forum and export of official and large community Telegram chat history as reliable data sources, but much more data obviously exists - just think about the vastness of content creation and Catalyst Ecosystem funded proposals of past funds. This sounds overwhelming, but it is a good thing - the more data, the better any AI assistant is likely to perform.

### Cleaning the data as key

Before assigning any weights or providing context, we need a large amount of qualified data "chunks" ideally with emoticons, pictures removed and stripped down to the machine-understandable word tokens. In this Github repository several sample scripts can be found to showcase how this may look like, and below are a few helper functions in Python to make use of our OSDS libraries to make the available data as useful to your model as possible.

The functions are self-explanatory, one of the big advantages of using Python for this.

~~~
def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return clean_text(text)

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Extract only the text content
        text = soup.get_text(separator=' ', strip=True)
    return clean_text(text)

def process_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        elif filename.endswith('.html'):
            text = extract_text_from_html(file_path)
        else:
            continue
        documents.append(text)
    return documents

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_documents(documents)
    return texts
~~~
