def build_prompt(review, examples):
    prompt = """
You are an expert sentiment analysis system.
Classify the sentiment of each movie review as positive or negative.

Examples:
"""

    for _, row in examples.iterrows():
        prompt += f"""
Review:
{row['text']}
Sentiment: {row['sentiment']}
"""

    prompt += f"""
Now classify the following review:

Review:
{review}

Sentiment:
"""
    return prompt