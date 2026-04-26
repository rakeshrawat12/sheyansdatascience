from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# ============================
# Data Model
# ============================

class Item(BaseModel):
    metadata: str
    category: str
    embedding: list


# ============================
# Vector DB
# ============================

class VectorDB:
    def __init__(self):
        self.data = []
        self.id = 0

    def insert(self, item):
        self.data.append({
            "id": self.id,
            "metadata": item.metadata,
            "category": item.category,
            "embedding": item.embedding
        })
        self.id += 1

    def search(self, query_vec, k=3):
        results = []

        for item in self.data:
            emb = np.array(item["embedding"])
            sim = cosine_similarity([query_vec], [emb])[0][0]

            results.append({
                "id": item["id"],
                "metadata": item["metadata"],
                "category": item["category"],
                "distance": float(1 - sim)
            })

        results.sort(key=lambda x: x["distance"])
        return results[:k]


db = VectorDB()

# ============================
# Routes
# ============================

@app.get("/")
def home():
    return {"msg": "API running 🚀"}


@app.post("/insert")
def insert(item: Item):
    db.insert(item)
    return {"msg": "inserted"}


@app.get("/items")
def get_items():
    return db.data


@app.get("/search")
def search(v: str, k: int = 3, metric: str = "cosine", algo: str = "bruteforce"):
    vec = np.array([float(x) for x in v.split(",")])

    results = db.search(vec, k)

    return {
        "results": results,
        "latencyUs": 120  # dummy latency for UI
    }


@app.delete("/delete/{item_id}")
def delete(item_id: int):
    global db
    db.data = [x for x in db.data if x["id"] != item_id]
    return {"msg": "deleted"}