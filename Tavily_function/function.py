from agents import function_tool
from configuration.config import tavily_api_key
import requests


@function_tool
def web_search(query: str):
    "Perform a web search using Tavily API"
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {tavily_api_key}"}
    payload = {"query": query, "search_depth": "basic"}

    res = requests.post(url, json=payload, headers=headers)
    if res.status_code == 200:
        data = res.json()
        return data.get("results", [])
    else:
        return {"error": res.text}