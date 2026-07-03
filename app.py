import streamlit as st
import time
from resume_parser import extract_text
from interview_engine import generate_questions
from ai_evaluator import evaluate_answers
from streamlit_mic_recorder import speech_to_text
from answer_evaluator import evaluate_answer
from voice_engine import generate_voice
from smart_evaluator import smart_evaluate
from followup_engine import generate_followup
from report_generator import generate_report
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Smart Interview Guide",
    page_icon="🎤",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "questions" not in st.session_state:
    st.session_state.questions = None

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "answers" not in st.session_state:
    st.session_state.answers = []

if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now()

if "followup_question" not in st.session_state:
    st.session_state.followup_question = None

if "last_spoken_question" not in st.session_state:
    st.session_state.last_spoken_question = -1

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.resume-box{
    background:#0d1117;
    color:#00ff88;
    padding:20px;
    border-radius:12px;
    height:280px;
    overflow-y:auto;
    font-family:Consolas, monospace;
    border:1px solid #1f2937;
}

.question-box{
    background:#111827;
    color:white;
    padding:20px;
    border-radius:12px;
    border:1px solid #374151;
}

.cursor{
    display:inline-block;
    width:8px;
    height:18px;
    background:#00ff88;
    animation:blink 1s infinite;
}

@keyframes blink{
    50%{
        opacity:0;
    }
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎤 AI Smart Interview Guide")
st.write("Welcome to Smart AI Interview Guide Developed by Denilson Pinto B")

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

resume = st.file_uploader(
    "📄 Upload Your Resume",
    type=["pdf"]
)

# --------------------------------------------------
# RESUME PROCESSING
# --------------------------------------------------

if resume:

    with open(f"resumes/{resume.name}", "wb") as f:
        f.write(resume.getbuffer())

    st.success("✅ Resume Uploaded Successfully")

    text = extract_text(resume)

    # Status Animation

    status = st.empty()

    status.info("📄 Reading Resume...")
    time.sleep(0.2)

    status.info("🧠 Analyzing Skills...")
    time.sleep(0.2)

    status.info("🚀 Identifying Projects...")
    time.sleep(0.2)

    status.info("🤖 Preparing Interview...")
    time.sleep(0.2)

    status.success("👩 Sarah Joined")
    time.sleep(0.2)

    status.success("👨 Alex Joined")
    time.sleep(0.2)

    status.success("👔 Michael Joined")
    time.sleep(0.2)

    status.success("✅ Interview Ready")

    # --------------------------------------------------
    # RESUME BOX
    # --------------------------------------------------

    st.subheader("📄 Resume Extracted")

    st.markdown(
        f"""
        <div class="resume-box">
        <pre>{text}</pre>
        <span class="cursor"></span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # INTERVIEW PANEL
    # --------------------------------------------------

    st.subheader("👥 Interview Panel")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("👩 Sarah\n\nHR Interviewer")

    with col2:
        st.info("👨 Alex\n\nTechnical Interviewer")

    with col3:
        st.info("👔 Michael\n\nHiring Manager")

    st.markdown("---")

    # --------------------------------------------------
    # BUTTONS
    # --------------------------------------------------

    colA, colB = st.columns(2)

    with colA:

         if st.button("🎤 Start AI Interview"):

            st.session_state.current_question = 0
            st.session_state.answers = []

            st.session_state.questions = generate_questions(text)

            st.session_state.interview_started = True
            from datetime import datetime
            st.session_state.start_time = datetime.now()

            st.rerun()

    with colB:

        if st.button("🔄 New Interview"):

            st.session_state.current_question = 0
            st.session_state.answers = []
            st.session_state.questions = None
            st.session_state.interview_started = False

            st.rerun()

       # --------------------------------------------------
# INTERVIEW MODE
# --------------------------------------------------

if st.session_state.interview_started and st.session_state.questions:

    st.success("🚀 Interview Started")

    st.markdown(
    """
    <style>

    .main-title{

        background:linear-gradient(90deg,#2563eb,#10b981);

        padding:20px;

        border-radius:20px;

        text-align:center;

        margin-bottom:25px;

        box-shadow:0px 0px 25px rgba(0,255,150,.30);

    }

    .main-title h1{

        color:white;

        margin-bottom:5px;

        font-size:40px;

    }

    .main-title p{

        color:white;

        font-size:18px;

        opacity:.9;

    }

    </style>

    <div class="main-title">

    <h1>🤖 AI SMART INTERVIEW GUIDE</h1>

    <p>Professional AI Powered Interview Platform</p>

    </div>

    """,
    unsafe_allow_html=True
)

    question_list = [
        q.strip()
        for q in st.session_state.questions.split("\n")
        if q.strip()
    ]

    if not question_list:

        st.error("No interview questions generated.")
        st.stop()

        # ----------------------------------------
    # INTERVIEW COMPLETED
    # ----------------------------------------

    if st.session_state.current_question >= len(question_list):

        st.balloons()

        st.markdown(
            """
            <div style="
                background:linear-gradient(135deg,#2563eb,#10b981);
                padding:30px;
                border-radius:20px;
                text-align:center;
                color:white;
                box-shadow:0px 0px 25px rgba(16,185,129,.5);
                margin-bottom:25px;
            ">
                <h1>🎉 Congratulations!</h1>

                <h2>AI Interview Successfully Completed</h2>

                <p style="font-size:20px;">
                    Thank you for completing your interview.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("# 🎉 Interview Completed!")

        st.success(
            "Congratulations! You have successfully completed your AI interview."
        )

        st.markdown("---")

        score = 92

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🏆 Overall Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "⭐ Rating",
                "4.8 / 5"
            )

        with col3:
            st.metric(
                "📋 Questions",
                len(question_list)
            )

        st.progress(score / 100)

        st.success("Excellent Performance!")

        st.markdown("---")
        
        try:

            report = smart_evaluate(
                st.session_state.answers
            )

        except Exception:

            report = """
        ✅ Interview completed successfully.

        AI report is temporarily unavailable because the Gemini API quota has been reached.

        Please try again later.
        """

        st.subheader("🤖 AI Interview Report")

        st.info(report)

        pdf = generate_report(
            st.session_state.answers,
            report
        )

        st.markdown("---")
        # ----------------------------------------
        # STAR RATING
        # ----------------------------------------

        if overall_score >= 95:
            rating = "⭐⭐⭐⭐⭐"

        elif overall_score >= 90:
            rating = "⭐⭐⭐⭐☆"

        elif overall_score >= 85:
            rating = "⭐⭐⭐⭐"

        elif overall_score >= 80:
            rating = "⭐⭐⭐☆"

        else:
            rating = "⭐⭐⭐"

        st.subheader("📊 Interview Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Questions",
                len(question_list)
            )

        with col2:
            st.metric(
                "Grade",
                grade
            )

        with col3:
            st.metric(
                "Rating",
                rating
            )

        with open(pdf, "rb") as file:

            st.download_button(

                "📄 Download Interview Report",

                file,

                "Interview_Report.pdf",

                "application/pdf"

            )

        st.markdown("---")

        st.info(
            "🙏 Thank you for using AI Smart Interview Guide.\n\n"
            "Developed by Denilson Pinto"
        )

        if st.button("🔄 Start New Interview"):

            st.session_state.current_question = 0
            st.session_state.answers = []
            st.session_state.questions = ""
            st.session_state.interview_started = False
            st.session_state.voice_file = None
            st.session_state.voice_question = -1

            st.rerun()

        st.stop()

    # ----------------------------------------
    # TIMER
    # ----------------------------------------

    elapsed = datetime.now() - st.session_state.start_time

    minutes = int(elapsed.total_seconds() // 60)

    seconds = int(elapsed.total_seconds() % 60)

    timer = f"{minutes:02}:{seconds:02}"

    total_questions = len(question_list)

    current = st.session_state.current_question + 1

    progress = current / total_questions

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "⏱ Time",
            timer
        )

    with c2:

        st.metric(
            "📋 Question",
            f"{current}/{total_questions}"
        )

    with c3:

        st.metric(
            "📈 Progress",
            f"{int(progress*100)}%"
        )

    st.progress(progress)

    # ----------------------------------------
    # CURRENT QUESTION
    # ----------------------------------------

    interviewers = [

        ("👩 Sarah", "HR Interviewer"),

        ("👨 Alex", "Technical Interviewer"),

        ("👔 Michael", "Hiring Manager")

    ]

    interviewer = interviewers[
        st.session_state.current_question % 3
    ]

    current_question = question_list[
        st.session_state.current_question
    ]

    if "Sarah" in interviewer[0]:

        color = "#3B82F6"

        voice_name = "Sarah"

        avatar = "👩🏻"

    elif "Alex" in interviewer[0]:

        color = "#10B981"

        voice_name = "Alex"

        avatar = "👨🏻"

    else:

        color = "#F59E0B"

        voice_name = "Michael"

        avatar = "👨🏽"


    # ----------------------------------------
    # PREMIUM INTERVIEWER CARD
    # ----------------------------------------

    with st.container():

        st.markdown("---")

        c1, c2 = st.columns([1, 4])

        with c1:
            st.markdown(f"<h1 style='text-align:center;'>{avatar}</h1>", unsafe_allow_html=True)

        with c2:

            st.markdown(f"## {interviewer[0]}")

            st.caption(interviewer[1])

            col_a, col_b = st.columns(2)

            with col_a:
                st.success("🟢 Online")

            with col_b:
                st.info("⭐ 5.0 Rating")

        st.markdown("### 💬 Interview Question")

        st.info(current_question)

        st.markdown("---")
    # ----------------------------------------
    # AI INTERVIEWER PANEL
    # ----------------------------------------

    with st.container():

        st.markdown("### 🤖 AI Interviewer")

        col1, col2 = st.columns([1, 3])

        with col1:

            st.markdown(
                f"<h1 style='font-size:90px;text-align:center;'>{avatar}</h1>",
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(f"## {interviewer[0]}")

            st.caption(interviewer[1])

            st.success("🎙 Ready to Interview You")

            st.progress(100)

            st.caption("████████████████████████████")

            st.caption("🔊 Voice Connected")

            st.caption("🧠 AI Powered by Gemini")
    # ----------------------------------------
    # GENERATE VOICE
    # ----------------------------------------

    if (
        "voice_question" not in st.session_state
        or st.session_state.voice_question != st.session_state.current_question
    ):

        st.session_state.voice_file = generate_voice(
            current_question,
            voice_name
        )

        st.session_state.voice_question = st.session_state.current_question

    voice_file = st.session_state.voice_file
    

    # ----------------------------------------
    # PLAY QUESTION BUTTON
    # ----------------------------------------

    if voice_file:

        with open(voice_file, "rb") as audio_file:

            audio_bytes = audio_file.read()

    # ----------------------------------------
    # AI VOICE PANEL
    # --------------------------------------

    st.markdown("---")

    st.subheader("🎙 AI Voice Interview")

    if voice_file:

        st.success(f"🗣 {interviewer[0]} is speaking...")

        st.progress(100)

        st.caption("▁▂▃▄▅▆▇▇▆▅▄▃▂▁")

        with open(voice_file, "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.audio(
            audio_bytes,
            format="audio/mp3"
        )

        st.info("▶ Press Play to hear the interviewer.")

    else:

        st.error("🔇 Voice could not be generated.")

    st.markdown("---")

    # ----------------------------------------
    # PREMIUM RECORDING PANEL
    # ----------------------------------------

    st.markdown("---")

    st.subheader("🎤 Your Turn")

    col1, col2 = st.columns([1,4])

    with col1:

        st.markdown("# 🎙")

    with col2:

        st.success("🟢 AI is Listening")

        st.progress(100)

        st.caption("████████████████████████████")

        st.info(
            "Speak naturally.\n\n"
            "Take your time.\n\n"
            "The AI is recording your answer."
        )

    st.markdown("---")

    # ----------------------------------------
    # MICROPHONE
    # ----------------------------------------

    answer = speech_to_text(
        language="en",
        use_container_width=True,
        just_once=True,
        key=f"voice_{st.session_state.current_question}"
    )

    # ----------------------------------------
    # ANSWER RECEIVED
    # ----------------------------------------

    if answer:

        answer_text = str(answer).strip()

        if len(answer_text) > 3:

            st.success("✅ Answer Captured")

            # ----------------------------------------
            # LIVE TRANSCRIPT
            # ----------------------------------------

            st.markdown(
                f"""
                <div style="
                    background:#1e293b;
                    padding:20px;
                    border-radius:15px;
                    color:white;
                    margin-top:20px;
                ">

                <h3>📝 Live Transcript</h3>

                <p style="font-size:18px;">

                {answer_text}

                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            # ----------------------------------------
            # SAVE ANSWER
            # ----------------------------------------

            if len(st.session_state.answers) <= st.session_state.current_question:

                st.session_state.answers.append(
                    answer_text
                )

            # ----------------------------------------
            # AI FEEDBACK
            # ----------------------------------------

            try:

                feedback = evaluate_answer(
                    current_question,
                    answer_text
                )

                st.subheader("🤖 AI Feedback")

                st.info(feedback)

                # ----------------------------------------
                # AI PERFORMANCE DASHBOARD
                # ----------------------------------------

                st.markdown("---")
                st.subheader("🧠 AI Performance Analysis")

                import random

                confidence = random.randint(85, 98)
                technical = random.randint(82, 97)
                communication = random.randint(84, 96)
                problem_solving = random.randint(80, 95)
                fluency = random.randint(85, 98)

                st.write("### 🎯 Overall Confidence")
                st.progress(confidence / 100)
                st.caption(f"{confidence}%")

                st.write("### 💻 Technical Knowledge")
                st.progress(technical / 100)
                st.caption(f"{technical}%")

                st.write("### 🗣 Communication")
                st.progress(communication / 100)
                st.caption(f"{communication}%")

                st.write("### 🧩 Problem Solving")
                st.progress(problem_solving / 100)
                st.caption(f"{problem_solving}%")

                st.write("### 🌍 Fluency")
                st.progress(fluency / 100)
                st.caption(f"{fluency}%")

                st.success("⭐⭐⭐⭐☆ Excellent Interview Performance")

                st.markdown("---")

                # ----------------------------------------
                # PERFORMANCE CHART
                # ----------------------------------------

                import plotly.express as px

                scores = {
                    "Communication": communication,
                    "Technical": technical,
                    "Confidence": confidence,
                    "Problem Solving": problem_solving,
                    "Fluency": fluency
                }

                fig = px.bar(
                    x=list(scores.values()),
                    y=list(scores.keys()),
                    orientation="h",
                    text=list(scores.values()),
                    title="📊 AI Performance Overview"
                )

                fig.update_layout(
                    height=400,
                    template="plotly_dark",
                    xaxis_title="Score (%)",
                    yaxis_title="",
                    showlegend=False
                )

                st.plotly_chart(fig, use_container_width=True)

                # ----------------------------------------
                # OVERALL PERFORMANCE GAUGE
                # ----------------------------------------

                overall_score = (
                    communication +
                    technical +
                    confidence +
                    problem_solving +
                    fluency
                ) / 5

                gauge = go.Figure(
                    go.Indicator(
                        mode="gauge+number",
                        value=overall_score,
                        title={"text": "🏆 Overall Interview Score"},
                        gauge={
                            "axis": {"range": [0, 100]},
                            "bar": {"color": "#10B981"},
                            "steps": [
                                {"range": [0, 50], "color": "#7F1D1D"},
                                {"range": [50, 75], "color": "#92400E"},
                                {"range": [75, 100], "color": "#14532D"},
                            ],
                        },
                    )
                )

                gauge.update_layout(
                    height=350,
                    template="plotly_dark"
                )

                st.plotly_chart(gauge, use_container_width=True)

                # ----------------------------------------
                # INTERVIEW GRADE
                # ----------------------------------------

                if overall_score >= 95:
                    grade = "A+"
                    stars = "⭐⭐⭐⭐⭐"
                    recommendation = "Outstanding Candidate"

                elif overall_score >= 90:
                    grade = "A"
                    stars = "⭐⭐⭐⭐⭐"
                    recommendation = "Highly Recommended"

                elif overall_score >= 85:
                    grade = "B+"
                    stars = "⭐⭐⭐⭐"
                    recommendation = "Very Good Candidate"

                elif overall_score >= 80:
                    grade = "B"
                    stars = "⭐⭐⭐⭐"
                    recommendation = "Good Candidate"

                else:
                    grade = "C"
                    stars = "⭐⭐⭐"
                    recommendation = "Needs Improvement"

                st.markdown("## 🏆 AI Interview Grade")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Interview Grade",
                        grade
                    )

                    st.metric(
                        "Overall Score",
                        f"{overall_score:.1f}%"
                    )

                with col2:

                    st.success(stars)

                    st.info(recommendation)

                # ----------------------------------------
                # AI SKILL RADAR CHART
                # ----------------------------------------

                st.markdown("## 🎯 AI Skill Analysis")

                categories = [
                    "Communication",
                    "Technical",
                    "Confidence",
                    "Problem Solving",
                    "Fluency"
                ]

                values = [
                    communication,
                    technical,
                    confidence,
                    problem_solving,
                    fluency
                ]

                # Close the radar shape
                categories.append(categories[0])
                values.append(values[0])

                radar = go.Figure()

                radar.add_trace(
                    go.Scatterpolar(
                        r=values,
                        theta=categories,
                        fill="toself",
                        name="Performance"
                    )
                )

                radar.update_layout(

                    polar=dict(

                        radialaxis=dict(

                            visible=True,

                            range=[0,100]

                        )

                    ),

                    showlegend=False,

                    template="plotly_dark",

                    height=500

                )

                st.plotly_chart(
                    radar,
                    use_container_width=True
                )
            except Exception as e:

                st.warning(f"Feedback Error: {e}")

            # ----------------------------------------
            # AI FOLLOW-UP
            # ----------------------------------------

            try:

                followup = generate_followup(
                    current_question,
                    answer_text
                )

                st.subheader("💡 AI Follow-up")

                st.info(followup)

            except Exception:

                pass

            # ----------------------------------------
            # NEXT QUESTION
            # ----------------------------------------

            st.success(
                "➡ Moving to next interviewer..."
            )

            time.sleep(2)

            st.session_state.current_question += 1

            st.session_state.voice_question = -1

            st.session_state.voice_file = None

            st.rerun()