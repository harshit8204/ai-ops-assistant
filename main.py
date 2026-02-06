from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/run")
def run_assistant(request: QueryRequest):

    user_query = request.query

    # 1️⃣ Plan
    plan = PlannerAgent.create_plan(user_query)

    # 2️⃣ Execute
    results = ExecutorAgent.execute(plan)

    # 3️⃣ Verify
    verification = VerifierAgent.verify(plan, results)

    return {
        "plan": plan,
        "results": results,
        "verification": verification
    }
