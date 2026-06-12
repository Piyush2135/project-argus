import os
import time
import json
import hashlib
from datetime import datetime

QUESTION_FILE = "latest_question.txt"
DATABASE_FILE = "question_bank.json"

# Load existing database
if os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        database = json.load(f)
else:
    database = []

seen_ids = set(item["id"] for item in database)

print("Study Assistant started.")
print("Watching for new OCR questions...\n")

while True:
    try:
        if not os.path.exists(QUESTION_FILE):
            time.sleep(0.5)
            continue

        with open(QUESTION_FILE, "r", encoding="utf-8") as f:
            question = f.read().strip()

        if len(question) < 20:
            time.sleep(0.5)
            continue

        # Create a unique hash for duplicate detection
        qid = hashlib.md5(
            question.encode("utf-8")
        ).hexdigest()

        if qid in seen_ids:
            time.sleep(0.5)
            continue

        # New question detected
        seen_ids.add(qid)

        record = {
            "id": qid,
            "timestamp": datetime.now().isoformat(),
            "question": question
        }

        database.append(record)

        # Save database
        with open(DATABASE_FILE, "w", encoding="utf-8") as f:
            json.dump(
                database,
                f,
                indent=2,
                ensure_ascii=False
            )

        print("=" * 60)
        print("NEW QUESTION SAVED")
        print("=" * 60)
        print(question)
        print("=" * 60)
        print(f"Total saved: {len(database)}\n")

        time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped.")
        break

    except Exception as e:
        print("Error:", e)
        time.sleep(1)