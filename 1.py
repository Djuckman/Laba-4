import json

# TODO решите задачу
INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE) as inp:
        json_data = json.load(inp)
        return round(sum([inst["score"] * inst["weight"] for inst in json_data]), 3)


print(task())
