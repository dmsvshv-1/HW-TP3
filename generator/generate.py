import csv
import random
import os
import sys

NUM_ROWS = 50
COLUMNS = ["hero", "kills", "deaths", "role"]

def generate_row():
    return {
        "hero": random.choice(["Invoker", "Pudge", "Earthshaker", "Lina", "Juggernaut"]),
        "kills": random.randint(0, 30),
        "deaths": random.randint(0, 15),
        "role": random.choice(["Carry", "Support", "Offlane", "Midlane", "FullSupport"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
