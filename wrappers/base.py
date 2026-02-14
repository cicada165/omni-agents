class AgentWrapper:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.command = config.get("command", name)

    def execute(self, task):
        """
        Executes the task using the agent's CLI tool.
        This method should be overridden by specific agent wrappers if they have custom arguments.
        """
        print(f"[{self.name}] Executing task: {task}")
        # Implementation of subprocess call will go here
        # import subprocess
        # subprocess.run([self.command, ...])
