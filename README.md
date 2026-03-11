# 🤖 AI Ops Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![OpenWeather](https://img.shields.io/badge/OpenWeather-API-orange?style=for-the-badge&logo=openweathermap&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub-REST%20API-181717?style=for-the-badge&logo=github&logoColor=white)

**A modular, multi-agent backend system that autonomously plans, executes, and verifies tasks using real-world APIs — built with FastAPI.**

[📖 API Docs](#-api-documentation) &nbsp;·&nbsp; [🚀 Quick Start](#-getting-started) &nbsp;·&nbsp; [🐛 Report Bug](https://github.com/harshit8204/ai-ops-assistant/issues) &nbsp;·&nbsp; [✨ Request Feature](https://github.com/harshit8204/ai-ops-assistant/issues)

</div>

---

## 💡 What Is This?

**AI Ops Assistant** is a backend system inspired by **agentic AI workflows** — where instead of a single model doing everything, multiple specialized agents collaborate to complete a task.

You send it a natural language query like:

> *"Find trending Python repos and get the weather in Mumbai"*

And it autonomously:
1. 🧠 **Plans** — breaks the query into structured execution steps
2. ⚙️ **Executes** — calls the right tools and external APIs
3. ✅ **Verifies** — validates and returns a clean, structured response

This mirrors real-world **LLMOps / AI agent pipelines** used in production systems — making it a strong portfolio project for roles in **backend development, AI/ML engineering, and DevOps automation**.

---

## 🏗️ System Architecture

```
User Query (Natural Language)
         │
         ▼
┌─────────────────────┐
│    Planner Agent    │  ◄── Parses query → builds structured execution plan
└─────────┬───────────┘
          │  Execution Plan (JSON)
          ▼
┌─────────────────────┐
│   Executor Agent    │  ◄── Runs tools in sequence based on the plan
└─────────┬───────────┘
          │  Tool Results
          ▼
┌─────────────────────┐
│   Verifier Agent    │  ◄── Validates output, catches errors, ensures quality
└─────────┬───────────┘
          │  Final Response
          ▼
     Structured JSON Output
```

### 🧩 Agent Breakdown

| Agent | Responsibility |
|-------|---------------|
| 🧠 **Planner** | Analyzes user query → generates a step-by-step execution plan |
| ⚙️ **Executor** | Dispatches tasks to the right tools → calls external APIs |
| ✅ **Verifier** | Validates API responses → ensures result correctness |

### 🔧 Tools Available

| Tool | API Used | What It Does |
|------|----------|-------------|
| 🌦️ **Weather Tool** | OpenWeather API | Fetches real-time weather for any city |
| 🐙 **GitHub Search Tool** | GitHub REST API | Finds trending repositories by language/topic |

---

## ✨ Key Features

- 🤖 **Multi-Agent Pipeline** — Planner → Executor → Verifier architecture
- 🌦️ **Live Weather Data** — Real-time conditions via OpenWeather API
- 🐙 **GitHub Trending Search** — Discover hot repos by language or topic
- 📋 **Structured JSON Output** — Every response is clean and machine-readable
- ⚡ **Async-ready FastAPI Backend** — High performance, auto-documented REST API
- 🧱 **Modular & Extensible** — Add new tools/agents without touching existing code
- 📄 **Interactive Swagger Docs** — Explore and test every endpoint at `/docs`

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| 🐍 **Python** | 3.10+ | Core language |
| ⚡ **FastAPI** | 0.100+ | REST API framework |
| 🦄 **Uvicorn** | Latest | ASGI web server |
| 📦 **Requests** | Latest | HTTP client for external APIs |
| 🔐 **python-dotenv** | Latest | Environment variable management |
| 🧬 **Pydantic** | v2 | Data validation & serialization |

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python **3.10 or higher**
- A free [OpenWeather API key](https://openweathermap.org/api)

```bash
python --version   # should be 3.10+
```

### 📥 Installation

**1. Clone the repository**
```bash
git clone https://github.com/harshit8204/ai-ops-assistant.git
cd ai-ops-assistant
```

**2. Create & activate a virtual environment**
```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

> 🔑 Get a free API key at [openweathermap.org](https://openweathermap.org/api)

**5. Start the server**
```bash
uvicorn main:app --reload
```

**6. Open the interactive API docs**
```
http://127.0.0.1:8000/docs
```

---

## 📖 API Documentation

Once the server is running, visit **`http://127.0.0.1:8000/docs`** for the full interactive Swagger UI.

### Example Queries

| Prompt | What Happens |
|--------|-------------|
| `"Get weather in Delhi"` | Planner → Weather Tool → Delhi forecast |
| `"Find trending Python repositories"` | Planner → GitHub Tool → top Python repos |
| `"Find trending Java repos and weather in Mumbai"` | Planner → both tools run → combined result |
| `"Weather in Bangalore"` | Single-agent plan → Weather Tool only |

### Sample Response Structure

```json
{
  "query": "Find trending Python repositories and weather in Delhi",
  "plan": [
    { "step": 1, "tool": "github_search", "params": { "language": "python" } },
    { "step": 2, "tool": "weather", "params": { "city": "Delhi" } }
  ],
  "results": {
    "github_search": { "repositories": [...] },
    "weather": { "city": "Delhi", "temp": "32°C", "condition": "Clear" }
  },
  "verified": true
}
```

---

## 🗺️ Roadmap

- [x] Multi-agent architecture (Planner, Executor, Verifier)
- [x] Weather Tool via OpenWeather API
- [x] GitHub Trending Search Tool
- [x] Structured JSON execution plans
- [x] FastAPI with Swagger docs
- [ ] 🔜 LLM-based Planner (OpenAI / Gemini integration)
- [ ] 🔜 React frontend dashboard
- [ ] 🔜 Natural language understanding improvements
- [ ] 🔜 Redis caching layer for API responses
- [ ] 🔜 More tools — News API, Stock Prices, etc.

---

## ⚠️ Known Limitations

- Planner uses **keyword-based parsing** (no NLP/LLM yet)
- City extraction is **heuristic-based** — may miss edge cases
- No **frontend UI** — API-only for now
- **Basic error handling** — production hardening needed

> These are great starting points for contributions! See the Roadmap above.

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/add-llm-planner`
3. Commit changes: `git commit -m "feat: integrate OpenAI for planning"`
4. Push: `git push origin feature/add-llm-planner`
5. Open a Pull Request

---

## 👤 Author

**Harshit**

[![GitHub](https://img.shields.io/badge/GitHub-harshit8204-181717?style=flat-square&logo=github)](https://github.com/harshit8204)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 🌟 If this project helped you or you found it interesting, please give it a star!

*Built to explore agentic AI architecture and real-world API orchestration.*

</div>
