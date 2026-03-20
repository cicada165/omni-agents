import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch, MagicMock

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wrappers.base import AgentWrapper
from wrappers.claude_wrapper import ClaudeWrapper
from orchestrator import load_config, AGENT_CLASSES

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.config = {
            "agents": {
                "claude-pro": {"enabled": True, "category": "agent"},
                "claude-bedrock": {"enabled": True, "category": "agent"},
                "codex": {"enabled": True, "category": "agent"},
                "cursor": {"enabled": True, "category": "utility"}
            },
            "settings": {"default_agent": "claude-pro", "dry_run": True}
        }

    def test_agent_wrapper_initialization(self):
        wrapper = AgentWrapper("test_agent", {})
        self.assertEqual(wrapper.name, "test_agent")

    def test_claude_wrapper_dry_run_pro(self):
        wrapper = ClaudeWrapper("claude-pro", {"dry_run": True})
        with patch('sys.stdout', new=StringIO()) as fake_out:
            wrapper.execute("test task")
            self.assertIn("[claude-pro] Dry run:", fake_out.getvalue())

    def test_claude_wrapper_dry_run_bedrock(self):
        wrapper = ClaudeWrapper("claude-bedrock", {"dry_run": True})
        with patch('sys.stdout', new=StringIO()) as fake_out:
            wrapper.execute("test task")
            self.assertIn("[claude-bedrock] Dry run:", fake_out.getvalue())

    def test_unknown_agent_handling(self):
        # Verify that asking for an unknown agent (if we were to implement that check in a factory) 
        # or just checking the dict 
        self.assertNotIn("unknown_agent", AGENT_CLASSES)

if __name__ == '__main__':
    unittest.main()
