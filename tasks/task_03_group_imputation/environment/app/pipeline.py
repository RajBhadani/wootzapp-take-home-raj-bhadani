from pathlib import Path

import pandas as pd


DATA = Path("/app/data")
OUT = Path("/app/output")


def main():
    frame = pd.read_csv(DATA / "orders.csv")

    frame["list_price"] = pd.to_numeric(
        frame["list_price"],
        errors="raise",
    )

    frame["discount"] = pd.to_numeric(
        frame["discount"],
        errors="coerce",
    )

    category_medians = frame.groupby("category")["discount"].transform("median")
    frame["discount"] = frame["discount"].fillna(category_medians)

    frame["revenue"] = frame["list_price"] * (1 - frame["discount"])

    result = (
        frame.groupby("category", as_index=False)["revenue"]
        .sum()
        .round({"revenue": 2})
    )

    result = result[["category", "revenue"]]

    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(
        OUT / "category_revenue.csv",
        index=False,
    )


if __name__ == "__main__":
    main()