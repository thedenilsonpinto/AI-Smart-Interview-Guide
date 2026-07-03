import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_followup(question, answer):

    try:

        prompt = f"""
You are an interviewer.

Original Question:
{question}

Candidate Answer:
{answer}

Generate ONE short follow-up question.

Maximum 1 line.
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:

        return "Can you explain that in more detail?"