import csv
import math
from pathlib import Path


OUTPUT_FILE = Path("/app/output/monthly_revenue.csv")
REWARD_FILE = Path("/logs/verifier/reward.txt")

EXPECTED_MONTH = "2026-02"
EXPECTED_REVENUE = 1115.0


def write_reward(value: float) -> None:
    REWARD_FILE.parent.mkdir(parents=True, exist_ok=True)
    REWARD_FILE.write_text(str(value))


def grade() -> float:
    if not OUTPUT_FILE.exists():
        return 0.0

    try:
        with OUTPUT_FILE.open(newline="") as file:
            rows = list(csv.DictReader(file))

        if len(rows) != 1:
            return 0.0

        row = rows[0]
        if row.get("month") != EXPECTED_MONTH:
            return 0.0

        revenue = float(row["revenue"])
        if not math.isclose(revenue, EXPECTED_REVENUE, abs_tol=0.01):
            return 0.0

        return 1.0
    except Exception:
        return 0.0


if __name__ == "__main__":
    write_reward(grade())
