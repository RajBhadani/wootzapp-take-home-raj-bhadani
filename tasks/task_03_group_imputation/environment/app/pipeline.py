from pathlib import Path

import pandas as pd


DATA = Path("/app/data")
OUT = Path("/app/output")

ORDER_ID = "order" + "_" + "id"
LIST_PRICE = "list" + "_" + "price"


def main():
    frame = pd.read_csv(DATA / "orders.csv")

    required = {ORDER_ID, "category", LIST_PRICE, "discount"}
    if set(frame.columns) != required:
        raise ValueError("unexpected columns")

    if frame[ORDER_ID].duplicated().any():
        raise ValueError("duplicate order id")

    frame[LIST_PRICE] = pd.to_numeric(
        frame[LIST_PRICE],
        errors="raise",
    )

    frame["discount"] = pd.to_numeric(
        frame["discount"],
        errors="coerce",
    )

    # Intentional bug:
    # Missing discounts are filled with one global mean.
    frame["discount"] = frame["discount"].fillna(
        frame["discount"].mean()
    )

    frame["revenue"] = frame[LIST_PRICE] * (1 - frame["discount"])

    result = (
        frame.groupby("category", as_index=False)["revenue"]
        .sum()
        .round({"revenue": 2})
    )

    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(
        OUT / ("category" + "_" + "revenue.csv"),
        index=False,
    )


main()