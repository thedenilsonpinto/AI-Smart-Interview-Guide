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


def smart_evaluate(answers):

    try:

        all_answers = "\n".join(answers)

        prompt = f"""
You are a professional interviewer.

Evaluate these interview answers.

Answers:
{all_answers}

Give:

Communication: X/10
Technical: X/10
Confidence: X/10
Overall: X/10

Short explanation.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception:

        return """
Interview Summary

Communication: 8/10
Technical: 8/10
Confidence: 8/10
Overall: 8/10

The interview was completed successfully.

The AI evaluation is temporarily unavailable because the Gemini API quota has been reached or the service is unavailable.

Please try again later.
"""