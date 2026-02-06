import requests

class GitHubTool:

    BASE_URL = "https://api.github.com"

    @staticmethod
    def search_repositories(language: str, sort: str = "stars"):
        url = f"{GitHubTool.BASE_URL}/search/repositories"
        params = {
            "q": f"language:{language}",
            "sort": sort,
            "order": "desc"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        items = response.json()["items"][:5]

        return [
            {
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "url": repo["html_url"],
                "description": repo["description"]
            }
            for repo in items
        ]
