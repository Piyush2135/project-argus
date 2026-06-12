import json
import os

DATABASE_FILE = "question_bank.json"

if not os.path.exists(DATABASE_FILE):
    print("No question bank found.")
    exit()

with open(DATABASE_FILE, "r", encoding="utf-8") as f:
    database = json.load(f)

print("=" * 60)
print(f"Total Questions Collected: {len(database)}")
print("=" * 60)

while True:
    print("\nOptions:")
    print("1. List all questions")
    print("2. Search by keyword")
    print("3. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        for i, item in enumerate(database, 1):
            print("\n" + "-" * 60)
            print(f"Question {i}")
            print("-" * 60)
            print(item["question"])

    elif choice == "2":
        keyword = input("Enter keyword: ").lower().strip()
        found = False

        for i, item in enumerate(database, 1):
            if keyword in item["question"].lower():
                found = True
                print("\n" + "-" * 60)
                print(f"Match {i}")
                print("-" * 60)
                print(item["question"])

        if not found:
            print("No matching questions found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")