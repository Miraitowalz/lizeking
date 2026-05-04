
class CheckerAgent:
    def check(self, ans):
        if "100%" in ans:
            return "⚠️需人工确认:" + ans
        return ans
