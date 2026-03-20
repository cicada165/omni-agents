import subprocess
from .base import AgentWrapper

class CodexWrapper(AgentWrapper):
    def delegate(self, task):
        print(f"🤖 [AGENT] Delegating to Codex for DevOps/Terminal execution...")
        return self._run_subprocess([self.command, task])
