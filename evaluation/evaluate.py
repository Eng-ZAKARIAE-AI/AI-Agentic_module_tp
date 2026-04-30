import re
from tqdm import tqdm
from utils.sampling import generate_fewshot_examples
from evaluation.metrics import compute_metrics
from llm.client import llm_predict

def evaluate(df_gold, df_pool, prompt_builder, runs=10, n_shots=8):
    results = []

    for seed in range(runs):
        y_true, y_pred = [], []

        examples = generate_fewshot_examples(
            df_pool,
            seed=seed,
            n_per_class=n_shots // 2
        )

        for _, row in tqdm(df_gold.iterrows(), total=len(df_gold)):
            prompt = prompt_builder(row["text"], examples)
            raw_prediction = llm_predict(prompt)
            
            # Robust extraction using regex to find the last mention of positive/negative
            matches = re.findall(r'\b(positive|negative)\b', raw_prediction.lower())
            if matches:
                prediction = matches[-1] # Take the last one
            else:
                prediction = raw_prediction.strip().lower() # fallback
            
            # Debugging print
            if prediction != row["sentiment"]:
                print(f"\nMISMATCH found!")
                print(f"True: {row['sentiment']}, Pred: '{prediction}'")
                # print(f"Prompt sent:\n{prompt}")
                print(f"Raw response:\n{raw_prediction}\n")
            else:
                # print(f"DEBUG: True: {row['sentiment']}, Pred: '{prediction}'")
                pass

            y_true.append(row["sentiment"])
            y_pred.append(prediction)

        results.append(compute_metrics(y_true, y_pred))

    return results