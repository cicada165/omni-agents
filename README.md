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

3. **Configuration**:
   Copy `config.yaml` and update paths/arguments if your tools are in non-standard locations.
   
## Usage

```bash
python orchestrator.py --task "Your complex task here" --agent claude
```
