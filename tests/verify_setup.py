from src.ai_client import GeminiClient


def main():
    print("--- Connecting to Gemini ---")
    try:
        # Initialize client
        client = GeminiClient()

        # Send a test prompt
        print("Sending prompt: 'Hello, are you working?'")
        response = client.ask("Hello, are you working? Reply with 'Yes, I am live!'")

        print(f"Response: {response}")
        print("--- SUCCESS: Framework is connected! ---")

    except Exception as e:
        print(f"--- FAILURE: {e} ---")


if __name__ == "__main__":
    main()