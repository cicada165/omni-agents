class AgentWrapper:
    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.command = config.get("command", name)
        self.category = config.get("category", "utility")
        # Leaked-code inspired attributes:
        self.is_destructive = config.get("is_destructive", False)
        self.requires_permission = config.get("requires_permission", False)
        self.search_hint = config.get("search_hint", "Agent tool for executing generic tasks.")

    def execute(self, task, context=None):
        """Main entry point for tool execution with optional context."""
        if self.category == "agent":
            return self.delegate(task, context)
        else:
            return self.call(task, context)

    def delegate(self, task, context=None):
        """Handle execution for autonomous agents (interactive/loops)."""
        print(f"🤖 [AGENT] Delegating task to {self.name}...")
        return self._run_subprocess([self.command, task], context)

    def call(self, task, context=None):
        """Handle execution for stateless utilities (API wrappers/CLI)."""
        print(f"🛠️  [UTILITY] Calling {self.name}...")
        return self._run_subprocess([self.command, task], context)

    def _run_subprocess(self, command, context=None):
        """Common subprocess runner with permission and destructive checks."""
        import subprocess
        
        # Check if tool requires manual approval
        if (self.is_destructive or self.requires_permission) and not self.config.get("auto_approve", False):
            print(f"⚠️  [PERMISSION] Tool '{self.name}' is {'destructive' if self.is_destructive else 'sensitive'}.")
            confirm = input(f"   Confirm execution of command: {' '.join(command)}? (y/N): ")
            if confirm.lower() != 'y':
                print(f"🛑 [ABORTED] {self.name} execution cancelled.")
                return

        if self.config.get("dry_run", False):
            print(f"[{self.name}] Dry run: {' '.join(command)}")
            return
            
        try:
            print(f"[{self.name}] Executing: {' '.join(command)}")
            # Future-proofing: Inject context if the command supports it (e.g. via env vars)
            env = None
            if context:
                import os
                env = os.environ.copy()
                env.update({f"OMNI_{k.upper()}": str(v) for k, v in context.items()})
            
            subprocess.run(command, check=True, env=env)
        except Exception as e:
            print(f"[{self.name}] Error: {e}")

