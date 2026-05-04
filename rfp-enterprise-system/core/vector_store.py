
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:

    def __init__(self):
        self.docs = []
        self.vectorizer = TfidfVectorizer()

    def load(self):
        with open("data/knowledge.txt", encoding="utf-8") as f:
            self.docs = f.readlines()

    def search(self, q):
        if not self.docs:
            return ""
        vec = self.vectorizer.fit_transform(self.docs + [q])
        sim = cosine_similarity(vec[-1], vec[:-1])[0]
        idx = sim.argsort()[-3:]
        return " ".join([self.docs[i] for i in idx])
