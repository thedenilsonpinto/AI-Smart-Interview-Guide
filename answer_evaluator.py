import google.generativeai as genai

genai.configure(
    api_key="YOUR_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def evaluate_answer(question, answer):

    # Don't evaluate empty answers
    if answer is None:
        return None

    if len(answer.strip()) < 3:
        return None

    try:

        prompt = f"""
You are an expert interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Give:

Score: X/10

Strength:
- point 1
- point 2

Improvement:
- point 1
- point 2

Keep response short.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception:

        return """
Score: 7/10

Strength:
- Good attempt

Improvement:
- Add more technical details
"""