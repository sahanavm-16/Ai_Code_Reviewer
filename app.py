import os
import streamlit as st
from google import generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit Page Setup
st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

# --- Dark Mode State ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- Toggle Button ---
mode = st.toggle("🌗 Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = mode

# --- CSS Styling based on Mode ---
if st.session_state.dark_mode:
    background_color = "#0E1117"
    text_color = "#FAFAFA"
    secondary_text = "#BBBBBB"
else:
    background_color = "#FFFFFF"
    text_color = "#1E1E1E"
    secondary_text = "#222222"

# --- Inject CSS ---
st.markdown(f"""
    <style>
        body {{
            background-color: {background_color};
            color: {text_color};
        }}
        .centered-text {{
            text-align: center;
            font-weight: 700;
            color: {text_color};
        }}
        .description {{
            text-align: center;
            font-size: 18px;
            font-weight: 500;
            color: {secondary_text};
            margin-top: -10px;
            line-height: 1.6;
        }}
        .stTextArea textarea {{
            font-family: monospace;
            font-size: 15px;
            background-color: {'#1E1E1E' if st.session_state.dark_mode else '#F9F9F9'};
            color: {text_color};
        }}
        .stSelectbox, .stButton>button {{
            color: {text_color} !important;
        }}
        footer {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- Page Title and Description ---
st.markdown("<h1 class='centered-text'>🤖 AI-Powered Code Reviewer</h1>", unsafe_allow_html=True)
st.markdown(f"""
    <p class='description'>
        Welcome to your <b>AI Code Reviewer.</b><br>
        Paste your code below, choose the programming language, and get AI-driven insights on:<br>
        ✅ <b>Strengths</b> &emsp; ⚠️ <b>Issues</b> &emsp; 💡 <b>Suggestions</b> &emsp; 🔒 <b>Security Tips</b>
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Language Selection ---
language = st.selectbox(
    "🌐 Select Programming Language:",
    [
        "Auto Detect", "Python", "C", "C++", "Java", "JavaScript",
        "HTML/CSS", "SQL", "Go", "PHP", "Rust", "Swift", "Other"
    ]
)

# --- Code Input ---
user_code = st.text_area("💻 Paste your code here:", height=300, placeholder="def add(a, b):\n    return a + b")

# --- Review Button ---
if st.button("🔍 Review My Code"):
    if not user_code.strip():
        st.warning("Please paste some code first!")
    else:
        with st.spinner("Analyzing your code with Gemini... ⏳"):
            prompt = f"""
            You are an expert software engineer and code reviewer.
            Review the following {language if language != "Auto Detect" else "code"}.
            Provide feedback in this format:

            1️⃣ **Strengths** — What’s good or efficient about the code.  
            2️⃣ **Issues/Bugs** — Mistakes or potential problems.  
            3️⃣ **Suggestions** — How to improve readability, performance, or maintainability.  
            4️⃣ **Security/Optimization Tips** — Advice for safety, performance, or scalability.  

            Code ({language}):
            {user_code}
            """

            try:
                response = model.generate_content(prompt)
                feedback = response.text

                st.subheader("🧾 Code Review Report")
                st.markdown(feedback)

                st.markdown("---")
                st.subheader("📄 Your Original Code")
                st.code(user_code, language=language.lower() if language != "Auto Detect" else "text")

                st.success("✅ Review completed successfully!")

            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- Footer ---
st.markdown("---")
st.markdown(
    f"""
    <div style='text-align:center; color:{secondary_text};'>
        Built with ❤️ using Streamlit<br>
        © 2025 AI Code Reviewer. All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True
)
