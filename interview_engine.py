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
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(resume_text):

    try:

        prompt = f"""
Generate exactly 5 interview questions.

Rules:

- Return only questions.
- No introduction.
- No numbering explanation.
- No phrases like:
  "Let's start with"
  "I would like to know"
  "Can you tell me"
- Every question must end with '?'

Format:

Question 1?
Question 2?
Question 3?
Question 4?
Question 5?

Resume:

{resume_text}
"""

        response = model.generate_content(prompt)

        print("===== GEMINI RESPONSE =====")
        print(response.text)

        return response.text

    except Exception:

        return """
1. Tell me about yourself.

2. Explain your main project.

3. What are your strongest technical skills?

4. Why should we hire you?

5. What are your future goals?
"""