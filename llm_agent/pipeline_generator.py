# ============================================================
# LLM-ASSISTED ETL PIPELINE GENERATOR
# ============================================================

import json

from llm_agent.agent import GeminiAgent
from llm_agent.prompts import build_pipeline_prompt


class PipelineGenerator:
    """
    Generates a structured ETL workflow from a
    natural-language user request using an LLM.
    """

    def __init__(self):

        # Create the Gemini LLM agent
        self.agent = GeminiAgent()

    # ========================================================
    # GENERATE PIPELINE
    # ========================================================

    def generate_pipeline(self, user_request):
        """
        Send the user's ETL request to Gemini and
        convert the response into a Python dictionary.
        """

        # Build the complete prompt
        prompt = build_pipeline_prompt(
            user_request
        )

        # Ask Gemini to generate the pipeline
        response = self.agent.ask(
            prompt
        )

        # ----------------------------------------------------
        # Clean Gemini response
        # ----------------------------------------------------

        response = response.strip()

        # Remove Markdown code fences if Gemini adds them
        if response.startswith("```"):

            response = response.replace(
                "```json",
                ""
            )

            response = response.replace(
                "```",
                ""
            )

            response = response.strip()

        # ----------------------------------------------------
        # Convert JSON response to Python dictionary
        # ----------------------------------------------------

        try:

            pipeline = json.loads(
                response
            )

        except json.JSONDecodeError:

            print(
                "\nERROR: Gemini did not return valid JSON."
            )

            print(
                "\nRaw Gemini response:"
            )

            print(
                response
            )

            return None

        # ----------------------------------------------------
        # Validate pipeline structure
        # ----------------------------------------------------

        if not isinstance(
            pipeline,
            dict
        ):

            print(
                "\nERROR: Generated pipeline is not a JSON object."
            )

            return None

        # Check pipeline name
        if "pipeline_name" not in pipeline:

            print(
                "\nERROR: Pipeline is missing 'pipeline_name'."
            )

            return None

        # Check steps
        steps = pipeline.get(
            "steps",
            []
        )

        if not isinstance(
            steps,
            list
        ):

            print(
                "\nERROR: Pipeline 'steps' must be a list."
            )

            return None

        if len(steps) == 0:

            print(
                "\nERROR: Pipeline contains no steps."
            )

            return None

        # ----------------------------------------------------
        # Validate individual steps
        # ----------------------------------------------------

        valid_operations = {
            "LOAD",
            "CLEAN",
            "TRANSFORM",
            "JOIN",
            "STORE",
            "VALIDATE",
            "VALIDATION"
        }

        for index, step in enumerate(
            steps,
            start=1
        ):

            if not isinstance(
                step,
                dict
            ):

                print(
                    f"\nERROR: Step {index} "
                    f"is not a JSON object."
                )

                return None

            # Required fields
            operation = step.get(
                "operation"
            )

            dataset = step.get(
                "dataset"
            )

            if not operation:

                print(
                    f"\nERROR: Step {index} "
                    f"is missing 'operation'."
                )

                return None

            if not dataset:

                print(
                    f"\nERROR: Step {index} "
                    f"is missing 'dataset'."
                )

                return None

            operation = str(
                operation
            ).upper().strip()

            # Check supported operation
            if operation not in valid_operations:

                print(
                    f"\nERROR: Step {index} "
                    f"contains unsupported operation: "
                    f"{operation}"
                )

                print(
                    "\nSupported operations:"
                )

                print(
                    ", ".join(
                        sorted(valid_operations)
                    )
                )

                return None

            # Make sure operation is stored consistently
            step["operation"] = operation

            # ------------------------------------------------
            # JOIN validation
            # ------------------------------------------------

            if operation == "JOIN":

                if not step.get(
                    "join_with"
                ):

                    print(
                        f"\nERROR: JOIN step {index} "
                        f"is missing 'join_with'."
                    )

                    return None

                if not step.get(
                    "join_key"
                ):

                    print(
                        f"\nERROR: JOIN step {index} "
                        f"is missing 'join_key'."
                    )

                    return None

            # ------------------------------------------------
            # Add step number if Gemini omitted it
            # ------------------------------------------------

            if not step.get(
                "step_number"
            ):

                step["step_number"] = index

        return pipeline

    # ========================================================
    # DISPLAY PIPELINE
    # ========================================================

    def display_pipeline(
        self,
        pipeline
    ):
        """
        Display the generated ETL workflow
        in a readable format.
        """

        if pipeline is None:

            return

        print(
            "\n========================================"
        )

        print(
            "GENERATED ETL PIPELINE"
        )

        print(
            "========================================"
        )

        print(
            f"\nPipeline Name: "
            f"{pipeline.get('pipeline_name', 'Unnamed Pipeline')}"
        )

        print(
            f"\nDescription: "
            f"{pipeline.get('description', 'No description provided.')}"
        )

        # ----------------------------------------------------
        # Datasets
        # ----------------------------------------------------

        datasets = pipeline.get(
            "datasets",
            []
        )

        print(
            "\nDatasets:"
        )

        if datasets:

            for dataset in datasets:

                print(
                    f"  - {dataset}"
                )

        else:

            print(
                "  No datasets specified."
            )

        # ----------------------------------------------------
        # Steps
        # ----------------------------------------------------

        print(
            "\nSteps:"
        )

        for step in pipeline.get(
            "steps",
            []
        ):

            step_number = step.get(
                "step_number"
            )

            operation = step.get(
                "operation"
            )

            dataset = step.get(
                "dataset"
            )

            details = step.get(
                "details",
                ""
            )

            print(
                f"\nStep {step_number}"
            )

            print(
                f"Operation : {operation}"
            )

            print(
                f"Dataset   : {dataset}"
            )

            print(
                f"Details   : {details}"
            )

            # JOIN information
            if operation == "JOIN":

                print(
                    f"Join With : "
                    f"{step.get('join_with')}"
                )

                print(
                    f"Join Key  : "
                    f"{step.get('join_key')}"
                )

        print(
            "\n========================================"
        )