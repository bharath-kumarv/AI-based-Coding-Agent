import traceback

def evaluate_code(user_code, problem):
    local_env = {}

    try:
        exec(user_code, {}, local_env)

        # Case 1: expected_output exists
        if "expected_output" in problem:
            output = local_env.get("output")
            if output == problem["expected_output"]:
                return "success", "Correct"
            return "failure", "Wrong output"

        # Case 2: function-based problem
        if "function" in problem and "test" in problem:
            func = local_env.get(problem["function"])
            if not func:
                return "error", "Function not defined"

            result = func(*problem["test"]["input"])
            if result == problem["test"]["output"]:
                return "success", "Correct"
            return "failure", "Wrong result"

        # Case 3: no checker → assume run-only
        return "success", "Code executed successfully"

    except Exception as e:
        return "error", traceback.format_exc()
