# final_working_app.py - PUT THIS IN YOUR MAIN FOLDER
import streamlit as st
import random
import json
from datetime import datetime

# ==================== NO GEMINI REQUIRED ====================
# We'll create SMART ADAPTIVE problems without external AI

st.set_page_config(
    page_title="Adaptive Coding Agent",
    page_icon="🤖",
    layout="wide"
)

# ==================== SMART PROBLEM GENERATOR ====================
class AdaptiveProblemGenerator:
    def __init__(self):
        self.problem_history = []
        self.user_skills = {
            "loops": {"score": 0.5, "attempts": 0, "success_rate": 0},
            "conditionals": {"score": 0.5, "attempts": 0, "success_rate": 0},
            "functions": {"score": 0.5, "attempts": 0, "success_rate": 0},
            "lists": {"score": 0.5, "attempts": 0, "success_rate": 0}
        }
        
    def generate_problem(self, user_performance=None):
        """Generate SMART adaptive problems"""
        
        # Analyze user performance to choose topic
        weakest_topic = min(self.user_skills.items(), 
                          key=lambda x: x[1]["score"])[0]
        
        # Adjust difficulty based on performance
        if user_performance:
            if user_performance.get("consecutive_correct", 0) >= 2:
                difficulty = "medium" if self._get_avg_score() < 0.7 else "hard"
            elif user_performance.get("consecutive_errors", 0) >= 2:
                difficulty = "easy"
            else:
                difficulty = "easy" if self._get_avg_score() < 0.5 else "medium"
        else:
            difficulty = "easy"
        
        # Generate problem based on topic and difficulty
        problem = self._create_problem(weakest_topic, difficulty)
        
        # Add to history
        self.problem_history.append({
            "topic": weakest_topic,
            "difficulty": difficulty,
            "timestamp": datetime.now().isoformat()
        })
        
        return problem
    
    def _get_avg_score(self):
        """Calculate average user score"""
        scores = [skill["score"] for skill in self.user_skills.values()]
        return sum(scores) / len(scores) if scores else 0.5
    
    def _create_problem(self, topic, difficulty):
        """Create a unique problem every time"""
        
        # Dynamic parameters
        base_num = random.randint(3, 10)
        
        if difficulty == "easy":
            num = base_num
            complexity = "simple"
        elif difficulty == "medium":
            num = base_num * 2
            complexity = "intermediate"
        else:  # hard
            num = base_num * 3
            complexity = "challenging"
        
        # Topic-specific problems (always different due to random numbers)
        problems = {
            "loops": [
                {
                    "question": f"Create a list of numbers from 1 to {num}",
                    "expected_output": str(list(range(1, num + 1))),
                    "starter_code": "output = []",
                    "hint": f"Use range(1, {num + 1}) and convert to list",
                    "explanation": "The range() function generates numbers, list() converts to list"
                },
                {
                    "question": f"Calculate the sum of squares from 1 to {num}",
                    "expected_output": str(sum(i*i for i in range(1, num + 1))),
                    "starter_code": "output = 0",
                    "hint": f"Loop from 1 to {num} and add i*i each time",
                    "explanation": "Square each number (i*i) and add to total"
                }
            ],
            "conditionals": [
                {
                    "question": f"Check if {num} is even or odd",
                    "expected_output": "Even" if num % 2 == 0 else "Odd",
                    "starter_code": f"output = ''  # Check if {num} is even or odd",
                    "hint": "Use modulo operator: num % 2 == 0 for even",
                    "explanation": "Even numbers are divisible by 2 (remainder 0)"
                },
                {
                    "question": f"Classify {num}: 'Small' if <10, 'Medium' if 10-20, 'Large' if >20",
                    "expected_output": "Small" if num < 10 else "Medium" if num <= 20 else "Large",
                    "starter_code": f"output = ''  # Classify {num}",
                    "hint": "Use if-elif-else chain with comparison operators",
                    "explanation": "Chain conditions to check ranges"
                }
            ],
            "functions": [
                {
                    "question": f"Create a function to double a number, then double {num}",
                    "expected_output": str(num * 2),
                    "starter_code": f"# Define function here\n\ndef double(x):\n    return x * 2\n\noutput = double({num})",
                    "hint": "Define function with def, then call it",
                    "explanation": "Functions encapsulate reusable code"
                },
                {
                    "question": f"Create a function is_even(n), test with {num}",
                    "expected_output": str(num % 2 == 0),
                    "starter_code": f"# Define function here\n\ndef is_even(n):\n    return n % 2 == 0\n\noutput = is_even({num})",
                    "hint": "Return the boolean expression directly",
                    "explanation": "Functions can return boolean values"
                }
            ],
            "lists": [
                {
                    "question": f"Reverse this list: {list(range(1, num+1))}",
                    "expected_output": str(list(range(1, num+1))[::-1]),
                    "starter_code": f"original = {list(range(1, num+1))}\noutput = []  # Reverse it",
                    "hint": "Use list slicing: list[::-1]",
                    "explanation": "Slicing with [::-1] reverses a list"
                },
                {
                    "question": f"Filter even numbers from: {list(range(1, num*2+1))}",
                    "expected_output": str([i for i in range(1, num*2+1) if i % 2 == 0]),
                    "starter_code": f"numbers = {list(range(1, num*2+1))}\noutput = []  # Filter evens",
                    "hint": "Use list comprehension with condition",
                    "explanation": "List comprehensions can filter elements"
                }
            ]
        }
        
        # Get topic problems and rotate
        topic_problems = problems.get(topic, problems["loops"])
        
        # Add unique ID to ensure variety
        problem_id = len(self.problem_history)
        selected = topic_problems[problem_id % len(topic_problems)].copy()
        
        # Add metadata
        selected.update({
            "topic": topic,
            "difficulty": difficulty,
            "complexity": complexity,
            "problem_id": problem_id,
            "generated_at": datetime.now().isoformat()
        })
        
        return selected
    
    def update_user_skill(self, topic, correct):
        """Update user skill based on performance"""
        if topic in self.user_skills:
            skill = self.user_skills[topic]
            skill["attempts"] += 1
            
            if correct:
                skill["score"] = min(1.0, skill["score"] + 0.1)
            else:
                skill["score"] = max(0.1, skill["score"] - 0.05)
            
            # Update success rate
            if correct:
                skill["success_rate"] = (skill.get("successes", 0) + 1) / skill["attempts"]
                skill["successes"] = skill.get("successes", 0) + 1

# ==================== INITIALIZE APP ====================
if "generator" not in st.session_state:
    st.session_state.generator = AdaptiveProblemGenerator()

if "stats" not in st.session_state:
    st.session_state.stats = {
        "total_correct": 0,
        "total_attempts": 0,
        "current_streak": 0,
        "consecutive_errors": 0,
        "consecutive_correct": 0,
        "level": "beginner",
        "badges": []
    }

if "current_problem" not in st.session_state:
    st.session_state.current_problem = st.session_state.generator.generate_problem()

# ==================== UI STYLING ====================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.stButton>button {
    background: linear-gradient(90deg, #FF512F, #DD2476);
    color: white;
    border: none;
    padding: 10px 24px;
    border-radius: 8px;
    font-weight: bold;
}
.stTextArea textarea {
    background-color: #1e1e1e;
    color: #d4d4d4;
    border: 1px solid #444;
}
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
