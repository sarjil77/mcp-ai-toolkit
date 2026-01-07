# MCP AI Toolkit - Server Documentation

Detailed documentation for each MCP server in the toolkit.

---

## Table of Contents

1. [insurance Server](#insurance-server)
2. [Research Server](#research-server)
3. [Content Aggregator Server](#content-aggregator-server)
4. [Decision Engine Server](#decision-engine-server)
5. [Monitoring & Alerts Server](#monitoring--alerts-server)
6. [WhatsApp Server](#whatsapp-server)

---

## insurance Server

**File:** `servers/insurance_server.py`
**MCP Name:** `insurance`

### Purpose

Processes insurance certificate PDFs using the insurance API to extract structured data for compliance verification and document management.

### API Configuration

- **Base URL:** `https://staging-openai-endorsement-acc-api.injalaone.com`
- **Method:** POST
- **File Key:** `img`
- **Authentication:** None required

### Tools

#### `process_insurance_certificate(file_path: str)`

Process a complete insurance certificate PDF.

**Parameters:**
- `file_path`: Absolute path to the PDF file

**Returns:** Complete JSON with all extracted data including:
- CertificateHolder
- Classification
- Coverages
- Insured
- Producer
- Description of Operation
- Success status

#### `get_certificate_holder_info(file_path: str)`

Extract only certificate holder information.

**Returns:**
```json
{
  "Name": "Company Name",
  "Address": "123 Main St",
  "City": "San Francisco",
  "StateName": "CA",
  "ZipCode": "94105"
}
```

#### `get_coverage_details(file_path: str)`

Extract coverage details including limits and policy information.

**Returns:** List of coverage objects with:
- Coverage ID
- Limits (type, amount)
- Policy Info (carrier, policy number, dates)
- Endorsements

#### `get_insured_information(file_path: str)`

Extract insured party details.

#### `get_producer_information(file_path: str)`

Extract insurance agent/producer information.

#### `validate_certificate_signature(file_path: str)`

Check if the certificate is digitally signed.

**Returns:**
```json
{
  "signed": "Yes",
  "filename": ["certificate.pdf"],
  "classification": "COI"
}
```

---

## Research Server

**File:** `servers/research_server.py`
**MCP Name:** `research`

### Purpose

Search and manage academic papers from ArXiv with intelligent organization and retrieval.

### Tools

#### `search_papers(topic: str, max_results: int = 5)`

Search ArXiv for papers on a specific topic.

**Parameters:**
- `topic`: Research topic to search
- `max_results`: Maximum papers to retrieve (default: 5)

**Returns:** List of paper IDs

**Side Effects:** Saves paper metadata to `data/papers/{topic}/papers_info.json`

#### `extract_info(paper_id: str)`

Get detailed information about a specific paper.

**Parameters:**
- `paper_id`: ArXiv paper ID (e.g., "2301.07041")

**Returns:** JSON string with paper details

### Resources

#### `papers://folders`

List all available topic folders with saved papers.

#### `papers://{topic}`

Get detailed information about all papers in a specific topic folder.

### Prompts

#### `generate_search_prompt(topic: str, num_papers: int = 5)`

Generate a structured prompt for Claude to search and analyze papers.

---

## Content Aggregator Server

**File:** `servers/content_aggregator_server.py`
**MCP Name:** `content-aggregator`

### Purpose

Comprehensive market intelligence and content synthesis across multiple domains.

### Tools

#### `research_job_market_intelligence(role: str, company: str = None, location: str = None)`

Get comprehensive job market research.

**Returns:**
- Salary insights (entry, mid, senior levels)
- Skills demand (hot, emerging, declining)
- Company insights
- Academic backing
- Actionable recommendations
- Next steps

#### `industry_trend_analysis(industry: str, timeframe: str = "next_12_months")`

Analyze industry trends and predictions.

**Returns:**
- Key trends (technology, regulatory, market)
- Growth opportunities with risk assessment
- Threat analysis
- Strategic recommendations

#### `competitive_intelligence(company_name: str, competitors: List[str])`

Gather competitive intelligence.

**Returns:**
- Competitive landscape analysis
- Technology stack comparison
- SWOT analysis
- Strategic insights

#### `research_synthesis(topic: str, sources: List[str], focus_area: str = None)`

Synthesize research from multiple sources.

**Returns:**
- Key findings with consensus and conflicts
- Practical implications
- Future research directions
- Confidence levels

---

## Decision Engine Server

**File:** `servers/decision_engine_server.py`
**MCP Name:** `decision-engine`

### Purpose

AI-powered decision support for career planning, strategic research, and priority management.

### Tools

#### `analyze_career_opportunity(opportunity: Dict, user_profile: Dict)`

Comprehensive analysis of job opportunities.

**Parameters:**
- `opportunity`: Job details (company, title, salary, etc.)
- `user_profile`: Your skills, experience, values

**Returns:**
- Fit analysis with scoring (skill, experience, cultural fit)
- Opportunity potential assessment
- Risk assessment with mitigation strategies
- Competitive analysis
- Action recommendations with timeline
- Decision confidence level

#### `strategic_research_planning(research_goals: List[str], time_budget: int, current_knowledge: Dict)`

Create a structured research/learning plan.

**Parameters:**
- `research_goals`: Learning objectives
- `time_budget`: Hours per week available
- `current_knowledge`: Current skill levels

**Returns:**
- 12-week phased learning path
- Success metrics
- Risk mitigation strategies
- Adaptive features

#### `intelligent_priority_ranking(tasks: List[Dict], criteria: Dict)`

Multi-criteria prioritization of tasks/opportunities.

**Parameters:**
- `tasks`: List of items to prioritize
- `criteria`: Weights for impact, urgency, effort, feasibility, alignment

**Returns:**
- Ranked items with detailed scores
- Quick wins identification
- High-impact projects
- Bottlenecks to address

#### `generate_personalized_recommendations(user_data: Dict, context: Dict)`

Generate personalized recommendations.

**Returns:**
- Career recommendations
- Learning recommendations
- Networking recommendations
- Optimization strategies
- Success metrics with timelines

---

## Monitoring & Alerts Server

**File:** `servers/monitoring_server.py`
**MCP Name:** `monitoring-alerts`

### Purpose

Real-time monitoring for jobs, research, and industry news with intelligent alerting.

### Tools

#### `create_job_monitor(companies: List[str], keywords: List[str], alert_contact: str, check_frequency: str = "daily")`

Set up job posting monitoring.

**Returns:**
- Monitor ID
- Current matches found
- Next check time
- Alert configuration

#### `create_research_monitor(topics: List[str], alert_contact: str, min_relevance: str = "high")`

Monitor new research publications.

**Returns:**
- Monitor setup details
- Recent papers sample
- Sources being monitored

#### `create_industry_news_monitor(industry: str, keywords: List[str], alert_contact: str)`

Monitor industry news and developments.

**Returns:**
- Monitor configuration
- Recent news items
- Sources tracked

#### `check_all_monitors()`

Execute all active monitors and generate alerts.

**Returns:**
- Summary of checks
- New findings
- Alerts generated

#### `get_personalized_alerts(contact: str, days: int = 7)`

Get personalized alert summary.

**Returns:**
- Priority alerts
- Weekly digest
- Recommendations
- Upcoming deadlines

#### `create_smart_digest(topics: List[str], frequency: str)`

Create periodic summary digests.

**Returns:**
- Summary statistics
- Top highlights
- Action items

---

## WhatsApp Server

**File:** `whatsapp-mcp/whatsapp-mcp-server/main.py`
**MCP Name:** `whatsapp`

### Purpose

Integration with WhatsApp for messaging capabilities via the WhatsApp Bridge.

### Prerequisites

Requires the WhatsApp Bridge (Go application) to be running.

### Tools

#### `search_contacts(query: str)`

Search contacts by name or phone number.

#### `list_messages(after, before, sender_phone_number, chat_jid, query, limit, page, include_context, context_before, context_after)`

Get messages with various filters.

#### `list_chats(query, limit, page, include_last_message, sort_by)`

Get chat list.

#### `get_chat(chat_jid, include_last_message)`

Get specific chat metadata.

#### `get_direct_chat_by_contact(sender_phone_number)`

Get chat by phone number.

#### `get_contact_chats(jid, limit, page)`

Get all chats involving a contact.

#### `get_last_interaction(jid)`

Get most recent message with a contact.

#### `get_message_context(message_id, before, after)`

Get context around a specific message.

#### `send_message(chat_jid, message)`

Send a text message.

#### `send_file(chat_jid, file_path, caption)`

Send a file attachment.

#### `send_audio_message(chat_jid, file_path)`

Send a voice message.

#### `download_media(message_id, output_path)`

Download media from a message.

---

## Common Patterns

### Error Handling

All servers return error information in a consistent format:

```json
{
  "error": "Error message",
  "Success": "False"
}
```

### Timestamps

Most responses include ISO-8601 formatted timestamps:

```json
{
  "created_at": "2025-01-07T10:30:00.000000",
  "analysis_date": "2025-01-07T10:30:00.000000"
}
```

### Unique IDs

Operations that create entities generate unique IDs:

```json
{
  "monitor_id": "job_monitor_1736245800",
  "plan_id": "research_plan_1736245800"
}
```
