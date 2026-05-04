
class ClassifierAgent:
    def classify(self, q):
        if "安全" in q:
            return "安全合规"
        elif "架构" in q:
            return "技术架构"
        return "功能特性"
