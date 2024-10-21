import json
import os
from typing import List, Dict
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

def save_chunks_to_file(chunks: List[Dict[str, str]], output_file: str):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Chunks saved to {output_file}")

def load_chunks_from_file(input_file: str) -> List[Dict[str, str]]:
    with open(input_file, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    print(f"Loaded {len(chunks)} chunks from {input_file}")
    return chunks

def create_embeddings(chunks: List[Dict[str, str]], model_name: str = 'all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    texts = [chunk['content'] for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings

def store_in_faiss(embeddings: np.ndarray, output_file: str):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, output_file)
    print(f"FAISS index saved to {output_file}")

def main():
    chunks_file = "processed_chunks.json"
    faiss_index_file = "faiss_index.bin"
    
    # Check if chunks file already exists
    if os.path.exists(chunks_file):
        chunks = load_chunks_from_file(chunks_file)
    else:
        # If not, assume we're working with the chunks from the previous script
        # You might need to modify this part if you're running this as a separate script
        chunks = all_chunks  # This should be the variable from the previous script
        save_chunks_to_file(chunks, chunks_file)
    
    print("Creating embeddings...")
    embeddings = create_embeddings(chunks)
    
    print("Storing embeddings in FAISS...")
    store_in_faiss(embeddings, faiss_index_file)
    
    print("Processing complete!")
    print(f"Chunks are saved in: {chunks_file}")
    print(f"FAISS index is saved in: {faiss_index_file}")

if __name__ == "__main__":
    main()
