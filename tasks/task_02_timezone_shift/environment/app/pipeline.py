from pathlib import Path
import pandas as pd

DATA = Path("/app/data")
OUT = Path("/app/output")

EVENT_ID = "event" + "_" + "id"
OCCURRED_AT = "occurred" + "_" + "at"


def main():
    frame = pd.read_csv(DATA / "events.csv")

    required = {EVENT_ID, OCCURRED_AT, "amount"}
    if set(frame.columns) != required:
        raise ValueError("unexpected columns")

    if frame[EVENT_ID].duplicated().any():
        raise ValueError("duplicate event id")

    frame["amount"] = pd.to_numeric(frame["amount"], errors="raise")
    frame[OCCURRED_AT] = pd.to_datetime(
        frame[OCCURRED_AT],
        utc=True,
        errors="raise",
    )

    # Intentional bug:
    # UTC date is used directly instead of converting to Asia/Kolkata.
    frame["date"] = frame[OCCURRED_AT].dt.date.astype(str)

    result = (
        frame.groupby("date", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "revenue"})
    )

    OUT.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUT / "daily_revenue.csv", index=False)


main()