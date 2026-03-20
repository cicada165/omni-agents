class AgentWrapper:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.command = config.get("command", name)
        self.category = config.get("category", "utility")

    def execute(self, task):
        """Main entry point for tool execution."""
        if self.category == "agent":
            return self.delegate(task)
        else:
            return self.call(task)

    def delegate(self, task):
        """Handle execution for autonomous agents (interactive/loops)."""
        print(f"🤖 [AGENT] Delegating task to {self.name}...")
        return self._run_subprocess([self.command, task])

    def call(self, task):
        """Handle execution for stateless utilities (API wrappers/CLI)."""
        print(f"🛠️  [UTILITY] Calling {self.name}...")
        return self._run_subprocess([self.command, task])

    def _run_subprocess(self, command):
        """Common subprocess runner."""
        import subprocess
        if self.config.get("dry_run", False):
            print(f"[{self.name}] Dry run: {' '.join(command)}")
            return
            
        try:
            print(f"[{self.name}] Executing: {' '.join(command)}")
            subprocess.run(command, check=True)
        except Exception as e:
            print(f"[{self.name}] Error: {e}")
