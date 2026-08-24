# ============================================================
# MANUAL ETL PIPELINE
# EXPERIMENT 3 - PAYMENTS
# ============================================================

import os
import time
import pandas as pd


# ============================================================
# PROJECT PATHS
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
    "raw",
    "olist_order_payments_dataset.csv"
)

OUTPUT_DIR = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed"
)

OUTPUT_PATH = os.path.join(
    OUTPUT_DIR,
    "manual_payments.csv"
)


# ============================================================
# START TIMER
# ============================================================

start_time = time.perf_counter()


print("=" * 60)
print("MANUAL ETL PIPELINE")
print("EXPERIMENT 3 - PAYMENTS")
print("=" * 60)


# ============================================================
# STEP 1: EXTRACT
# ============================================================

print("\nStep 1: EXTRACT")

if not os.path.exists(RAW_PATH):

    raise FileNotFoundError(
        f"Payments dataset not found:\n{RAW_PATH}"
    )

df = pd.read_csv(RAW_PATH)

print(
    f"payments loaded: {len(df)} rows"
)


# ============================================================
# STEP 2: CLEAN
# ============================================================

print("\nStep 2: CLEAN payments")

missing_before = int(
    df.isnull().sum().sum()
)

duplicates_before = int(
    df.duplicated().sum()
)


print(
    f"Missing values before: "
    f"{missing_before}"
)

print(
    f"Duplicates before: "
    f"{duplicates_before}"
)


# Remove duplicates

df = df.drop_duplicates()


# Handle missing values

for column in df.columns:

    if df[column].isnull().any():

        if pd.api.types.is_numeric_dtype(
            df[column]
        ):

            median_value = df[column].median()

            if pd.isna(median_value):

                median_value = 0

            df[column] = df[column].fillna(
                median_value
            )

        else:

            df[column] = df[column].fillna("")


print(
    f"Rows after cleaning: "
    f"{len(df)}"
)


# ============================================================
# STEP 3: TRANSFORM
# ============================================================

print("\nStep 3: TRANSFORM payments")

print(
    "Converting payment-related numeric "
    "columns to appropriate numeric types."
)


numeric_columns = [
    "payment_sequential",
    "payment_installments",
    "payment_value"
]


for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# There is no payment-date column in the
# Olist payments dataset, so no date
# conversion is performed.


print(
    "Transformation completed."
)


# ============================================================
# STEP 4: STORE
# ============================================================

print("\nStep 4: STORE")

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print(
    "Output saved to:"
)

print(
    OUTPUT_PATH
)

print(
    f"Rows    : {df.shape[0]}"
)

print(
    f"Columns : {df.shape[1]}"
)


# ============================================================
# STEP 5: VALIDATION
# ============================================================

print("\nStep 5: VALIDATION")

final_rows = df.shape[0]

final_columns = df.shape[1]

missing_values = int(
    df.isnull().sum().sum()
)

duplicate_rows = int(
    df.duplicated().sum()
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
    f"{missing_values}"
)

print(
    f"Duplicate rows: "
    f"{duplicate_rows}"
)


# ============================================================
# COMPLETION
# ============================================================

execution_time = (
    time.perf_counter()
    - start_time
)


print("\n")
print("=" * 60)
print("MANUAL ETL COMPLETED")
print("=" * 60)

print(
    f"\nExecution time: "
    f"{execution_time:.4f} seconds"
)

print(
    "\nPipeline completed successfully."
)