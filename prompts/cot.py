def build_prompt(review, examples):
    prompt = """
You are an expert sentiment analysis system.

Analyze the sentiment of the movie review provided below.
First, identify key emotional or opinionated words and phrases.
Second, explain how these contribute to the overall sentiment.
Finally, conclude with the sentiment: positive or negative.

Examples:
"""

    for _, row in examples.iterrows():
        prompt += f"""
Review:
{row['text']}
Sentiment: {row['sentiment']}
"""

    prompt += f"""
Now analyze the following review.

Review:
{review}

Analysis:
"""
    return prompt