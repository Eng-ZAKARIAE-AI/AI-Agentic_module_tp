def build_prompt(review, examples=None):
    return f"""
Classify the sentiment of the following movie review.
Respond with only one word: positive or negative.

Review:
{review}

Sentiment:
"""