# TODO решите задачу
import json
FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
        return round(sum([item["score"] * item["weight"] for item in json_data]), 3)

print(task())
