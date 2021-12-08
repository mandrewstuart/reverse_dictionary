import faiss


index = None


def load_index():
    d = 512
    global index
    index = faiss.IndexFlatL2(d)


def add_vectors(vectors):
    global index
    index.add(vectors)
    return index