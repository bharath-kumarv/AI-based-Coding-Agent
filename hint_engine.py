def generate_hint(status, problem):
    if status == "error":
        return "Fix syntax, indentation, or variable names."
    if status == "failure":
        return problem.get("hint", "Review the logic.")
    return ""
