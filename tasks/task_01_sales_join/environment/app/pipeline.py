from pathlib import Path
from typing import Iterable

import pandas as pd


APP_DIR = Path("/app")
DATA_DIR = APP_DIR / "data"
OUTPUT_DIR = APP_DIR / "output"

SALES_COLUMNS = [
    "transaction_id",
    "sale_date",
    "store_id",
    "product_id",
    "quantity",
]

PRICE_COLUMNS = [
    "store_id",
    "product_id",
    "unit_price",
]


def require_columns(
    frame: pd.DataFrame,
    required_columns: Iterable[str],
    file_name: str,
) -> None:
    missing = set(required_columns) - set(frame.columns)
    if missing:
        formatted = ", ".join(sorted(missing))
        raise ValueError(f"{file_name} is missing required columns: {formatted}")


def load_csv(file_name: str) -> pd.DataFrame:
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return pd.read_csv(file_path)


def normalize_sales(sales: pd.DataFrame) -> pd.DataFrame:
    require_columns(sales, SALES_COLUMNS, "sales.csv")

    cleaned = sales.copy()
    cleaned["transaction_id"] = cleaned["transaction_id"].astype(str).str.strip()
    cleaned["store_id"] = cleaned["store_id"].astype(str).str.strip()
    cleaned["product_id"] = cleaned["product_id"].astype(str).str.strip()

    cleaned["sale_date"] = pd.to_datetime(
        cleaned["sale_date"],
        errors="raise",
    )

    cleaned["quantity"] = pd.to_numeric(
        cleaned["quantity"],
        errors="raise",
    )

    if cleaned["transaction_id"].duplicated().any():
        raise ValueError("sales.csv contains duplicate transaction IDs")

    if (cleaned["quantity"] <= 0).any():
        raise ValueError("Sales quantities must be positive")

    return cleaned


def normalize_prices(prices: pd.DataFrame) -> pd.DataFrame:
    require_columns(prices, PRICE_COLUMNS, "product_prices.csv")

    cleaned = prices.copy()
    cleaned["store_id"] = cleaned["store_id"].astype(str).str.strip()
    cleaned["product_id"] = cleaned["product_id"].astype(str).str.strip()

    cleaned["unit_price"] = pd.to_numeric(
        cleaned["unit_price"],
        errors="raise",
    )

    if (cleaned["unit_price"] <= 0).any():
        raise ValueError("Product prices must be positive")

    if cleaned.duplicated(["store_id", "product_id"]).any():
        raise ValueError(
            "product_prices.csv has duplicate store-product price records"
        )

    return cleaned


def create_monthly_revenue(
    sales: pd.DataFrame,
    prices: pd.DataFrame,
) -> pd.DataFrame:
    merged = sales.merge(
        prices,
        on="product_id",
        how="left",
    )

    if merged["unit_price"].isna().any():
        missing_products = (
            merged.loc[merged["unit_price"].isna(), "product_id"]
            .drop_duplicates()
            .tolist()
        )
        raise ValueError(
            f"Missing price information for products: {missing_products}"
        )

    merged["revenue"] = merged["quantity"] * merged["unit_price"]
    merged["month"] = (
        merged["sale_date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_revenue = (
        merged.groupby("month", as_index=False)["revenue"]
        .sum()
        .sort_values("month")
        .reset_index(drop=True)
    )

    monthly_revenue["revenue"] = monthly_revenue["revenue"].round(2)
    return monthly_revenue


def save_report(report: pd.DataFrame) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "monthly_revenue.csv"
    report.to_csv(output_file, index=False)

    return output_file


def main() -> None:
    raw_sales = load_csv("sales.csv")
    raw_prices = load_csv("product_prices.csv")

    sales = normalize_sales(raw_sales)
    prices = normalize_prices(raw_prices)

    monthly_revenue = create_monthly_revenue(sales, prices)
    output_file = save_report(monthly_revenue)

    print(f"Monthly revenue report written to: {output_file}")


if __name__ == "__main__":
    main()
