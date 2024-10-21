import os
import re
import sys
import psutil
from bs4 import BeautifulSoup
from docx import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^a-zA-Z0-9\s.,;:?!-]', '', text)
    return text

def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        return clean_text(text)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return ""

def extract_text_from_html(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
        return clean_text(text)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return ""

def process_file(file_path: str) -> List[Dict[str, str]]:
    print(f"Processing {file_path}...")
    if file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith('.html'):
        text = extract_text_from_html(file_path)
    else:
        print(f"Unsupported file type: {file_path}")
        return []

    if not text:
        print(f"No content extracted from {file_path}")
        return []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    return [{"content": chunk, "source": os.path.basename(file_path)} for chunk in chunks]

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    print(f"Current memory usage: {memory_usage}%")
    if memory_usage > 90:
        print("Warning: High memory usage. Consider closing other applications or increasing available memory.")
        return False
    return True

def main():
    data_directory = "./data"  # Update this to your data directory
    all_chunks = []
    total_files = 0
    processed_files = 0

    for filename in os.listdir(data_directory):
        if filename.endswith(('.docx', '.html')):
            total_files += 1

    print(f"Found {total_files} files to process.")

    for filename in os.listdir(data_directory):
        if filename.endswith(('.docx', '.html')):
            file_path = os.path.join(data_directory, filename)
            chunks = process_file(file_path)
            all_chunks.extend(chunks)
            processed_files += 1
            
            print(f"Processed {len(chunks)} chunks from {filename}")
            print(f"Progress: {processed_files}/{total_files} files")
            
            if not check_memory_usage():
                user_input = input("Do you want to continue processing? (y/n): ")
                if user_input.lower() != 'y':
                    print("Processing stopped by user.")
                    break

    print(f"\nProcessing complete. Total chunks: {len(all_chunks)}")
    print("\nSample of processed chunks:")
    for i, chunk in enumerate(all_chunks[:5]):
        print(f"\nChunk {i+1} from {chunk['source']}:")
        print(chunk['content'][:100] + "...")  # Print first 100 characters of each chunk

if __name__ == "__main__":
    main()
