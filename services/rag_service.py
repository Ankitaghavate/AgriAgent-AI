import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter


class RAGService:
    def __init__(self):
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.documents = []
        self.index_path = "faiss_index.pkl"

    def build_index(self, file_path="knowledge_base/schemes.txt"):
        print("Building FAISS index...")

        # Read knowledge base
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        chunks = splitter.split_text(text)

        self.documents = chunks

        # Generate embeddings
        embeddings = self.embedding_model.encode(chunks)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        # Save index
        with open(self.index_path, "wb") as f:
            pickle.dump((self.index, self.documents), f)

        print("FAISS index built and saved.")

    def load_index(self):
        if not os.path.exists(self.index_path):
            raise Exception("Index not found. Run build_index() first.")

        with open(self.index_path, "rb") as f:
            self.index, self.documents = pickle.load(f)

        print("FAISS index loaded successfully.")

    def retrieve(self, query, top_k=3):
        query_embedding = self.embedding_model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)

        results = [self.documents[i] for i in indices[0]]
        return results
