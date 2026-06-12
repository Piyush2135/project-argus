import json
import csv
import os

DATABASE_FILE = "question_bank.json"
CSV_FILE = "question_bank.csv"

if not os.path.exists(DATABASE_FILE):
    print("question_bank.json not found.")
    exit()

with open(DATABASE_FILE, "r", encoding="utf-8") as f:
    database = json.load(f)


def detect_topic(text):
    text = text.lower()

    physics = [
        "force", "velocity", "speed", "magnet", "heat",
        "current", "voltage", "light", "energy", "motion"
    ]

    chemistry = [
        "atom", "molecule", "acid", "base", "salt",
        "metal", "reaction", "compound", "element"
    ]

    biology = [
        "cell", "blood", "kidney", "nephron",
        "photosynthesis", "respiration", "organ"
    ]

    geography = [
        "river", "mountain", "capital", "country",
        "ocean", "state", "continent"
    ]

    history = [
        "war", "king", "dynasty", "freedom",
        "independence", "empire"
    ]

    for word in physics:
        if word in text:
            return "Physics"

    for word in chemistry:
        if word in text:
            return "Chemistry"

    for word in biology:
        if word in text:
            return "Biology"

    for word in geography:
        if word in text:
            return "Geography"

    for word in history:
        if word in text:
            return "History"

    return "General Knowledge"


# Add topic tags
for item in database:
    item["topic"] = detect_topic(item["question"])


# Save updated JSON
with open(DATABASE_FILE, "w", encoding="utf-8") as f:
    json.dump(database, f, indent=2, ensure_ascii=False)


# Export CSV
with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "No.",
        "Timestamp",
        "Topic",
        "Question"
    ])

    for i, item in enumerate(database, start=1):
        writer.writerow([
            i,
            item.get("timestamp", ""),
            item.get("topic", ""),
            item.get("question", "").replace("\n", " | ")
        ])

print("=" * 60)
print(f"Processed {len(database)} questions.")
print(f"Updated: {DATABASE_FILE}")
print(f"Exported: {CSV_FILE}")
print("=" * 60)

# Topic summary
summary = {}
for item in database:
    topic = item["topic"]
    summary[topic] = summary.get(topic, 0) + 1

print("\nQuestion Summary:")
for topic, count in sorted(summary.items()):
    print(f"{topic:20} : {count}")