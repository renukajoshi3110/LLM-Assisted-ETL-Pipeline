from agent import GeminiAgent


def main():

    agent = GeminiAgent()

    question = """
    Explain ETL Pipeline in simple words in 5 lines.
    """

    answer = agent.ask(question)

    print("\n========== GEMINI RESPONSE ==========\n")
    print(answer)


if __name__ == "__main__":
    main()