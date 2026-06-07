from client import LLMClient
MY_INJECTED_KEY = "sk-or-Ur-API-Key"

# Initialize once
llm = LLMClient(MY_INJECTED_KEY)

# Use anywhere in your agents
response = llm.predict("Analyze this data: [1, 2, 3]")
print(response)