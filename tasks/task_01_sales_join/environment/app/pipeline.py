from pathlib import Path
import pandas as pd


APP_DIR = Path("/app")
DATA_DIR = APP_DIR / "data"
OUTPUT_DIR = APP_DIR / "output"


def load_sales() -> pd.DataFrame:
    sales = pd.read_csv(DATA_DIR / "sales.csv")
    sales["sale_date"] = pd.to_datetime(sales["sale_date"])
    sales["quantity"] = pd.to_numeric(sales["quantity"])
    return sales


def load_prices() -> pd.DataFrame:
    prices = pd.read_csv(DATA_DIR / "product_prices.csv")
    prices["unit_price"] = pd.to_numeric(prices["unit_price"])
    return prices


def create_monthly_revenue(
    sales: pd.DataFrame, prices: pd.DataFrame
) -> pd.DataFrame:
    merged = sales.merge(
        prices,
        on="product_id",
        how="left",
    )

    merged["revenue"] = merged["quantity"] * merged["unit_price"]
    merged["month"] = merged["sale_date"].dt.to_period("M").astype(str)

    report = (
        merged.groupby("month", as_index=False)["revenue"]
        .sum()
        .sort_values("month")
    )

    return report


def save_report(report: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT_DIR / "monthly_revenue.csv", index=False)


def main() -> None:
    sales = load_sales()
    prices = load_prices()
    report = create_monthly_revenue(sales, prices)
    save_report(report)


if __name__ == "__main__":
    main()
