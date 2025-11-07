# app.py
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key from the .env file
load_dotenv()
try:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    st.error("Error connecting to Gemini. Please check your GEMINI_API_KEY in the .env file.")
    st.stop() # Stop if the key is missing/invalid

MODEL_NAME = 'gemini-2.5-flash'

# app.py (continued)

def run_gemini_agent(email_text, tone):
    """
    Combines summarization and reply generation into a single efficient call.
    """
    system_prompt = f"""
    You are an expert AI Email Agent. Your task is to perform two things on the provided email:

    1. **SUMMARIZE**: Create a concise summary of the email in 3 bullet points.
    2. **REPLY**: Generate two distinct reply options in a {tone} tone. The first reply should be 'Accepting/Positive', and the second should be 'Declining/Requesting More Info'.

    Present the output in the following distinct, easy-to-read format:

    **SUMMARY:**
    * [Bullet Point 1: Main Topic]
    * [Bullet Point 2: Required Action/Decision]
    * [Bullet Point 3: Deadline/Context]

    **REPLY 1 (Accept/Positive):**
    [Generated Reply Text]

    **REPLY 2 (Decline/Request Info):**
    [Generated Reply Text]
    """
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[{"role": "user", "parts": [{"text": system_prompt}, {"text": f"EMAIL:\n---\n{email_text}"}]}]
    )
    return response.text

# app.py (continued)

# --- Streamlit UI Setup ---
st.set_page_config(layout="centered", page_title="Simple AI Email Agent")
st.title("📧 Simple AI Email Agent")
st.markdown("Paste an email below to get a summary and suggested replies instantly.")

# --- User Inputs ---
with st.sidebar:
    st.header("Agent Settings")
    tone_options = ['Formal', 'Casual', 'Urgent', 'Friendly']
    tone = st.selectbox("Select Reply Tone:", tone_options)
    st.markdown("---")
    st.caption("Using model: " + MODEL_NAME)

email_input = st.text_area("Paste Email Body Here:", height=250, 
                           placeholder="e.g., 'Hi team, the final report is due Friday at 5 PM. Please send all necessary data to me by Thursday noon. Thanks, Alex.'")

if st.button("Analyze & Generate Replies 🚀", type="primary"):
    if not email_input:
        st.error("Please paste an email to analyze.")
    else:
        # 3. RUN THE AGENT
        with st.spinner(f"Analyzing and drafting responses with a **{tone}** tone..."):
            try:
                full_result = run_gemini_agent(email_input, tone)
                
                # 4. DISPLAY THE RESULTS (Simple and Beautiful)
                st.subheader("✅ Analysis Complete")
                st.markdown(full_result)
                
                # Add a separator for clarity
                st.markdown("---")
                st.success("Responses ready! Review and adapt before sending.")

            except Exception as e:
                st.error(f"An error occurred: {e}. Check your API key and connection.")