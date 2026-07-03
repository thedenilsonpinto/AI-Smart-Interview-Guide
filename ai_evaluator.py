def evaluate_answers(answers):

    total_words = sum(len(answer.split()) for answer in answers)

    if total_words > 150:
        communication = 9
    elif total_words > 80:
        communication = 8
    else:
        communication = 6

    technical = 8
    confidence = 8

    overall = round(
        (communication + technical + confidence) / 3,
        1
    )

    return {
        "communication": communication,
        "technical": technical,
        "confidence": confidence,
        "overall": overall
    }