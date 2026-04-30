from client import LLMClient
MY_INJECTED_KEY = "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"

# Initialize once
llm = LLMClient(MY_INJECTED_KEY)

# Use anywhere in your agents
response = llm.predict("Analyze this data: [1, 2, 3]")
print(response)