# ============================================================
# LLM-ASSISTED ETL PIPELINE GENERATION PROMPTS
# ============================================================

PIPELINE_GENERATION_PROMPT = """
You are an expert Data Engineer.

Your task is to design an ETL pipeline based on the user's request.

The project contains the following available datasets:

- customers
- orders
- order_items
- payments
- products

The ETL pipeline should follow these stages:

1. EXTRACT
   Load the required datasets.

2. TRANSFORM
   Clean missing values.
   Remove duplicates.
   Convert data types when necessary.
   Join datasets when requested.
   Apply the transformations requested by the user.

3. LOAD
   Save the final processed data as a CSV file.

4. VALIDATION
   Report:
   - number of rows
   - number of columns
   - missing values
   - duplicate rows
   - successful completion

IMPORTANT:
Return ONLY valid JSON.

Do NOT use Markdown.
Do NOT use ```json.
Do NOT write explanations outside the JSON.
Do NOT add comments inside the JSON.

The JSON must contain exactly these fields:

{{
    "pipeline_name": "Short name of the pipeline",

    "description": "Short description of the pipeline",

    "datasets": [
        "dataset_name"
    ],

    "steps": [
        {{
            "step_number": 1,
            "operation": "LOAD",
            "dataset": "dataset_name",
            "details": "Load the required dataset."
        }},
        {{
            "step_number": 2,
            "operation": "CLEAN",
            "dataset": "dataset_name",
            "details": "Clean missing values and remove duplicate records."
        }},
        {{
            "step_number": 3,
            "operation": "TRANSFORM",
            "dataset": "dataset_name",
            "details": "Apply the required data type conversions and transformations."
        }},
        {{
            "step_number": 4,
            "operation": "JOIN",
            "dataset": "dataset_name",
            "join_with": "dataset_name",
            "join_key": "customer_id",
            "details": "Join the datasets using the required key."
        }},
        {{
            "step_number": 5,
            "operation": "STORE",
            "dataset": "final_result",
            "details": "Save the final processed dataset as a CSV file."
        }}
    ],

    "extract": [
        "Step describing data extraction"
    ],

    "transform": [
        "Step describing data transformation"
    ],

    "load": [
        "Step describing data loading"
    ],

    "validation": [
        "Step describing validation"
    ],

    "python_implementation_plan": [
        "Step-by-step Python implementation instruction"
    ]
}}

RULES FOR STEPS:

- Every item in "steps" MUST be a JSON object.
- Every step MUST contain:
  "step_number"
  "operation"
  "dataset"
  "details"

- The "operation" value MUST be exactly one of:
  "LOAD"
  "CLEAN"
  "TRANSFORM"
  "JOIN"
  "STORE"

- Do NOT use "EXTRACT" as an operation.
  Use "LOAD" for extracting/loading a dataset.

- Do NOT use "SAVE" as an operation.
  Use "STORE".

- Do NOT use "ACTION" as a field.
  Use "operation".

- For JOIN steps, ALWAYS include:
  "join_with"
  "join_key"

- For JOIN between orders and customers, use:
  "dataset": "orders"
  "join_with": "customers"
  "join_key": "customer_id"

- For STORE, use:
  "operation": "STORE"

- Only use datasets from:
  customers, orders, order_items, payments, products

- Do not invent dataset names.

- Use pandas for Python implementation.

- Keep the pipeline focused on the user's request.

- Make the steps specific to the user's request.

- If the user requests orders and customers, the steps should load,
  clean, transform, join, and store those datasets.

- Every generated pipeline MUST include a final VALIDATION step.
- The VALIDATION step must always be the last step.
- The VALIDATION step must use:
  "operation": "VALIDATION"
  "dataset": "final_result"
  "details": "Validate rows, columns, missing values, duplicate rows, and successful completion."

USER REQUEST:
{user_request}
"""


def build_pipeline_prompt(user_request):
    """
    Build the prompt used for ETL pipeline generation.
    """

    return PIPELINE_GENERATION_PROMPT.format(
        user_request=user_request
    )


# ============================================================
# ETL EXPLANATION PROMPT
# ============================================================

ETL_EXPLANATION_PROMPT = """
You are an expert Data Engineer.

Explain the following ETL pipeline.

Cover:

1. Extract
2. Transform
3. Load
4. Data Quality
5. Validation
6. Final Output

Pipeline:
{pipeline}

Keep the explanation clear and professional.
"""


def build_etl_explanation_prompt(pipeline):
    """
    Build a prompt for explaining an ETL pipeline.
    """

    return ETL_EXPLANATION_PROMPT.format(
        pipeline=pipeline
    )


# ============================================================
# DATA QUALITY PROMPT
# ============================================================

DATA_QUALITY_PROMPT = """
You are a Data Quality Engineer.

Analyze the following ETL data quality report.

Explain:

1. Number of rows
2. Number of columns
3. Missing values
4. Duplicate records
5. Potential data quality problems
6. Whether the data is ready for analysis

Data Quality Report:
{data_quality_report}

Give a concise professional assessment.
"""


def build_data_quality_prompt(data_quality_report):
    """
    Build a prompt for data quality analysis.
    """

    return DATA_QUALITY_PROMPT.format(
        data_quality_report=data_quality_report
    )