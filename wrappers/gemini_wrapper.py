import subprocess
from .base import AgentWrapper

class GeminiWrapper(AgentWrapper):
    def delegate(self, task):
        print(f"🤖 [AGENT] Delegating to Gemini for Deep Research...")
        return self._run_subprocess([self.command, task])
