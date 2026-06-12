import os
import time
from ollama_client import ask_ollama

QUESTION_FILE = "latest_question.txt"
ANSWER_FILE = "latest_answer.txt"

last_question = ""

print("Ollama AI started...")
print("Watching latest_question.txt...\n")

while True:
    try:
        if not os.path.exists(QUESTION_FILE):
            time.sleep(0.1)
            continue

        with open(QUESTION_FILE, "r", encoding="utf-8") as f:
            question = f.read().strip()

        if len(question) < 20:
            time.sleep(0.1)
            continue

        if question == last_question:
            time.sleep(0.1)
            continue

        last_question = question

        print("=" * 60)
        print("NEW QUESTION")
        print("=" * 60)
        print(question)
        print("\nThinking...\n")

        answer = ask_ollama(question)

        with open(
            ANSWER_FILE,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(answer)

        print("ANSWER:")
        print(answer)
        print("=" * 60)

    except KeyboardInterrupt:
        break

    except Exception as e:
        print("Error:", e)
        time.sleep(1)