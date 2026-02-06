\# AI Ops Assistant



AI Ops Assistant is a modular multi-agent backend system built using FastAPI.

It dynamically plans and executes tasks using external APIs.



---



\## Features



\- Multi-agent architecture (Planner, Executor, Verifier)

\- Weather data via OpenWeather API

\- Trending GitHub repository search

\- Structured execution plan output

\- Modular and extensible design



---



\## Architecture



Planner Agent:

\- Analyzes user query

\- Creates structured plan of steps



Executor Agent:

\- Executes tools based on plan

\- Calls external APIs



Verifier Agent:

\- Validates results



Tools:

\- Weather Tool (OpenWeather API)

\- GitHub Search Tool (GitHub REST API)



---



\## APIs Used



1\. OpenWeather API

2\. GitHub Search API



---



\## Setup Instructions



1\. Clone the repository

2\. Navigate into project folder

3\. Create virtual environment:



&nbsp;  python -m venv venv



4\. Activate virtual environment:



&nbsp;  Windows:

&nbsp;  .\\venv\\Scripts\\Activate



5\. Install dependencies:



&nbsp;  pip install -r requirements.txt



6\. Create .env file:



&nbsp;  OPENWEATHER\_API\_KEY=your\_api\_key\_here



7\. Run server:



&nbsp;  uvicorn main:app --reload



8\. Open in browser:



&nbsp;  http://127.0.0.1:8000/docs



---



\## Example Prompts



\- Get weather in Delhi

\- Find trending Python repositories

\- Find trending Java repositories and weather in Mumbai

\- Weather in Bangalore



---



\## Known Limitations



\- Basic keyword-based planner (no NLP parsing)

\- City extraction is simple heuristic-based

\- No frontend UI

\- Limited error handling



---



\## Future Improvements



\- Add LLM-based planner

\- Add frontend dashboard

\- Improve natural language understanding

\- Add caching layer



---



\## Tech Stack



\- Python

\- FastAPI

\- Uvicorn

\- Requests

\- python-dotenv

\- Pydantic



