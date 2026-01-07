# MCP AI Toolkit - Setup Guide

This guide will help you set up the MCP AI Toolkit on your system.

## Prerequisites

### 1. Python 3.10+

Ensure you have Python 3.10 or higher installed:

```bash
python --version
```

### 2. uv Package Manager (Recommended)

Install [uv](https://github.com/astral-sh/uv) for fast Python package management:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Claude Desktop

Download and install [Claude Desktop](https://claude.ai/download) for using MCP servers with Claude.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/mcp-ai-toolkit.git
cd mcp-ai-toolkit
```

### Step 2: Install Dependencies

Using uv (recommended):
```bash
uv sync
```

Using pip:
```bash
pip install -e .
```

### Step 3: Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Step 4: Configure Claude Desktop

Add the MCP servers to your Claude Desktop configuration:

**Linux:** `~/.config/claude/claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "asureitfy": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit", "run", "servers/asureitfy_server.py"]
    },
    "research": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit", "run", "servers/research_server.py"]
    },
    "content-aggregator": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit", "run", "servers/content_aggregator_server.py"]
    },
    "decision-engine": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit", "run", "servers/decision_engine_server.py"]
    },
    "monitoring-alerts": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit", "run", "servers/monitoring_server.py"]
    }
  }
}
```

**Important:** Replace `/path/to/mcp-ai-toolkit` with the actual path to your installation.

### Step 5: Restart Claude Desktop

After updating the configuration, restart Claude Desktop for changes to take effect.

## WhatsApp Integration (Optional)

The WhatsApp server requires the [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) bridge.

### Setup WhatsApp Bridge

1. Install Go 1.19+
2. Navigate to the bridge directory:
   ```bash
   cd whatsapp-mcp/whatsapp-bridge
   ```
3. Run the bridge:
   ```bash
   go run main.go
   ```
4. Scan the QR code with WhatsApp on your phone

### Add WhatsApp to Claude Desktop

```json
{
  "mcpServers": {
    "whatsapp": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit/whatsapp-mcp/whatsapp-mcp-server", "run", "main.py"]
    }
  }
}
```

## Verification

### Test Server Connection

You can test if servers are working by running them directly:

```bash
# Test research server
uv run servers/research_server.py

# Test asureitfy server
uv run servers/asureitfy_server.py
```

### Test with Claude

Open Claude Desktop and try:
- "Search for papers on machine learning"
- "What MCP tools do you have available?"

## Troubleshooting

### Common Issues

1. **Server not appearing in Claude**
   - Check the file paths in claude_desktop_config.json
   - Ensure uv is installed and in your PATH
   - Restart Claude Desktop

2. **Import errors**
   - Run `uv sync` to install all dependencies
   - Check Python version is 3.10+

3. **Permission errors**
   - Ensure the script files have execute permissions
   - Check file ownership

### Getting Help

- Open an issue on GitHub
- Check existing issues for solutions
- Review the server logs for error messages
