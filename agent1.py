import json 
from dotenv import load_dotenv

load_dotenv()

from deepagents import create_deep_agent

def search_opportunites(query: str) -> str:
    """Searches the verified Australian cybersecurity database for courses, scholarships, and traineeships."""

    with open("dataopp.json", "r") as f:
        opportunites = json.load(f)

    q = query.lower()

    results = [item for item in opportunites 
    if q in item ["title"].lower() or q in item["description"].lower()]

    if not results:
        results = opportunites

    return json.dumps(results)


agent = create_deep_agent(
    model = "google_genai:gemini-3.6-flash",
    tools = [search_opportunites]
)

def run_agent(user_message: str) -> str:
    response = agent.invoke({
        "messages": [{"role": "user", "content": user_message}]
    })
    content = response["messages"][-1].content
    if isinstance(content, list):
        return content[0].get("text", str(content))
    return str(content)

# optional: still test from terminal
if __name__ == "__main__":
    print(run_agent("What opportunities are available for someone with no IT experience"))