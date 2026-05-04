
import asyncio
from agents.classifier import ClassifierAgent
from agents.generator import GeneratorAgent
from agents.checker import CheckerAgent
from utils.file_parser import parse_file
from utils.excel_writer import write_excel

class Orchestrator:

    def __init__(self):
        self.classifier = ClassifierAgent()
        self.generator = GeneratorAgent()
        self.checker = CheckerAgent()

    async def process_one(self, q):
        category = self.classifier.classify(q)
        answer = await self.generator.generate(q, category)
        checked = self.checker.check(answer)

        return {
            "question": q,
            "category": category,
            "answer": checked
        }

    async def run(self, file):
        questions = parse_file(file)

        tasks = [self.process_one(q) for q in questions]
        results = await asyncio.gather(*tasks)

        output_file = write_excel(results)

        return {
            "results": results,
            "file": output_file
        }
