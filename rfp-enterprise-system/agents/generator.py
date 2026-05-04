
from llm.llm import call_llm
from core.vector_store import VectorStore

class GeneratorAgent:

    def __init__(self):
        self.store = VectorStore()
        self.store.load()

    async def generate(self, q, category):
        context = self.store.search(q)
        prompt = f"问题:{q}\n分类:{category}\n知识:{context}\n请生成专业回答"
        return call_llm(prompt)
