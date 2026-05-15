def update_difficulty(status, memory):
    # Default initialization (VERY IMPORTANT)
    memory.setdefault("level", "easy")
    memory.setdefault("correct_in_row", 0)
    memory.setdefault("wrong_in_row", 0)

    if status == "success":
        memory["correct_in_row"] += 1
        memory["wrong_in_row"] = 0
    else:
        memory["wrong_in_row"] += 1
        memory["correct_in_row"] = 0

    # Increase difficulty
    if memory["correct_in_row"] >= 3:
        if memory["level"] == "easy":
            memory["level"] = "medium"
        elif memory["level"] == "medium":
            memory["level"] = "hard"
        memory["correct_in_row"] = 0

    # Decrease difficulty
    if memory["wrong_in_row"] >= 2:
        if memory["level"] == "hard":
            memory["level"] = "medium"
        elif memory["level"] == "medium":
            memory["level"] = "easy"
        memory["wrong_in_row"] = 0

    return memory
