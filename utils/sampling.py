import pandas as pd
#(Balanced & unbiased few‑shot sampling)
def generate_fewshot_examples(df, n_per_class=4, seed=42):
    pos = df[df["sentiment"] == "positive"].sample(
        n_per_class, random_state=seed
    )
    neg = df[df["sentiment"] == "negative"].sample(
        n_per_class, random_state=seed
    )

    return (
        pd.concat([pos, neg])
        .sample(frac=1, random_state=seed)
        .reset_index(drop=True)
    )