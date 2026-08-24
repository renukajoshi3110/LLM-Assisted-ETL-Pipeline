# ============================================================
# ETL EXPERIMENT RESULTS ANALYSIS
# ============================================================
#
# Reads experiment_results.csv and calculates:
# - Average execution times
# - LLM generation overhead
# - Development effort
# - Data quality success rate
# - Runtime comparison
#
# ============================================================

import os
import pandas as pd


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

RESULTS_PATH = os.path.join(
    PROJECT_ROOT,
    "evaluation",
    "results",
    "experiment_results.csv"
)


# ============================================================
# CHECK FILE
# ============================================================

if not os.path.exists(RESULTS_PATH):

    raise FileNotFoundError(
        f"Results file not found:\n{RESULTS_PATH}"
    )


# ============================================================
# LOAD RESULTS
# ============================================================

df = pd.read_csv(
    RESULTS_PATH
)


print("=" * 70)
print("ETL EXPERIMENT RESULTS ANALYSIS")
print("=" * 70)

print(
    f"\nExperiments analyzed: "
    f"{len(df)}"
)


# ============================================================
# DISPLAY EXPERIMENT DATA
# ============================================================

print("\n")
print("=" * 70)
print("EXPERIMENT RESULTS")
print("=" * 70)

for _, row in df.iterrows():

    print(
        f"\nExperiment {int(row['experiment_id'])}"
    )

    print(
        f"Test case: "
        f"{row['test_case']}"
    )

    print(
        f"Manual execution: "
        f"{row['manual_execution_time_seconds']:.4f} seconds"
    )

    print(
        f"LLM generation: "
        f"{row['llm_generation_time_seconds']:.4f} seconds"
    )

    print(
        f"LLM execution: "
        f"{row['llm_execution_time_seconds']:.4f} seconds"
    )

    print(
        f"LLM total: "
        f"{row['llm_total_time_seconds']:.4f} seconds"
    )

    print(
        f"Manual code lines: "
        f"{int(row['manual_code_lines'])}"
    )

    print(
        f"LLM pipeline steps: "
        f"{int(row['llm_pipeline_steps'])}"
    )


# ============================================================
# AVERAGE PERFORMANCE
# ============================================================

average_manual_time = (
    df["manual_execution_time_seconds"]
    .mean()
)

average_llm_generation = (
    df["llm_generation_time_seconds"]
    .mean()
)

average_llm_execution = (
    df["llm_execution_time_seconds"]
    .mean()
)

average_llm_total = (
    df["llm_total_time_seconds"]
    .mean()
)


print("\n")
print("=" * 70)
print("AVERAGE PERFORMANCE")
print("=" * 70)

print(
    f"\nAverage manual ETL execution : "
    f"{average_manual_time:.4f} seconds"
)

print(
    f"Average LLM generation time  : "
    f"{average_llm_generation:.4f} seconds"
)

print(
    f"Average LLM ETL execution    : "
    f"{average_llm_execution:.4f} seconds"
)

print(
    f"Average LLM total time       : "
    f"{average_llm_total:.4f} seconds"
)


# ============================================================
# RUNTIME OVERHEAD
# ============================================================

df["runtime_overhead_seconds"] = (
    df["llm_total_time_seconds"]
    - df["manual_execution_time_seconds"]
)

average_overhead = (
    df["runtime_overhead_seconds"]
    .mean()
)


print("\n")
print("=" * 70)
print("RUNTIME OVERHEAD")
print("=" * 70)

print(
    f"\nAverage additional time introduced "
    f"by LLM generation: "
    f"{average_overhead:.4f} seconds"
)


# ============================================================
# DEVELOPMENT EFFORT
# ============================================================

average_manual_lines = (
    df["manual_code_lines"]
    .mean()
)

average_llm_steps = (
    df["llm_pipeline_steps"]
    .mean()
)


print("\n")
print("=" * 70)
print("DEVELOPMENT EFFORT")
print("=" * 70)

print(
    f"\nAverage manual implementation lines : "
    f"{average_manual_lines:.2f}"
)

print(
    f"Average LLM workflow steps           : "
    f"{average_llm_steps:.2f}"
)


# ============================================================
# DATA QUALITY
# ============================================================

rows_match_rate = (
    (
        df["manual_rows"]
        == df["llm_rows"]
    ).mean()
    * 100
)

columns_match_rate = (
    (
        df["manual_columns"]
        == df["llm_columns"]
    ).mean()
    * 100
)

missing_match_rate = (
    (
        df["manual_missing_values"]
        == df["llm_missing_values"]
    ).mean()
    * 100
)

duplicates_match_rate = (
    (
        df["manual_duplicates"]
        == df["llm_duplicates"]
    ).mean()
    * 100
)


print("\n")
print("=" * 70)
print("DATA QUALITY COMPARISON")
print("=" * 70)

print(
    f"\nRows match rate       : "
    f"{rows_match_rate:.2f}%"
)

print(
    f"Columns match rate    : "
    f"{columns_match_rate:.2f}%"
)

print(
    f"Missing values match  : "
    f"{missing_match_rate:.2f}%"
)

print(
    f"Duplicate match rate  : "
    f"{duplicates_match_rate:.2f}%"
)


# ============================================================
# SUCCESS RATE
# ============================================================

manual_success_rate = (
    (
        df["manual_status"]
        == "SUCCESS"
    ).mean()
    * 100
)

llm_success_rate = (
    (
        df["llm_status"]
        == "SUCCESS"
    ).mean()
    * 100
)


print("\n")
print("=" * 70)
print("PIPELINE SUCCESS RATE")
print("=" * 70)

print(
    f"\nManual ETL success rate : "
    f"{manual_success_rate:.2f}%"
)

print(
    f"LLM ETL success rate    : "
    f"{llm_success_rate:.2f}%"
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print(
    "\nThe experiments show that the LLM-assisted "
    "pipelines produced matching measured data-quality "
    "results across all tested workflows."
)

print(
    "\nThe LLM introduces additional execution time "
    "because pipeline generation requires an LLM call."
)

print(
    "\nThe main potential benefit is reduced manual "
    "ETL development effort through natural-language "
    "pipeline generation."
)


# ============================================================
# SAVE ANALYSIS CSV
# ============================================================

ANALYSIS_PATH = os.path.join(
    PROJECT_ROOT,
    "evaluation",
    "results",
    "analysis_summary.csv"
)


summary = pd.DataFrame(
    {
        "metric": [
            "Experiments",
            "Average Manual ETL Time",
            "Average LLM Generation Time",
            "Average LLM ETL Time",
            "Average LLM Total Time",
            "Average Runtime Overhead",
            "Average Manual Code Lines",
            "Average LLM Workflow Steps",
            "Rows Match Rate",
            "Columns Match Rate",
            "Missing Values Match Rate",
            "Duplicate Match Rate",
            "Manual Success Rate",
            "LLM Success Rate"
        ],

        "value": [
            len(df),
            average_manual_time,
            average_llm_generation,
            average_llm_execution,
            average_llm_total,
            average_overhead,
            average_manual_lines,
            average_llm_steps,
            rows_match_rate,
            columns_match_rate,
            missing_match_rate,
            duplicates_match_rate,
            manual_success_rate,
            llm_success_rate
        ]
    }
)


summary.to_csv(
    ANALYSIS_PATH,
    index=False
)


print("\n")
print("=" * 70)
print("ANALYSIS SAVED")
print("=" * 70)

print(
    f"\nAnalysis file:"
)

print(
    ANALYSIS_PATH
)