import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="Py | Python Learning Buddy", page_icon="🐍", layout="centered")

# =========================================================
# THEME: Blue & Black
# =========================================================
st.markdown("""
    <style>
    .stApp { background-color: #0d1b2a; }
    h1, h2, h3, p, label, span { color: #e8edf2 !important; }
    .stButton>button {
        background-color: #1b98e0;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        padding: 0.5rem 1.2rem;
    }
    .stButton>button:hover { background-color: #147bb5; }
    .stTextInput>div>div>input, .stTextArea textarea {
        background-color: #1b263b;
        color: white;
        border-radius: 6px;
    }
    .stRadio label { color: #e8edf2 !important; }
    div[data-testid="stExpander"] {
        background-color: #14213d;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.title("🐍 Py — Your Python Learning Buddy")
st.write("A friendly, patient AI tutor that helps you master **Python Basics** — one concept at a time.")

with st.expander("👤 Meet Py"):
    st.write(
        "Py is a friendly, patient, and encouraging tutor who explains coding "
        "concepts in simple language, using easy words and real-life examples. "
        "Py never makes you feel bad for mistakes — only motivated to keep learning."
    )

st.divider()

# =========================================================
# CONCEPT EXPLAINER
# =========================================================
st.header("📖 Explain a Concept")
concept = st.text_input("Enter a Python concept (e.g. variables, loops, lists, functions):")

explanations = {
    "variables": "A variable is like a labeled box where you store information. "
                 "Example: `age = 15` — here `age` is a box holding the value 15. "
                 "You can change what's inside anytime!",
    "loops": "A loop lets you repeat an action multiple times without rewriting code. "
             "Example: `for i in range(5): print(i)` prints 0 to 4 automatically — "
             "like telling someone 'do this 5 times' instead of repeating instructions.",
    "lists": "A list is like a shopping bag that holds multiple items together. "
              "Example: `fruits = ['apple', 'banana', 'mango']` — you can add, remove, "
              "or check items inside it anytime.",
    "functions": "A function is a reusable block of code that performs a task, like a "
                 "recipe you can use again and again. Example: `def greet(name): "
                 "print('Hello', name)` — call `greet('Ravi')` anytime you need it.",
}

if st.button("Explain ✨"):
    if concept.strip() == "":
        st.warning("Please enter a concept first.")
    else:
        key = concept.strip().lower()
        if key in explanations:
            st.success(f"**Py:** {explanations[key]}")
        else:
            st.info(f"**Py:** '{concept}' is a great topic to explore! Try starting "
                    f"with fundamentals like variables, loops, lists, or functions, "
                    f"and Py will walk you through it step by step.")

st.divider()

# =========================================================
# QUIZ SECTION
# =========================================================
st.header("📝 Quick Quiz")

quiz = [
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#",
    },
    {
        "question": "Which of these is a valid variable name?",
        "options": ["2name", "name_2", "name-2", "name 2"],
        "answer": "name_2",
    },
    {
        "question": "What does print(type(5)) return?",
        "options": ["<class 'str'>", "<class 'int'>", "<class 'float'>", "<class 'bool'>"],
        "answer": "<class 'int'>",
    },
    {
        "question": "Which data type holds True/False values?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool",
    },
    {
        "question": "What does len('Python') return?",
        "options": ["5", "6", "7", "Error"],
        "answer": "6",
    },
]

user_answers = {}
for idx, q in enumerate(quiz):
    user_answers[idx] = st.radio(q["question"], q["options"], key=f"q{idx}", index=None)

if st.button("Submit Quiz"):
    score = sum(1 for idx, q in enumerate(quiz) if user_answers[idx] == q["answer"])
    st.success(f"You scored {score}/{len(quiz)}! 🎉")
    for idx, q in enumerate(quiz):
        if user_answers[idx] != q["answer"]:
            st.write(f"❌ **{q['question']}** — correct answer: **{q['answer']}**")

st.divider()

# =========================================================
# FOOTER
# =========================================================
st.caption("Py — Making Python simple, one step at a time. 🐍")
