from .base import AgentWrapper
import subprocess
from .base import AgentWrapper

class ClaudeWrapper(AgentWrapper):
    def delegate(self, task):
        mode_desc = "Claude Pro" if "pro" in self.name else "Claude Bedrock (Tunnel)"
        print(f"🤖 [AGENT] Delegating to {mode_desc} for architectural planning...")
        return self._run_subprocess([self.command, task])
