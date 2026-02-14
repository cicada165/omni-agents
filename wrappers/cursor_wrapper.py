from .base import AgentWrapper

class CursorWrapper(AgentWrapper):
    def execute(self, task):
        print(f"[{self.name}] opening context in IDE...")
        # Hypothetical usage: cursor --open "task"
        command = [self.command, "--open", task]
        print(f"[{self.name}] (Simulated) Running: {' '.join(command)}")
