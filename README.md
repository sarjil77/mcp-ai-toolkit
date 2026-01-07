<p align="center">
  <img src="https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue?style=for-the-badge" alt="MCP"/>
  <img src="https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
</p>

<h1 align="center">🤖 MCP AI Toolkit</h1>

<p align="center">
  <strong>A comprehensive suite of Model Context Protocol (MCP) servers for AI-powered automation</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-servers">Servers</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-demo">Demo</a>
</p>

---

## 🌟 Overview

MCP AI Toolkit is a collection of specialized MCP servers that extend AI assistants (like Claude) with powerful real-world capabilities. From processing insurance documents to monitoring job markets and conducting academic research, this toolkit demonstrates the potential of AI-human collaboration.

## ✨ Features

| Server | Description | Key Capabilities |
|--------|-------------|------------------|
| 🔐 **insurance** | Insurance Certificate Processing | PDF extraction, coverage analysis, signature validation |
| 📚 **Research** | Academic Paper Management | ArXiv search, paper storage, research synthesis |
| 📊 **Content Aggregator** | Market Intelligence | Job market analysis, industry trends, competitive intelligence |
| 🧠 **Decision Engine** | AI-Powered Decision Support | Career analysis, strategic planning, priority ranking |
| 🔔 **Monitoring & Alerts** | Real-time Monitoring | Job alerts, research tracking, industry news monitoring |
| 💬 **WhatsApp** | Messaging Integration | Send/receive messages, contact management, media sharing |

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Claude Desktop / AI Client                │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    │ MCP Protocol (stdio)
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                         MCP Server Layer                         │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┤
│insurance │ Research │ Content  │ Decision │Monitoring│ WhatsApp │
│ Server   │  Server  │Aggregator│  Engine  │ & Alerts │  Server  │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
     │           │          │          │          │          │
     ▼           ▼          ▼          ▼          ▼          ▼
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│insurance │  ArXiv   │  Market  │ Analysis │  News &  │ WhatsApp │
│   API    │   API    │   Data   │ Engines  │ Job APIs │  Bridge  │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

## 📦 Installation

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Claude Desktop or compatible MCP client

### Quick Start

```bash
# Clone the repository
git clone https://github.com/sarjil77/mcp-ai-toolkit.git
cd mcp-ai-toolkit

# Install dependencies using uv
uv sync

# Or using pip
pip install -e .
```

### Configure Claude Desktop

Add the following to your Claude Desktop MCP configuration (`~/.config/claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "insurance": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-ai-toolkit", "run", "servers/insurance_server.py"]
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

## 🔧 Servers

### 🔐 insurance Server

Processes insurance certificate PDFs using the insurance API to extract structured data.

**Tools:**
| Tool | Description |
|------|-------------|
| `process_insurance_certificate` | Process complete PDF and extract all data |
| `get_certificate_holder_info` | Extract certificate holder details |
| `get_coverage_details` | Extract coverage limits and policy info |
| `get_insured_information` | Extract insured party details |
| `get_producer_information` | Extract agent/producer information |
| `validate_certificate_signature` | Verify digital signature status |

**Example:**
```python
# Process an insurance certificate
result = process_insurance_certificate("/path/to/certificate.pdf")

# Get specific coverage details
coverages = get_coverage_details("/path/to/certificate.pdf")
```

---

### 📚 Research Server

Search and manage academic papers from ArXiv with intelligent organization.

**Tools:**
| Tool | Description |
|------|-------------|
| `search_papers` | Search ArXiv for papers on a topic |
| `extract_info` | Get detailed info about a specific paper |

**Resources:**
| Resource | Description |
|----------|-------------|
| `papers://folders` | List all saved topic folders |
| `papers://{topic}` | Get papers for a specific topic |

**Example:**
```python
# Search for AI papers
paper_ids = search_papers("Large Language Models", max_results=10)

# Get paper details
info = extract_info("2301.07041")
```

---

### 📊 Content Aggregator Server

Comprehensive market intelligence and trend analysis.

**Tools:**
| Tool | Description |
|------|-------------|
| `research_job_market_intelligence` | Job market research with salary insights |
| `industry_trend_analysis` | Industry trend predictions and analysis |
| `competitive_intelligence` | SWOT analysis and competitive comparison |
| `research_synthesis` | Synthesize research from multiple sources |

**Example:**
```python
# Get job market intelligence
intel = research_job_market_intelligence(
    role="AI Engineer",
    company="OpenAI",
    location="San Francisco"
)
```

---

### 🧠 Decision Engine Server

AI-powered decision support for career and strategic planning.

**Tools:**
| Tool | Description |
|------|-------------|
| `analyze_career_opportunity` | Comprehensive job opportunity analysis |
| `strategic_research_planning` | Create phased learning/research plans |
| `intelligent_priority_ranking` | Multi-criteria task prioritization |
| `generate_personalized_recommendations` | Personalized career/learning advice |

**Example:**
```python
# Analyze a job opportunity
analysis = analyze_career_opportunity(
    opportunity={"company": "Google", "title": "AI Engineer", "salary": "$180k"},
    user_profile={"experience_years": 5, "skills": ["Python", "ML"]}
)
```

---

### 🔔 Monitoring & Alerts Server

Real-time monitoring for jobs, research, and industry news.

**Tools:**
| Tool | Description |
|------|-------------|
| `create_job_monitor` | Monitor job postings at companies |
| `create_research_monitor` | Track new research publications |
| `create_industry_news_monitor` | Monitor industry developments |
| `check_all_monitors` | Execute all active monitors |
| `get_personalized_alerts` | Get alert summary for a contact |
| `create_smart_digest` | Create periodic summary digests |

**Example:**
```python
# Set up job monitoring
monitor = create_job_monitor(
    companies=["Google", "Microsoft", "OpenAI"],
    keywords=["AI Engineer", "Machine Learning"],
    alert_contact="+1234567890"
)
```

---

### 💬 WhatsApp Server

Integration with WhatsApp for messaging capabilities (uses [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)).

**Tools:**
| Tool | Description |
|------|-------------|
| `search_contacts` | Search contacts by name/phone |
| `list_messages` | Get messages with filters |
| `list_chats` | Get chat list |
| `send_message` | Send text message |
| `send_file` | Send file attachment |
| `send_audio_message` | Send voice message |

## 🎮 Usage

### With Claude Desktop

Once configured, simply ask Claude to use the tools:

```
"Process this insurance certificate and tell me if it's valid"
"Search for recent papers on RAG systems"
"Analyze this job opportunity at Google"
"Set up monitoring for AI Engineer positions"
```

### Programmatic Usage

```python
from clients.mcp_chatbot import MCP_ChatBot
import asyncio

async def main():
    chatbot = MCP_ChatBot()
    await chatbot.connect_to_servers()
    
    response = await chatbot.process_query(
        "Search for papers on transformer architecture"
    )
    print(response)

asyncio.run(main())
```

## 🎬 Demo: Insurance Certificate Processing

A powerful demo showcasing the insurance server with WhatsApp integration:

### Scenario
Automated insurance certificate verification with mobile alerts.

### Flow
1. **Upload PDF** → insurance extracts structured data
2. **Validate Coverage** → Check limits and expiration dates
3. **Send Alert** → WhatsApp notification with results

```python
# Process certificate
cert = process_insurance_certificate("/path/to/cert.pdf")

# Check coverage
coverage = get_coverage_details("/path/to/cert.pdf")

# Validate signature
signature = validate_certificate_signature("/path/to/cert.pdf")

# Alert via WhatsApp
if signature["signed"] == "Yes":
    send_message(contact, "✅ Certificate verified and valid!")
else:
    send_message(contact, "⚠️ Certificate requires signature!")
```

## 📁 Project Structure

```
mcp-ai-toolkit/
├── servers/                     # MCP Server implementations
│   ├── insurance_server.py      # Insurance certificate processing
│   ├── research_server.py       # Academic research management
│   ├── content_aggregator_server.py  # Market intelligence
│   ├── decision_engine_server.py     # Decision support
│   └── monitoring_server.py     # Monitoring & alerts
│
├── clients/                     # Client implementations
│   └── mcp_chatbot.py           # Anthropic-based chatbot client
│
├── examples/                    # Usage examples
│   └── example_usage.py
│
├── data/                        # Data storage
│   └── papers/                  # Saved research papers
│
├── server_config.json           # MCP server configuration
├── pyproject.toml               # Python project config
└── README.md
```

## 🔮 Roadmap

- [ ] Add real API integrations (LinkedIn, Indeed, NewsAPI)
- [ ] Implement persistent storage with SQLite/PostgreSQL
- [ ] Add authentication and rate limiting
- [ ] Create web dashboard for monitoring
- [ ] Add more MCP resources and prompts
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Anthropic](https://anthropic.com) for Claude and MCP
- [Model Context Protocol](https://modelcontextprotocol.io) specification
- [whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) for WhatsApp integration
- [ArXiv API](https://arxiv.org/help/api/) for research paper access

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/sarjil77">Sarjil</a>
</p>
