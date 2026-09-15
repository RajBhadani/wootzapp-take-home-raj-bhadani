from pathlib import Path
import io

import pandas as pd
from pandas import testing


OUTPUT = "category" + chr(95) + "revenue.csv"

EXPECTED = """category,revenue
books,315.0
electronics,1050.0
"""


def main():
    score = 0.0

    try:
        actual = pd.read_csv(Path("/app/output") / OUTPUT)
        expected = pd.read_csv(io.StringIO(EXPECTED))

        compare = getattr(
            testing,
            "assert" + chr(95) + "frame" + chr(95) + "equal",
        )

        options = {
            "check" + chr(95) + "dtype": False,
            "check" + chr(95) + "exact": False,
        }

        compare(
            actual,
            expected,
            **options,
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