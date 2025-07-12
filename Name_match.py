from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

names = [
    "Geetha", "Gita", "Gitu", "Geeta", "Seetha", "Meeta", "Sunita", "Sita",
    "Rita", "Reeta", "Lalita", "Mamta", "Komal", "Kamal", "Kanta", "Anita",
    "Vinita", "Vanita", "Rachita", "Sarita", "Savita", "Nikita", "Namita",
    "Neeta", "Deepa", "Neelam", "Pushpa", "Preeti", "Poonam", "Radha"
]

model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight embedding model
name_embeddings = model.encode(names, convert_to_numpy=True)

# Create FAISS index
dim = name_embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(name_embeddings)

def get_similar_names(query, top_k=5):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)
    
    results = []
    for i, idx in enumerate(indices[0]):
        score = 100 - distances[0][i]  # Inverse L2 distance as score
        results.append((names[idx], round(score, 2)))
    
    return results
def generate_response(name_input):
    similar_names = get_similar_names(name_input)
    best = similar_names[0]
    
    response = f"The best match for '{name_input}' is **{best[0]}** with similarity score {best[1]}.\n"
    response += "Other similar names are:\n"
    for name, score in similar_names[1:]:
        response += f"- {name}: {score}\n"
    
    return response

print(generate_response("Geeta"))
