import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
import numpy as np

from prompts.zero_shot import build_prompt as zero_prompt
from prompts.few_shot import build_prompt as few_prompt
from prompts.cot import build_prompt as cot_prompt
from evaluation.evaluate import evaluate


def prepare_data():
    ds = load_dataset("imdb")
    df = pd.DataFrame(ds["train"])
    df["sentiment"] = df["label"].map({0: "negative", 1: "positive"})

    return train_test_split(
        df,
        test_size=0.1,
        random_state=42,
        stratify=df["label"]
    )


def summarize(name, results):
    acc = [r["accuracy"] for r in results]
    f1 = [r["micro_f1"] for r in results]

    print(f"\n{name}")
    print(f"Accuracy: {np.mean(acc):.3f} ± {np.std(acc):.3f}")
    print(f"Micro‑F1: {np.mean(f1):.3f} ± {np.std(f1):.3f}")


def main():
    df_pool, df_gold = prepare_data()

    # Reduced for quick testing
    df_gold_small = df_gold.sample(5, random_state=42)

    print("Running ZERO‑SHOT...")
    zero = evaluate(df_gold_small, df_pool, zero_prompt, runs=1)
    print("Running FEW‑SHOT...")
    few = evaluate(df_gold_small, df_pool, few_prompt, runs=1)
    print("Running CHAIN‑OF‑THOUGHT...")
    cot = evaluate(df_gold_small, df_pool, cot_prompt, runs=1)

    summarize("ZERO‑SHOT", zero)
    summarize("FEW‑SHOT", few)
    summarize("CHAIN‑OF‑THOUGHT", cot)


if __name__ == "__main__":
    main()