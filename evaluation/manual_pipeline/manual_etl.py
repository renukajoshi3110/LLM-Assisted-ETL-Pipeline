# ============================================================
# MANUAL ETL PIPELINE
# Baseline for comparison with LLM-assisted ETL
# ============================================================

import os
import time
import pandas as pd


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

RAW_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw"
)

PROCESSED_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed"
)

os.makedirs(
    PROCESSED_PATH,
    exist_ok=True
)


# ============================================================
# START TIMER
# ============================================================

start_time = time.perf_counter()


print("=" * 60)
print("MANUAL ETL PIPELINE")
print("=" * 60)


# ============================================================
# STEP 1 — EXTRACT
# ============================================================

print("\nStep 1: EXTRACT")

order_items_path = os.path.join(
    RAW_PATH,
    "olist_order_items_dataset.csv"
)

products_path = os.path.join(
    RAW_PATH,
    "olist_products_dataset.csv"
)

order_items = pd.read_csv(
    order_items_path
)

products = pd.read_csv(
    products_path
)

print(
    f"order_items loaded: "
    f"{len(order_items)} rows"
)

print(
    f"products loaded: "
    f"{len(products)} rows"
)


# ============================================================
# STEP 2 — CLEAN ORDER ITEMS
# ============================================================

print("\nStep 2: CLEAN order_items")

order_items_missing_before = int(
    order_items.isna().sum().sum()
)

order_items_duplicates_before = int(
    order_items.duplicated().sum()
)

order_items = order_items.drop_duplicates()

order_items = order_items.ffill()

order_items = order_items.dropna()

print(
    f"Missing values before: "
    f"{order_items_missing_before}"
)

print(
    f"Duplicates before: "
    f"{order_items_duplicates_before}"
)

print(
    f"Rows after cleaning: "
    f"{len(order_items)}"
)


# ============================================================
# STEP 3 — CLEAN PRODUCTS
# ============================================================

print("\nStep 3: CLEAN products")

products_missing_before = int(
    products.isna().sum().sum()
)

products_duplicates_before = int(
    products.duplicated().sum()
)

products = products.drop_duplicates()

products = products.ffill()

products = products.dropna()

print(
    f"Missing values before: "
    f"{products_missing_before}"
)

print(
    f"Duplicates before: "
    f"{products_duplicates_before}"
)

print(
    f"Rows after cleaning: "
    f"{len(products)}"
)


# ============================================================
# STEP 4 — JOIN
# ============================================================

print("\nStep 4: JOIN")

order_items["product_id"] = (
    order_items["product_id"].astype(str)
)

products["product_id"] = (
    products["product_id"].astype(str)
)

result = pd.merge(
    order_items,
    products,
    on="product_id",
    how="left",
    suffixes=(
        "_order_items",
        "_products"
    )
)

print(
    "Joined order_items + products"
)

print(
    f"Join key: product_id"
)

print(
    f"Result rows: {len(result)}"
)

print(
    f"Result columns: {len(result.columns)}"
)


# ============================================================
# STEP 5 — STORE
# ============================================================

print("\nStep 5: STORE")

output_path = os.path.join(
    PROCESSED_PATH,
    "manual_order_items_products.csv"
)

result.to_csv(
    output_path,
    index=False
)

print(
    f"Output saved to:\n{output_path}"
)


# ============================================================
# STEP 6 — VALIDATION
# ============================================================

print("\nStep 6: VALIDATION")

final_rows = len(result)

final_columns = len(
    result.columns
)

final_missing = int(
    result.isna().sum().sum()
)

final_duplicates = int(
    result.duplicated().sum()
)

print(
    f"Final rows: {final_rows}"
)

print(
    f"Final columns: {final_columns}"
)

print(
    f"Missing values: {final_missing}"
)

print(
    f"Duplicate rows: {final_duplicates}"
)


# ============================================================
# END TIMER
# ============================================================

end_time = time.perf_counter()

execution_time = (
    end_time - start_time
)

print("\n" + "=" * 60)
print("MANUAL ETL COMPLETED")
print("=" * 60)

print(
    f"\nExecution time: "
    f"{execution_time:.4f} seconds"
)

print(
    "\nPipeline completed successfully."
)