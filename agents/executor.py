from tools.github_tool import GitHubTool
from tools.weather_tool import WeatherTool

class ExecutorAgent:

    @staticmethod
    def execute(plan: dict):
        results = []

        for step in plan["steps"]:
            tool = step["tool"]
            params = step["parameters"]

            if tool == "github_search":
                result = GitHubTool.search_repositories(
                    language=params.get("language"),
                    sort=params.get("sort", "stars")
                )

            elif tool == "weather":
                city = params.get("city") or params.get("location")
                if not city:
                    raise ValueError("City parameter missing for weather tool")

                result = WeatherTool.get_weather(city=city)

            else:
                result = {"error": f"Unknown tool: {tool}"}

            results.append({
                "tool": tool,
                "result": result
            })

        return results
