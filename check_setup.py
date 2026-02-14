import shutil
import sys

TOOLS = ["claude", "codex", "gemini", "cursor", "antigravity"]

def check_tools():
    missing = []
    print("🔍 Checking for required CLI tools...")
    for tool in TOOLS:
        if shutil.which(tool):
            print(f"✅ Found: {tool}")
        else:
            print(f"❌ Missing: {tool}")
            missing.append(tool)
    
    if missing:
        print("\n⚠️  The following tools are missing from your PATH:")
        for tool in missing:
            print(f"   - {tool}")
        print("\nPlease install these tools or update config.yaml with absolute paths.")
        print("Note: The orchestrator will verify these at runtime.")
        sys.exit(1)
    else:
        print("\n🎉 All tools are available!")
        sys.exit(0)

if __name__ == "__main__":
    check_tools()
