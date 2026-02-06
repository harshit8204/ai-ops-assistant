class PlannerAgent:

    @staticmethod
    def create_plan(user_query: str):
        user_query = user_query.lower()
        steps = []

        # Weather detection
        if "weather" in user_query:
            words = user_query.split()
            if "in" in words:
                city = words[words.index("in") + 1].capitalize()
            else:
                city = "Delhi"

            steps.append({
                "tool": "weather",
                "parameters": {
                    "city": city
                }
            })

        # GitHub detection
        if any(word in user_query for word in [
            "github", "repository", "repositories",
            "repo", "repos", "project", "projects",
            "trending"
        ]):

            language = "python"
            if "java" in user_query:
                language = "java"
            elif "javascript" in user_query:
                language = "javascript"

            steps.append({
                "tool": "github_search",
                "parameters": {
                    "language": language,
                    "sort": "stars"
                }
            })

        return {"steps": steps}
