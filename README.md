Adaptive AI Coding Agent (Rule-Based Intelligent Tutor)
Project Overview

The Adaptive AI Coding Agent is a rule-based intelligent coding tutor developed using Python and Streamlit. The system dynamically generates programming challenges and adapts difficulty levels according to user performance.

Unlike API-dependent AI systems, this project is fully self-contained and operates using a custom-designed adaptive algorithm without relying on external AI services.

The platform continuously tracks user progress, analyzes performance patterns, and adjusts problem complexity to create a personalized learning experience.

Key Features
Adaptive difficulty adjustment (Easy → Medium → Hard)
Skill tracking across programming topics
Rule-based decision engine
Automatic answer evaluation
Context-aware hint generation
Persistent user memory using JSON storage
Basic authentication system
Interactive web interface using Streamlit
System Architecture
adaptive-ai-coding-agent/
│
├── app.py                  # Main Streamlit application
├── auth.py                 # Authentication logic
│
├── agent/
│   ├── decision_agent.py   # Adaptive difficulty logic
│   ├── evaluator.py        # Code evaluation engine
│   ├── hint_engine.py      # Context-based hints
│   └── memory.py           # User skill tracking
│
├── data/
│   └── user_memory.json    # Persistent performance tracking
│
├── problems/
│   ├── easy.py
│   ├── medium.py
│   └── hard.py
│
├── requirements.txt
└── README.md
Working Principle

The system evaluates user performance using multiple metrics, including:

Consecutive correct submissions
Consecutive incorrect attempts
Topic-wise skill scores
Overall success rate

Based on these metrics:

Consistent success increases difficulty
Repeated mistakes reduce difficulty
Balanced performance maintains moderate complexity

The tutor also prioritizes weaker skill areas and generates varied programming problems dynamically.

Technologies Used
Python
Streamlit
JSON Storage
Object-Oriented Programming
Rule-Based Adaptive Logic

No external AI APIs or machine learning services are used.

Installation
1. Clone the Repository
git clone https://github.com/your-username/adaptive-ai-coding-agent.git
cd adaptive-ai-coding-agent
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
Run the Application
streamlit run app.py
Adaptive Learning Logic

The adaptive engine updates user skill levels using:

Reward-based score increments for correct answers
Minor penalties for incorrect attempts
Weak-topic prioritization
Difficulty progression thresholds

This creates a personalized and progressive coding practice environment.

Future Enhancements
Secure code execution sandbox
Database-based user management
Advanced learner analytics
AI-assisted code feedback
Cloud deployment support
Project Status

Functional prototype demonstrating an adaptive educational coding tutor using rule-based intelligent agent architecture.
