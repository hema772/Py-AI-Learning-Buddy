import streamlit as st
import google.generativeai as genai

# =========================================================
# STEP 1: Configure Gemini API
# Get your key free from: https://aistudio.google.com/apikey
# =========================================================
GEMINI_API_KEY = ""   # <-- put your key here only

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# =========================================================
# PAGE CONFIG + BLUE-BLACK THEME
# =========================================================
st.set_page_config(page_title="Py - AI Learning Buddy", page_icon="🐍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0d1b2a; }
    h1, h2, h3, label, p { color: #e0e6ed !important; }
    .stButton>button {
        background-color: #1b98e0;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #1b263b;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.title("🐍 Py — Your Python Basics Learning Buddy")
st.caption("AI Learning Buddy Capstone Project")

with st.expander("👤 About Py (AI Persona)"):
    st.write(
        "You are Py, a friendly, patient, and encouraging Python programming "
        "tutor who explains coding concepts in simple language with fun "
        "real-life examples. You never make students feel bad for mistakes "
        "and always motivate them to keep learning."
    )

# =========================================================
# TOPIC + ACTIVITY SELECTION
# =========================================================
topic = st.text_input("Enter a Python topic (e.g. variables, loops, lists):")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Get Feedback on my Answer",
        "Ask Anything",
    ],
)

user_answer = ""
question_text = ""
if option == "Get Feedback on my Answer":
    question_text = st.text_area("Paste the quiz question here:")
    user_answer = st.text_input("Your answer:")

# =========================================================
# PROMPT TEMPLATES (matches your 5 submitted templates)
# =========================================================
PERSONA = "You are Py, a friendly, patient, and encouraging Python tutor."

def build_prompt(option, topic, question_text="", user_answer=""):
    if option == "Explain Concept":
        return (f"{PERSONA} Explain {topic} in simple language as if teaching "
                 f"a 15-year-old student. Use easy words, one clear analogy, "
                 f"and keep it short and engaging.")
    elif option == "Real-Life Example":
        return (f"{PERSONA} Give one clear real-life example of {topic} and "
                 f"explain how it works in simple terms.")
    elif option == "Generate Quiz":
        return (f"{PERSONA} Create 5 multiple-choice questions on {topic}. "
                 f"Each question should have 4 options (A, B, C, D). After "
                 f"each question, provide the correct answer and a short "
                 f"explanation.")
    elif option == "Get Feedback on my Answer":
        return (f"{PERSONA} The student answered \"{user_answer}\" for this "
                 f"question: {question_text}. Give encouraging feedback. If "
                 f"the answer is wrong, politely explain the correct answer.")
    else:
        return f"{PERSONA} {topic}"

# =========================================================
# GENERATE RESPONSE
# =========================================================
if st.button("Generate ✨"):
    if topic == "" and option != "Get Feedback on my Answer":
        st.warning("Please enter a topic first.")
    else:
        prompt = build_prompt(option, topic, question_text, user_answer)
        with st.spinner("Py is thinking..."):
            try:
                response = model.generate_content(prompt)
                st.success("Here's what Py says:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# =========================================================
# REFLECTION SECTION
# =========================================================
st.divider()
st.header("💭 Reflection on AI Limitations")
st.write(
    "AI is a great learning aid, but it cannot fully verify understanding, "
    "provide personalized mentorship, or replace human accountability. It "
    "works best as a supplement to human teaching, not a replacement."
)

st.caption("Built for the AI Learning Buddy Capstone Project • Topic: Python Basics")
