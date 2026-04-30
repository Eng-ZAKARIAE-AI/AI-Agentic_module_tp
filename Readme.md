# Sentiment Analysis Evaluation with LLMs

This project evaluates different prompting strategies for sentiment analysis on the IMDB movie review dataset using the `google/gemini-2.0-flash-001` model via OpenRouter.

## 🚀 Project Overview

The goal is to compare the performance and behavior of three core prompting techniques:
1. **Zero-Shot**: Direct classification with no context or examples.
2. **Few-Shot**: Providing a small set of labeled examples to guide the model.
3. **Chain-of-Thought (CoT)**: Encouraging the model to reason through its decision-making process before providing a final answer.

## 🛠️ Methodology

### Evaluation Pipeline
- **Dataset**: IMDB Movie Reviews (Binary classification: Positive/Negative).
- **Sampling**: Stratified sampling to ensure balanced classes in both the evaluation set and the few-shot pool.
- **Metrics**: Accuracy and Micro-F1 scores.
- **Robust Extraction**: Responses are parsed using regex to find the final sentiment even in long, reasoned outputs.

### Strategies
- **Zero-Shot**: "Classify... Respond with only one word: positive or negative."
- **Few-Shot**: Provides 8 balanced examples (4 positive, 4 negative) to establish pattern recognition.
- **Chain-of-Thought**: Instructs the model to:
    1. Identify key emotional words.
    2. Explain their contribution to the overall sentiment.
    3. Conclude with the final label.

## 📈 Key Findings

| Strategy | Performance | Behavior |
| :--- | :--- | :--- |
| **Zero-Shot** | **Extremely High (95-100%)** | Most efficient. The model has strong internal knowledge of the IMDB domain. |
| **Few-Shot** | **High (90-100%)** | Solid, but occasionally "distracted" by specific examples in the few-shot pool that might not align perfectly with the target review. |
| **Chain-of-Thought** | **Insightful (100% with regex)** | Provides excellent qualitative data. While accurate, it requires more robust parsing of the output to separate reasoning from the final label. |

### Observations on Model Reasoning
- **Nuance Identification**: In CoT mode, the model correctly identifies mixed sentiments (e.g., "good acting but terrible plot") and can weigh them to reach a final decision.
- **Bias**: Few-shot examples can sometimes introduce subtle biases if the examples are significantly different in style from the target review.

## 🔧 Improvements Made

During this session, several enhancements were made to the codebase:
- **Enhanced Debugging**: The evaluation script now prints detailed mismatch reports (True Label vs. Prediction + Raw Response) to facilitate error analysis.
- **Dynamic COT**: Refactored the Chain-of-Thought prompt to allow for genuine reasoning instead of restricting the model to a single word.
- **Regex Extraction**: Replaced simple string matching with a robust regex-based extraction logic to reliably find the final sentiment in long-form responses.
- **Scalability**: Updated the main execution loop to support larger sample sizes and multiple runs for statistical variance analysis.

## ⚠️ Known Issues & Troubleshooting
- **API Limits**: High-volume runs may trigger 429 (Rate Limit) or 504 (Timeout) errors from the upstream provider.
- **Neutrality**: For highly ambiguous reviews, the model may conclude a "Neutral" sentiment, which counts as an error in a binary (Positive/Negative) evaluation framework.

## 🏃 How to Run
```bash
python main.py
```
Check the console for real-time progress bars and final summary statistics for each method.
