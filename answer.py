from PIL import Image
import easyocr
import time
import os
import warnings

from ollama_client import ask_ollama



IMAGE_FILE = "capture.png"
CROP_FILE = "quiz_crop.png"

QUESTION_FILE = "latest_question.txt"
ANSWER_FILE = "latest_answer.txt"

LEFT = 0.03
TOP = 0.22
RIGHT = 0.97
BOTTOM = 0.86

CHECK_INTERVAL = 0.10



warnings.filterwarnings("ignore")

print("Loading OCR model...")
reader = easyocr.Reader(
    ['en'],
    gpu=False,
    verbose=False
)

print("OCR + Ollama ready.\n")

last_modified = 0
last_text = ""

BAD_WORDS = [
    "all",
    "wrong",
    "skipped",
    "report",
    "error",
    "previous",
    "next",
    "your ans",
    "right ans",
    "explanation",
    "sec",
    "problems",
    "terminal",
    "powershell",
    "output",
    "debug",
    "visual studio",
    "code",
    "rapid_quiz"
]

while True:
    try:

        if not os.path.exists(IMAGE_FILE):
            time.sleep(0.1)
            continue

        modified = os.path.getmtime(IMAGE_FILE)

        if modified == last_modified:
            time.sleep(CHECK_INTERVAL)
            continue

        last_modified = modified

        try:
            img = Image.open(IMAGE_FILE)
        except:
            time.sleep(0.05)
            continue

        w, h = img.size

        crop = img.crop((
            int(w * LEFT),
            int(h * TOP),
            int(w * RIGHT),
            int(h * BOTTOM)
        ))

        crop.save(CROP_FILE)

        result = reader.readtext(
            CROP_FILE,
            detail=0,
            paragraph=False
        )

        cleaned = []

        for line in result:

            line = line.strip()

            if len(line) < 2:
                continue

            lower = line.lower()

            if any(word in lower for word in BAD_WORDS):
                continue

            cleaned.append(line)

        final_text = "\n".join(cleaned).strip()

        if len(final_text) < 20:
            time.sleep(CHECK_INTERVAL)
            continue

        if final_text == last_text:
            time.sleep(CHECK_INTERVAL)
            continue

        last_text = final_text

        # Save OCR output
        with open(
            QUESTION_FILE,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(final_text)

       
        try:
            ai_answer = ask_ollama(final_text)
        except Exception as e:
            ai_answer = f"Ollama Error: {e}"

       
        with open(
            ANSWER_FILE,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(ai_answer)

        os.system("cls")

        print("=" * 80)
        print("OCR QUESTION")
        print("=" * 80)
        print(final_text)

        print("\n" + "=" * 80)
        print("OLLAMA ANSWER")
        print("=" * 80)
        print(ai_answer)

        print("\nWatching for next question...")

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\nStopped.")
        break

    except PermissionError:
        time.sleep(0.05)

    except Exception as e:
        print("Runtime Error:", e)
        time.sleep(0.2)
