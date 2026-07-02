import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="Py - AI Learning Buddy", page_icon="🐍", layout="centered")

# ---- Color Scheme: Blue & Black (Trust + Growth) ----
st.markdown("""
    <style>
    .main { background-color: #0d1b2a; }
    h1, h2, h3 { color: #1b98e0; }
    </style>
""", unsafe_allow_html=True)

st.title("🐍 Py — Your Python Basics Learning Buddy")
st.write("Hi! I'm **Py**, a friendly tutor here to help you learn Python Basics step by step.")

# ---- Persona Info ----
with st.expander("👤 About Py (AI Persona)"):
    st.write("You are Py, a friendly, patient, and encouraging Python programming tutor "
             "who explains coding concepts in simple language with fun real-life examples.")

# ---- Section 1: Explanation ----
st.header("📖 Ask Py to Explain a Concept")
concept = st.text_input("Enter a Python concept (e.g. variables, loops, lists):")
if st.button("Explain"):
    if concept:
        st.info(f"**Py:** Let's talk about **{concept}**! "
                f"[Here you would call an actual AI API to generate the real explanation]")
    else:
        st.warning("Please enter a concept first.")

# ---- Section 2: Quiz ----
st.header("📝 Quick Quiz")
quiz = {
    "What symbol is used for comments in Python?": ["//", "#", "/* */", "--"],
    "Which is a valid variable name?": ["2name", "name_2", "name-2", "name 2"],
}
answers = {"What symbol is used for comments in Python?": "#",
           "Which is a valid variable name?": "name_2"}

score = 0
for q, options in quiz.items():
    user_ans = st.radio(q, options, key=q)
    if user_ans == answers[q]:
        score += 1

if st.button("Submit Quiz"):
    st.success(f"You scored {score}/{len(quiz)}! 🎉")

# ---- Section 3: Reflection ----
st.header("💭 Reflection on AI Limitations")
st.write("AI is a great learning aid, but it works best alongside human guidance, "
         "since it cannot fully verify understanding or provide personalized mentorship.")

st.caption("Built as part of the AI Learning Buddy Capstone Project")