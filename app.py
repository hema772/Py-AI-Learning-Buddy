import streamlit as st
import google.generativeai as genai
import json
import re

# -------------------------------
# Configure Gemini API securely
# -------------------------------

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    st.error("""
❌ GOOGLE_API_KEY not found.

If running locally:
Create `.streamlit/secrets.toml`

If running on Streamlit Cloud:
Manage App → Settings → Secrets
""")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
st.set_page_config(page_title="Py - AI Learning Buddy", page_icon="🐍", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
<style>
.stButton>button {
    border-radius: 10px;
    font-weight: 600;
}
.correct-box {
    background-color: #d4edda;
    padding: 12px;
    border-radius: 8px;
    color: #155724;
    font-weight: 600;
}
.wrong-box {
    background-color: #f8d7da;
    padding: 12px;
    border-radius: 8px;
    color: #721c24;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("🐍 Meet Py")
    st.write("Your friendly, patient Python tutor who explains concepts with simple analogies and real-life examples.")
    st.markdown("---")
    st.caption("Built by Hemadharshini M | AI EMPOW(H)ER Program")

st.title("🎓 AI Learning Buddy — Py")
st.caption("A friendly AI tutor to help you master any topic, one concept at a time.")

# ---------- Session State ----------
if "history" not in st.session_state:
    st.session_state.history = []
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = {}

topic = st.text_input("📌 Enter a Topic", placeholder="e.g. Loops, Variables, Functions")

option = st.selectbox(
    "🎯 Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

def extract_json(text):
    """Pull JSON block out of Gemini's response safely."""
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(text)

generate_clicked = st.button("✨ Generate")

if generate_clicked:
    if topic == "":
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("Py is thinking... 🤔"):
            if option == "Explain Concept":
                prompt = f"You are Py, a friendly Python tutor. Explain {topic} in simple language as if teaching a 15-year-old student. Use easy words, one clear analogy, and keep it short and engaging."
                response = model.generate_content(prompt)
                st.session_state.history.append({"topic": topic, "activity": option, "response": response.text})
                st.session_state.quiz_data = None

            elif option == "Real-Life Example":
                prompt = f"You are Py, a friendly Python tutor. Give one clear real-life example of {topic} and explain how it works in simple terms."
                response = model.generate_content(prompt)
                st.session_state.history.append({"topic": topic, "activity": option, "response": response.text})
                st.session_state.quiz_data = None

            elif option == "Generate Quiz":
                prompt = f"""Create 5 multiple-choice questions on {topic} for a beginner.
Return ONLY valid JSON, no extra text, in this exact format:
[
  {{"question": "...", "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}}, "correct": "A", "explanation": "..."}}
]"""
                response = model.generate_content(prompt)
                try:
                    quiz = extract_json(response.text)
                    st.session_state.quiz_data = quiz
                    st.session_state.quiz_answers = {}
                    st.session_state.quiz_submitted = {}
                except Exception:
                    st.error("Couldn't parse quiz. Please try generating again.")
                    st.session_state.quiz_data = None

            else:
                prompt = topic
                response = model.generate_content(prompt)
                st.session_state.history.append({"topic": topic, "activity": option, "response": response.text})
                st.session_state.quiz_data = None

# ---------- Display Explanation / Example / Ask Anything ----------
if st.session_state.history and option != "Generate Quiz":
    latest = st.session_state.history[-1]
    st.markdown("### 💬 Py says:")
    st.write(latest["response"])
    st.download_button(
        label="⬇️ Download Response",
        data=latest["response"],
        file_name=f"{latest['topic']}_{latest['activity']}.txt",
        mime="text/plain"
    )

# ---------- Interactive Quiz ----------
if st.session_state.quiz_data:
    st.markdown("## 📝 Quiz Time")
    score = 0
    total = len(st.session_state.quiz_data)

    for i, q in enumerate(st.session_state.quiz_data):
        st.markdown(f"**Q{i+1}. {q['question']}**")

        selected = st.radio(
            "Choose one:",
            options=list(q["options"].keys()),
            format_func=lambda x, q=q: f"{x}. {q['options'][x]}",
            key=f"radio_{i}",
            index=None
        )

        submit_col, result_col = st.columns([1, 3])
        if submit_col.button("Submit", key=f"submit_{i}"):
            st.session_state.quiz_submitted[i] = selected

        if i in st.session_state.quiz_submitted and st.session_state.quiz_submitted[i]:
            chosen = st.session_state.quiz_submitted[i]
            if chosen == q["correct"]:
                st.markdown(f'<div class="correct-box">✅ Correct! {q["explanation"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="wrong-box">❌ Wrong. Correct answer: {q["correct"]}. {q["explanation"]}</div>', unsafe_allow_html=True)

        st.markdown("---")

    # Score summary
    correct_count = sum(
        1 for i, q in enumerate(st.session_state.quiz_data)
        if st.session_state.quiz_submitted.get(i) == q["correct"]
    )
    attempted = sum(1 for v in st.session_state.quiz_submitted.values() if v)
    if attempted > 0:
        st.info(f"📊 Score: {correct_count}/{attempted} attempted correctly")

# ---------- History ----------
if len(st.session_state.history) > 1:
    with st.expander("📜 View Previous Conversations"):
        for item in reversed(st.session_state.history[:-1]):
            st.markdown(f"**Topic:** {item['topic']} | **Activity:** {item['activity']}")
            st.write(item["response"])
            st.markdown("---")
