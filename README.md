# Omni-Agents (formerly Agent Orchestrator)

A system for orchestrating multiple CLI-based AI agents to accomplish complex tasks. This project integrates tools like Claude Code, Codex CLI, Gemini CLI, Cursor Hub, and Antigravity into a unified workflow.

## Overview

The Agent Orchestrator allows you to:
- Define complex tasks that require multiple specialized agents.
- Route sub-tasks or entire objectives to the most suitable CLI tool.
- Manage configuration and context across different agent executions.

## Supported Agents

- **Claude Code** (`claude`): Deep reasoning and architectural planning.
- **Codex CLI** (`codex`): Autonomous terminal operations and DevOps.
- **Gemini CLI** (`gemini`): Large context research and prototyping.
- **Cursor Hub** (`cursor`): IDE integration and diff viewing.
- **Antigravity** (`antigravity`): High-velocity prototype mode.

## Setup

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation**:
   Ensure you have the required CLI tools installed (`claude`, `codex`, `gemini`, `cursor`, `antigravity`). You can check your environment with:
   ```bash
   python check_setup.py
   ```

3. **Configure API Keys**:
   - For **Codex**, you need an OpenAI API Key.
   - Create a `.env` file from the example:
     ```bash
     cp .env.example .env
     ```
   - Obtain your key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
   - Paste the key into your `.env` file.

3. **Configuration**:
   Copy `config.yaml` and update paths/arguments if your tools are in non-standard locations.

## Architecture: Agents vs Utilities

Omni-Agents distinguishes between two types of tools:

1.  **AGENT**: Autonomous workers with their own execution loops and toolsets (e.g., Claude Code, Codex). When you use an agent, Omni-Agents **delegates** the task and lets the agent take over the TUI.
2.  **UTILITY**: Stateless API wrappers or CLI tools (e.g., Cursor, GitHub CLI). When you use a utility, Omni-Agents **calls** the tool to perform a specific action.

## Usage

```bash
# Delegate to an Agent
python orchestrator.py --task "Architect a new microservice" --agent claude-pro

# Call a Utility
python orchestrator.py --task "index.py" --agent cursor
```
