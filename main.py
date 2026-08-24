# ============================================================
# ADVANCED PROJECT
# LLM-ASSISTED ETL PIPELINE GENERATION
# ============================================================

import time

from llm_agent.pipeline_generator import PipelineGenerator
from llm_agent.executor import ETLExecutor


def main():

    print("\n")
    print("=" * 60)
    print("ADVANCED PROJECT")
    print("LLM-ASSISTED ETL PIPELINE GENERATION")
    print("=" * 60)

    print("\nAvailable datasets:")
    print("1. customers")
    print("2. orders")
    print("3. order_items")
    print("4. payments")
    print("5. products")

    print("\n")
    print("Describe the ETL pipeline you want.")
    print("Example:")
    print(
        "Load orders, clean missing values, "
        "join with customers, and store the result."
    )

    print("\n")

    # --------------------------------------------------------
    # STEP 1: Get user's natural-language request
    # --------------------------------------------------------

    user_request = input(
        "Your pipeline request:\n\n"
    )

    if not user_request.strip():

        print(
            "\nNo pipeline request was provided."
        )

        return

    # --------------------------------------------------------
    # STEP 2: Send request to Gemini
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("GENERATING PIPELINE USING GEMINI")
    print("=" * 60)

    generator = PipelineGenerator()

    # Start timer for LLM generation
    llm_start_time = time.perf_counter()

    pipeline = generator.generate_pipeline(
        user_request
    )

    # Stop timer for LLM generation
    llm_end_time = time.perf_counter()

    llm_generation_time = (
        llm_end_time - llm_start_time
    )

    # --------------------------------------------------------
    # STEP 3: Check generated pipeline
    # --------------------------------------------------------

    if pipeline is None:

        print(
            "\nPipeline generation failed."
        )

        return

    print(
        f"\nLLM Generation Time: "
        f"{llm_generation_time:.4f} seconds"
    )

    # --------------------------------------------------------
    # STEP 4: Display generated pipeline
    # --------------------------------------------------------

    generator.display_pipeline(
        pipeline
    )

    # --------------------------------------------------------
    # STEP 5: Ask user for confirmation
    # --------------------------------------------------------

    print("\n")

    confirmation = input(
        "Do you want to execute this pipeline? "
        "(yes/no): "
    )

    if confirmation.lower().strip() not in [
        "yes",
        "y"
    ]:

        print(
            "\nPipeline execution cancelled."
        )

        return

    # --------------------------------------------------------
    # STEP 6: Execute generated pipeline
    # --------------------------------------------------------

    executor = ETLExecutor()

    # Start ETL execution timer
    etl_start_time = time.perf_counter()

    try:

        executor.execute_pipeline(
            pipeline
        )

    except Exception as error:

        # Stop timer even if execution fails
        etl_end_time = time.perf_counter()

        etl_execution_time = (
            etl_end_time - etl_start_time
        )

        print("\n")
        print("=" * 60)
        print("PIPELINE EXECUTION FAILED")
        print("=" * 60)

        print(
            f"\nError: {error}"
        )

        print(
            f"\nETL Execution Time: "
            f"{etl_execution_time:.4f} seconds"
        )

        return

    # Stop ETL execution timer
    etl_end_time = time.perf_counter()

    etl_execution_time = (
        etl_end_time - etl_start_time
    )

    # --------------------------------------------------------
    # STEP 7: Display timing results
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("PERFORMANCE MEASUREMENT")
    print("=" * 60)

    print(
        f"\nLLM Generation Time : "
        f"{llm_generation_time:.4f} seconds"
    )

    print(
        f"ETL Execution Time  : "
        f"{etl_execution_time:.4f} seconds"
    )

    print(
        f"Total LLM-Assisted Time : "
        f"{llm_generation_time + etl_execution_time:.4f} seconds"
    )

    # --------------------------------------------------------
    # STEP 8: Finish
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("PROJECT EXECUTION COMPLETED")
    print("=" * 60)


if __name__ == "__main__":

    main()