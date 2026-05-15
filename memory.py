import json
import os

MEMORY_PATH = "data/user_memory.json"

DEFAULT_MEMORY = {
    "level": "easy",
    "streak": 0,
    "total_solved": 0
}

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return DEFAULT_MEMORY.copy()

    with open(MEMORY_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_MEMORY.copy()

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=4)
