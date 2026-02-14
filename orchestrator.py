import argparse
import yaml
import sys
import os
from wrappers.base import AgentWrapper
from wrappers.claude_wrapper import ClaudeWrapper
from wrappers.codex_wrapper import CodexWrapper
from wrappers.gemini_wrapper import GeminiWrapper
from wrappers.cursor_wrapper import CursorWrapper
from wrappers.antigravity_wrapper import AntigravityWrapper

AGENT_CLASSES = {
    "claude": ClaudeWrapper,
    "codex": CodexWrapper,
    "gemini": GeminiWrapper,
    "cursor": CursorWrapper,
    "antigravity": AntigravityWrapper
}

def load_config(config_path="config.yaml"):
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Omni-Agents CLI")
    parser.add_argument("--task", type=str, required=True, help="The task description")
    parser.add_argument("--agent", type=str, help="Specific agent to use (overrides default)")
    parser.add_argument("--dry-run", action="store_true", help="Print command instead of executing")
    
    args = parser.parse_args()
    config = load_config()
    
    agent_name = args.agent or config["settings"].get("default_agent")
    
    if agent_name not in config["agents"]:
        print(f"Error: Agent '{agent_name}' not found in configuration.")
        sys.exit(1)
        
    agent_config = config["agents"][agent_name]
    if not agent_config.get("enabled", True):
        print(f"Error: Agent '{agent_name}' is disabled.")
        sys.exit(1)

    print(f"🚀 Starting Orchestrator with agent: {agent_name}")
    print(f"📋 Task: {args.task}")

    wrapper_class = AGENT_CLASSES.get(agent_name, AgentWrapper)
    wrapper = wrapper_class(agent_name, agent_config)
    
    if args.dry_run or config["settings"].get("dry_run", False):
        print(f"[DRY RUN] Mode enabled")
        # In dry run, we might just print what execute would do, but the wrappers currently check dry_run inside execute too.
        # We can pass a flag to execute or let the wrapper handle it from config.
        # For now, let's just call execute, as the wrappers simulate execution.
        wrapper.execute(args.task)
    else:
        wrapper.execute(args.task)

if __name__ == "__main__":
    main()
