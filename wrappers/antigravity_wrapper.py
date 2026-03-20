import subprocess
from .base import AgentWrapper

class AntigravityWrapper(AgentWrapper):
    def delegate(self, task):
        print(f"🚀 [AGENT] Delegating to Antigravity for HIGH VELOCITY execution...")
        return self._run_subprocess([self.command, task])
