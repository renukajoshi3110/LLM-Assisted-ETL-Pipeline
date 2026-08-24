# ============================================================
# MANUAL ETL PIPELINE
# EXPERIMENT 2 - ORDERS + CUSTOMERS
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
print("EXPERIMENT 2 - ORDERS + CUSTOMERS")
print("=" * 60)


# ============================================================
# STEP 1 - EXTRACT
# ============================================================

print("\nStep 1: EXTRACT")

orders_path = os.path.join(
    RAW_PATH,
    "olist_orders_dataset.csv"
)

customers_path = os.path.join(
    RAW_PATH,
    "olist_customers_dataset.csv"
)

orders = pd.read_csv(
    orders_path
)

customers = pd.read_csv(
    customers_path
)

print(
    f"orders loaded: "
    f"{len(orders)} rows"
)

print(
    f"customers loaded: "
    f"{len(customers)} rows"
)


# ============================================================
# STEP 2 - CLEAN ORDERS
# ============================================================

print("\nStep 2: CLEAN orders")

orders_missing_before = int(
    orders.isna().sum().sum()
)

orders_duplicates_before = int(
    orders.duplicated().sum()
)

orders = orders.drop_duplicates()

orders = orders.ffill()

orders = orders.dropna()

print(
    f"Missing values before: "
    f"{orders_missing_before}"
)

print(
    f"Duplicates before: "
    f"{orders_duplicates_before}"
)

print(
    f"Rows after cleaning: "
    f"{len(orders)}"
)


# ============================================================
# STEP 3 - CLEAN CUSTOMERS
# ============================================================

print("\nStep 3: CLEAN customers")

customers_missing_before = int(
    customers.isna().sum().sum()
)

customers_duplicates_before = int(
    customers.duplicated().sum()
)

customers = customers.drop_duplicates()

customers = customers.ffill()

customers = customers.dropna()

print(
    f"Missing values before: "
    f"{customers_missing_before}"
)

print(
    f"Duplicates before: "
    f"{customers_duplicates_before}"
)

print(
    f"Rows after cleaning: "
    f"{len(customers)}"
)


# ============================================================
# STEP 4 - JOIN
# ============================================================

print("\nStep 4: JOIN")

orders["customer_id"] = (
    orders["customer_id"].astype(str)
)

customers["customer_id"] = (
    customers["customer_id"].astype(str)
)

result = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="left",
    suffixes=(
        "_orders",
        "_customers"
    )
)

print(
    "Joined orders + customers"
)

print(
    "Join key: customer_id"
)

print(
    f"Result rows: "
    f"{len(result)}"
)

print(
    f"Result columns: "
    f"{len(result.columns)}"
)


# ============================================================
# STEP 5 - STORE
# ============================================================

print("\nStep 5: STORE")

output_path = os.path.join(
    PROCESSED_PATH,
    "manual_orders_customers.csv"
)

result.to_csv(
    output_path,
    index=False
)

print(
    f"Output saved to:\n"
    f"{output_path}"
)


# ============================================================
# STEP 6 - VALIDATION
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
    f"Final rows: "
    f"{final_rows}"
)

print(
    f"Final columns: "
    f"{final_columns}"
)

print(
    f"Missing values: "
    f"{final_missing}"
)

print(
    f"Duplicate rows: "
    f"{final_duplicates}"
)


# ============================================================
# EXECUTION TIME
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