from pathlib import Path

import pandas as pd


DATA = Path("/app/data")
OUT = Path("/app/output")

INVOICE_ID = "invoice" + "_" + "id"
CUSTOMER_ID = "customer" + "_" + "id"
INVOICE_DATE = "invoice" + "_" + "date"


def main():
    frame = pd.read_csv(DATA / "invoices.csv")

    required = {
        INVOICE_ID,
        CUSTOMER_ID,
        INVOICE_DATE,
        "amount",
    }

    if set(frame.columns) != required:
        raise ValueError("unexpected columns")

    if frame[INVOICE_ID].duplicated().any():
        raise ValueError("duplicate invoice id")

    frame[INVOICE_DATE] = pd.to_datetime(
        frame[INVOICE_DATE],
        errors="raise",
    )

    frame["amount"] = pd.to_numeric(
        frame["amount"],
        errors="raise",
    )

    frame["month"] = frame[INVOICE_DATE].dt.to_period("M").astype(str)

    # Intentional bug:
    # Groups by customer only and keeps the first month.
    result = (
        frame.groupby(CUSTOMER_ID, as_index=False)
        .agg(
            month=("month", "first"),
            revenue=("amount", "sum"),
        )
    )

    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(
        OUT / ("customer" + "_" + "month" + "_" + "revenue.csv"),
        index=False,
    )


main()