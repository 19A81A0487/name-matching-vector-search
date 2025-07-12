import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

names = [
    "Geetha", "Gita", "Gitu", "Geeta", "Githa", "Geetanjali", "Githika", "Gitali", "Gitisha",
    "Anita", "Sunita", "Rita", "Sita", "Meeta", "Lalita", "Nita", "Savita", "Babita", "Sarita",
    "Aarathi", "Arathi", "Parvati", "Bhavani", "Haritha", "Deepa", "Devika", "Kavita", "Jyothi",
    "Swathi", "Divya", "Kiran", "Rekha", "Neeta", "Mamatha", "Yamuna"
]

model = SentenceTransformer('all-MiniLM-L6-v2')
name_embeddings = model.encode(names, convert_to_tensor=False)
embedding_dim = name_embeddings[0].shape[0]
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(name_embeddings))

st.title("🔍 Name Matching System")
input_name = st.text_input("Enter a name to search for similar ones:")

if input_name:
    input_embedding = model.encode([input_name])[0]
    input_embedding = np.array([input_embedding])
    distances, indices = index.search(input_embedding, 5)
    
    st.subheader("✅ Best Match")
    best_match = names[indices[0][0]]
    best_score = 1 - distances[0][0]
    st.write(f"**{best_match}** (Score: {best_score:.4f})")

    st.subheader("📋 Top Similar Names")
    for idx, dist in zip(indices[0], distances[0]):
        name = names[idx]
        score = 1 - dist
        st.write(f"{name} - Score: {score:.4f}")
