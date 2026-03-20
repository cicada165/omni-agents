import subprocess
from .base import AgentWrapper

class CursorWrapper(AgentWrapper):
    def call(self, task):
        print(f"🛠️  [UTILITY] Opening {task} in Cursor IDE...")
        return self._run_subprocess([self.command, ".", task])
