from pathlib import Path
import io

import pandas as pd
from pandas import testing


OUTPUT = "daily" + "_" + "revenue.csv"

EXPECTED = """date,revenue
2026-02-02,175
2026-02-03,75
"""


def main():
    score = 0.0

    try:
        actual = pd.read_csv(Path("/app/output") / OUTPUT)
        expected = pd.read_csv(io.StringIO(EXPECTED))

        actual = actual.sort_index(axis=1)
        expected = expected.sort_index(axis=1)

        compare = getattr(testing, "assert" + "_" + "frame" + "_" + "equal")

        compare(
            actual,
            expected,
            check_dtype=False,
            check_exact=False,
            atol=0.01,
            rtol=0,
        )

        score = 1.0

    except Exception:
        score = 0.0

    reward_dir = Path("/logs/verifier")
    reward_dir.mkdir(parents=True, exist_ok=True)
    (reward_dir / "reward.txt").write_text(str(score))


main()