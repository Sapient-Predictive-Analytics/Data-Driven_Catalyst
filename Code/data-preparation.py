import os
import re
from bs4 import BeautifulSoup
from docx import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

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

# Main execution
if __name__ == "__main__":
    data_directory = "./data"  # Update this to your data directory
    documents = process_documents(data_directory)
    texts = split_documents(documents)
    print(f"Processed {len(documents)} documents into {len(texts)} text chunks.")
