class VerifierAgent:

    @staticmethod
    def verify(plan: dict, results: list):

        if not plan.get("steps"):
            return {
                "status": "failed",
                "reason": "No plan steps generated."
            }

        if not results:
            return {
                "status": "failed",
                "reason": "No execution results returned."
            }

        # Check each step has a result
        for step in plan["steps"]:
            tool_name = step["tool"]

            matching = [r for r in results if r["tool"] == tool_name]

            if not matching:
                return {
                    "status": "failed",
                    "reason": f"Missing result for tool: {tool_name}"
                }

        return {
            "status": "success",
            "message": "Execution verified successfully."
        }
