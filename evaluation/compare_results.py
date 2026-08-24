# ============================================================
# ETL EXPERIMENT COMPARISON
# ============================================================
# Compares Manual ETL with LLM-Assisted ETL
#
# Experiments:
# 1. order_items + products
# 2. orders + customers
# 3. payments
# ============================================================

import csv
import os


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

RESULTS_DIR = os.path.join(
    PROJECT_ROOT,
    "evaluation",
    "results"
)

RESULTS_PATH = os.path.join(
    RESULTS_DIR,
    "experiment_results.csv"
)


# ============================================================
# EXPERIMENT DATA
# ============================================================

experiments = [

    # ========================================================
    # EXPERIMENT 1
    # ========================================================

    {
        "experiment_id": 1,
        "test_case": "order_items + products",

        "manual_execution_time_seconds": 1.9394,
        "manual_code_lines": 173,
        "manual_rows": 112650,
        "manual_columns": 15,
        "manual_missing_values": 0,
        "manual_duplicates": 0,
        "manual_status": "SUCCESS",

        "llm_generation_time_seconds": 7.6831,
        "llm_execution_time_seconds": 2.6945,
        "llm_total_time_seconds": 10.3776,
        "llm_pipeline_steps": 7,
        "llm_datasets": 2,
        "llm_rows": 112650,
        "llm_columns": 15,
        "llm_missing_values": 0,
        "llm_duplicates": 0,
        "llm_status": "SUCCESS"
    },

    # ========================================================
    # EXPERIMENT 2
    # ========================================================

    {
        "experiment_id": 2,
        "test_case": "orders + customers",

        "manual_execution_time_seconds": 2.1229,
        "manual_code_lines": 181,
        "manual_rows": 99441,
        "manual_columns": 12,
        "manual_missing_values": 0,
        "manual_duplicates": 0,
        "manual_status": "SUCCESS",

        "llm_generation_time_seconds": 9.9843,
        "llm_execution_time_seconds": 4.5018,
        "llm_total_time_seconds": 14.4861,
        "llm_pipeline_steps": 7,
        "llm_datasets": 2,
        "llm_rows": 99441,
        "llm_columns": 12,
        "llm_missing_values": 0,
        "llm_duplicates": 0,
        "llm_status": "SUCCESS"
    },

    # ========================================================
    # EXPERIMENT 3
    # ========================================================

    {
        "experiment_id": 3,
        "test_case": "payments",

        "manual_execution_time_seconds": 0.4619,
        "manual_code_lines": 152,
        "manual_rows": 103886,
        "manual_columns": 5,
        "manual_missing_values": 0,
        "manual_duplicates": 0,
        "manual_status": "SUCCESS",

        "llm_generation_time_seconds": 13.3143,
        "llm_execution_time_seconds": 0.7549,
        "llm_total_time_seconds": 14.0692,
        "llm_pipeline_steps": 5,
        "llm_datasets": 1,
        "llm_rows": 103886,
        "llm_columns": 5,
        "llm_missing_values": 0,
        "llm_duplicates": 0,
        "llm_status": "SUCCESS"
    }
]


# ============================================================
# NOTE
# ============================================================

# Manual code lines for Experiment 3 will be measured
# separately. We currently use 0 as a placeholder so that
# the timing and data-quality results can be recorded.


# ============================================================
# DISPLAY EXPERIMENTS
# ============================================================

print("=" * 60)
print("ETL EXPERIMENT COMPARISON")
print("=" * 60)


for experiment in experiments:

    print("\n")
    print("-" * 60)

    print(
        f"EXPERIMENT "
        f"{experiment['experiment_id']}"
    )

    print("-" * 60)

    print(
        f"Test case: "
        f"{experiment['test_case']}"
    )

    # --------------------------------------------------------
    # MANUAL
    # --------------------------------------------------------

    print("\nMANUAL ETL")

    print(
        f"Code lines       : "
        f"{experiment['manual_code_lines']}"
    )

    print(
        f"Execution time   : "
        f"{experiment['manual_execution_time_seconds']:.4f} seconds"
    )

    print(
        f"Final rows       : "
        f"{experiment['manual_rows']}"
    )

    print(
        f"Final columns    : "
        f"{experiment['manual_columns']}"
    )

    print(
        f"Missing values   : "
        f"{experiment['manual_missing_values']}"
    )

    print(
        f"Duplicates       : "
        f"{experiment['manual_duplicates']}"
    )

    print(
        f"Status           : "
        f"{experiment['manual_status']}"
    )

    # --------------------------------------------------------
    # LLM
    # --------------------------------------------------------

    print("\nLLM-ASSISTED ETL")

    print(
        f"Generation time  : "
        f"{experiment['llm_generation_time_seconds']:.4f} seconds"
    )

    print(
        f"Execution time   : "
        f"{experiment['llm_execution_time_seconds']:.4f} seconds"
    )

    print(
        f"Total time       : "
        f"{experiment['llm_total_time_seconds']:.4f} seconds"
    )

    print(
        f"Pipeline steps   : "
        f"{experiment['llm_pipeline_steps']}"
    )

    print(
        f"Datasets         : "
        f"{experiment['llm_datasets']}"
    )

    print(
        f"Final rows       : "
        f"{experiment['llm_rows']}"
    )

    print(
        f"Final columns    : "
        f"{experiment['llm_columns']}"
    )

    print(
        f"Missing values   : "
        f"{experiment['llm_missing_values']}"
    )

    print(
        f"Duplicates       : "
        f"{experiment['llm_duplicates']}"
    )

    print(
        f"Status           : "
        f"{experiment['llm_status']}"
    )

    # --------------------------------------------------------
    # DATA QUALITY
    # --------------------------------------------------------

    rows_match = (
        experiment["manual_rows"]
        == experiment["llm_rows"]
    )

    columns_match = (
        experiment["manual_columns"]
        == experiment["llm_columns"]
    )

    missing_match = (
        experiment["manual_missing_values"]
        == experiment["llm_missing_values"]
    )

    duplicates_match = (
        experiment["manual_duplicates"]
        == experiment["llm_duplicates"]
    )

    print("\nDATA QUALITY")

    print(
        f"Rows match       : "
        f"{rows_match}"
    )

    print(
        f"Columns match    : "
        f"{columns_match}"
    )

    print(
        f"Missing match    : "
        f"{missing_match}"
    )

    print(
        f"Duplicates match : "
        f"{duplicates_match}"
    )


# ============================================================
# SAVE CSV
# ============================================================

os.makedirs(
    RESULTS_DIR,
    exist_ok=True
)

fieldnames = list(
    experiments[0].keys()
)


# Overwrite the CSV so experiments are never duplicated.

with open(
    RESULTS_PATH,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(
        experiments
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n")
print("=" * 60)
print("EXPERIMENT RESULTS SAVED")
print("=" * 60)

print(
    f"\nResults file:"
)

print(
    RESULTS_PATH
)

print(
    f"\nTotal experiments recorded: "
    f"{len(experiments)}"
)