from autogen import AssistantAgent, UserProxyAgent
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("API key not found. Did you create a .env file?")

# Assign key securely
os.environ["OPENAI_API_KEY"] = api_key

# Define the summarizer agent
summarizer = AssistantAgent(
    name="SummarizerAgent",
    llm_config={
        "api_key": api_key,
        "model": "gpt-3.5-turbo",
        "temperature": 0.2
    }
)

# Define the user agent
user = UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)
# inside summarizer.py (at the bottom)
if __name__ == "__main__":
    test_code = """
def add(a, b):
    return a + b
"""
    message = f"Please summarize this function:\n{test_code}"
    user.initiate_chat(summarizer, message=message)

