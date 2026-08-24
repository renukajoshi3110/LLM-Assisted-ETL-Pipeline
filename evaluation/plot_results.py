# ============================================================
# ETL EXPERIMENT RESULTS VISUALIZATION
# ============================================================
#
# Creates charts from analysis_summary.csv and
# experiment_results.csv.
#
# Charts:
# 1. Manual vs LLM ETL execution time
# 2. LLM generation time
# 3. Manual vs LLM total time
# 4. Development effort
# 5. Data quality match rate
#
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt


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

EXPERIMENT_RESULTS_PATH = os.path.join(
    RESULTS_DIR,
    "experiment_results.csv"
)

CHARTS_DIR = os.path.join(
    RESULTS_DIR,
    "charts"
)


# ============================================================
# CHECK INPUT FILE
# ============================================================

if not os.path.exists(
    EXPERIMENT_RESULTS_PATH
):

    raise FileNotFoundError(
        "experiment_results.csv not found:\n"
        f"{EXPERIMENT_RESULTS_PATH}"
    )


# ============================================================
# CREATE CHART DIRECTORY
# ============================================================

os.makedirs(
    CHARTS_DIR,
    exist_ok=True
)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(
    EXPERIMENT_RESULTS_PATH
)


# ============================================================
# CREATE SHORT TEST CASE LABELS
# ============================================================

labels = [
    "Order Items + Products",
    "Orders + Customers",
    "Payments"
]


# ============================================================
# CHART 1
# MANUAL VS LLM ETL EXECUTION TIME
# ============================================================

plt.figure(
    figsize=(10, 6)
)

x = range(
    len(df)
)

width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    df[
        "manual_execution_time_seconds"
    ],
    width=width,
    label="Manual ETL"
)

plt.bar(
    [i + width / 2 for i in x],
    df[
        "llm_execution_time_seconds"
    ],
    width=width,
    label="LLM ETL"
)

plt.xticks(
    list(x),
    labels
)

plt.ylabel(
    "Execution Time (seconds)"
)

plt.title(
    "Manual vs LLM-Assisted ETL Execution Time"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_DIR,
        "execution_time_comparison.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 2
# LLM GENERATION TIME
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    labels,
    df[
        "llm_generation_time_seconds"
    ]
)

plt.ylabel(
    "Generation Time (seconds)"
)

plt.title(
    "LLM Pipeline Generation Time"
)

plt.xticks(
    rotation=15
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_DIR,
        "llm_generation_time.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 3
# MANUAL VS LLM TOTAL TIME
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    [i - width / 2 for i in x],
    df[
        "manual_execution_time_seconds"
    ],
    width=width,
    label="Manual ETL"
)

plt.bar(
    [i + width / 2 for i in x],
    df[
        "llm_total_time_seconds"
    ],
    width=width,
    label="LLM Total"
)

plt.xticks(
    list(x),
    labels
)

plt.ylabel(
    "Total Time (seconds)"
)

plt.title(
    "Manual ETL vs LLM-Assisted Total Time"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_DIR,
        "total_time_comparison.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 4
# DEVELOPMENT EFFORT
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    [i - width / 2 for i in x],
    df[
        "manual_code_lines"
    ],
    width=width,
    label="Manual Code Lines"
)

plt.bar(
    [i + width / 2 for i in x],
    df[
        "llm_pipeline_steps"
    ],
    width=width,
    label="LLM Workflow Steps"
)

plt.xticks(
    list(x),
    labels
)

plt.ylabel(
    "Count"
)

plt.title(
    "Manual Implementation Lines vs LLM Workflow Steps"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_DIR,
        "development_effort_comparison.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 5
# DATA QUALITY MATCH RATE
# ============================================================

quality_metrics = {
    "Rows": (
        (
            df["manual_rows"]
            == df["llm_rows"]
        ).mean()
        * 100
    ),

    "Columns": (
        (
            df["manual_columns"]
            == df["llm_columns"]
        ).mean()
        * 100
    ),

    "Missing Values": (
        (
            df["manual_missing_values"]
            == df["llm_missing_values"]
        ).mean()
        * 100
    ),

    "Duplicates": (
        (
            df["manual_duplicates"]
            == df["llm_duplicates"]
        ).mean()
        * 100
    )
}


plt.figure(
    figsize=(10, 6)
)

plt.bar(
    list(
        quality_metrics.keys()
    ),
    list(
        quality_metrics.values()
    )
)

plt.ylabel(
    "Match Rate (%)"
)

plt.ylim(
    0,
    110
)

plt.title(
    "Data Quality Agreement Between Manual and LLM ETL"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_DIR,
        "data_quality_match_rate.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# FINAL MESSAGE
# ============================================================

print("=" * 60)
print("ETL RESULTS VISUALIZATION")
print("=" * 60)

print(
    f"\nCharts saved to:"
)

print(
    CHARTS_DIR
)

print(
    "\nGenerated charts:"
)

print(
    "1. execution_time_comparison.png"
)

print(
    "2. llm_generation_time.png"
)

print(
    "3. total_time_comparison.png"
)

print(
    "4. development_effort_comparison.png"
)

print(
    "5. data_quality_match_rate.png"
)

print(
    "\nVisualization completed successfully."
)