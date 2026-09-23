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

user_prompt = "What opportunites are avaliable for someone with no IT experience"

response = agent.invoke({"messages": [{"role": "user", "content": user_prompt}]})
print(response["messages"][-1].content[0]["text"])