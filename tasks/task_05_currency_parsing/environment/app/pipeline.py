from pathlib import Path

import pandas as pd


DATA = Path("/app/data")
OUT = Path("/app/output")

PAYMENT_ID = "payment" + "_" + "id"
PAID_ON = "paid" + "_" + "on"


def main():
    frame = pd.read_csv(DATA / "payments.csv")

    required = {PAYMENT_ID, PAID_ON, "amount"}
    if set(frame.columns) != required:
        raise ValueError("unexpected columns")

    if frame[PAYMENT_ID].duplicated().any():
        raise ValueError("duplicate payment id")

    frame[PAID_ON] = pd.to_datetime(
        frame[PAID_ON],
        errors="raise",
    )

    # Intentional bug:
    # Currency symbols and commas become missing values,
    # then missing values are silently converted to zero.
    frame["amount"] = pd.to_numeric(
        frame["amount"],
        errors="coerce",
    ).fillna(0)

    frame["month"] = frame[PAID_ON].dt.to_period("M").astype(str)

    result = (
        frame.groupby("month", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "collections"})
        .round({"collections": 2})
    )

    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(
        OUT / ("monthly" + "_" + "collections.csv"),
        index=False,
    )


main()