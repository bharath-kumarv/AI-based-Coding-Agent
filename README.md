🤖 Adaptive AI Coding Agent (Rule-Based Intelligent Tutor)
📌 Project Overview

The Adaptive AI Coding Agent is a rule-based intelligent coding tutor built using Streamlit.
It dynamically generates programming problems and adapts difficulty levels based on user performance.

Unlike API-dependent AI systems, this tutor is fully self-contained and operates using a custom-designed adaptive algorithm without external AI services.

The system tracks user skill progression, analyzes performance patterns, and adjusts problem complexity accordingly.

🎯 Key Features

🔄 Adaptive difficulty adjustment (Easy → Medium → Hard)

📊 Skill tracking across topics (loops, conditionals, functions, lists)

🧠 Rule-based decision engine

📝 Automatic evaluation logic

💡 Context-aware hint generation

💾 Persistent user memory using JSON storage

🔐 Basic authentication system

🌐 Interactive web interface using Streamlit

🏗 System Architecture

The system follows a modular agent-based structure:

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

🧠 How It Works

The system analyzes user performance metrics:

Consecutive correct answers

Consecutive errors

Topic-wise skill scores

Success rate

It identifies weak skill areas.

Difficulty is adjusted dynamically:

Consistent success → Increased difficulty

Repeated errors → Reduced difficulty

Balanced performance → Moderate difficulty

New problems are generated with dynamic parameters for variation.

🛠 Technologies Used

Python

Streamlit

JSON (for memory persistence)

Object-Oriented Programming

Rule-based decision logic

No external AI APIs are used.

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/adaptive-ai-coding-agent.git
cd adaptive-ai-coding-agent

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py

📊 Learning Adaptation Logic

The adaptive engine adjusts user skill scores using:

Incremental reward on correct answers

Slight penalty on incorrect attempts

Weakest-skill prioritization

Difficulty progression thresholds

This enables a personalized coding practice experience.

🔮 Future Enhancements

Code execution sandboxing

Database-based user management

Advanced skill modeling

AI-based code feedback integration

Deployment on cloud platform

👩‍💻 Author

Subhasri N M
Engineering Student
AI & Machine Learning Enthusiast

⭐ Project Status

Functional prototype demonstrating adaptive educational agent architecture.