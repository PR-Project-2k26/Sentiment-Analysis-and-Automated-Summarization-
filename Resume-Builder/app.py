import streamlit as st
import os
import pandas as pd

from modules.history import (
    save_analysis,
    get_analysis_history,
    get_dashboard_stats
)
from streamlit_echarts import st_echarts
from modules.database import create_tables
from modules.parser import extract_resume_text
from modules.ats import calculate_ats
from modules.skills import (
    extract_skills,
    calculate_skill_match
)
from modules.suggestions import generate_suggestions
from modules.metrics import calculate_metrics
from modules.sections import detect_sections
from modules.score import calculate_resume_score
from modules.content_quality import evaluate_content_quality
from modules.ai_analyzer import analyze_resume_ai
from modules.career_roadmap import generate_career_roadmap

# Create database tables
create_tables()

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -------------------------------
# SIDEBAR
# -------------------------------

with st.sidebar:

    if "page" not in st.session_state:
        st.session_state.page = "🏠 Dashboard"

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📄 Resume Analysis",
            "📈 Progress Tracker"
        ],
        key="page"
    )
# -------------------------------
# DASHBOARD
# -------------------------------

if page == "🏠 Dashboard":

    st.markdown(
        """
        <div style="padding:40px;
                    border-radius:20px;
                    background:linear-gradient(135deg,#4F46E5,#7C3AED);
                    color:white;">

        <h1 style="margin-bottom:10px;">
        🚀 AI Resume Analyzer Pro
        </h1>

        <h4 style="font-weight:400;">
        Analyze your resume with AI, improve ATS score,
        identify skill gaps and build a personalized career roadmap.
        </h4>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    stats = get_dashboard_stats()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Resume Analyses",
            stats["total"]
        )

    with col2:

        st.metric(
            "🏆 Best Score",
            f'{stats["best"]}/100'
        )

    with col3:

        st.metric(
            "📈 Latest Score",
            f'{stats["latest"]}/100'
        )

    st.write("")
    st.subheader("✨ Features")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("## 🎯 ATS Analysis")

            st.write(
                "Checks ATS compatibility, formatting, sections and resume quality."
            )

    with col2:

        with st.container(border=True):

            st.markdown("## 🧠 Skill Gap Analysis")

            st.write(
                "Compares your resume against the job description and finds missing skills."
            )

    col3, col4 = st.columns(2)

    with col3:

        with st.container(border=True):

            st.markdown("## 🤖 AI Resume Review")

            st.write(
                "AI evaluates grammar, writing quality and professional tone."
            )

    with col4:

        with st.container(border=True):

            st.markdown("## 🛣 Career Roadmap")

            st.write(
                "Generates a personalized learning roadmap based on your skill gaps."
            )
# -------------------------------
# RESUME ANALYSIS
# -------------------------------

elif page == "📄 Resume Analysis":

    st.header("📄 Resume Analysis")

    uploaded_resume = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )


    job_description = st.text_area(
        "Paste Job Description",
        height=300,
        placeholder="Paste the complete Job Description here..."
    )

    if st.button("🚀 Analyze Resume"):

        if uploaded_resume is None:
            st.error("Please upload your resume.")

        elif job_description.strip() == "":
            st.error("Please paste the Job Description.")

        else:

            upload_path = os.path.join(
                "uploads",
                uploaded_resume.name
            )

            with open(upload_path, "wb") as f:
                f.write(uploaded_resume.getbuffer())

            st.success("Resume uploaded successfully!")

            resume_text = extract_resume_text(upload_path)

            resume_skills = extract_skills(resume_text)

            jd_skills = extract_skills(job_description)

            metrics = calculate_metrics(resume_text)

            sections = detect_sections(resume_text)

            content_quality = evaluate_content_quality(
                resume_text,
                metrics
            )

            ats_score, ats_report = calculate_ats(
                metrics,
                sections
            )

            skill_score, matched, missing = calculate_skill_match(
                resume_skills,
                jd_skills
            )

            resume_score, breakdown = calculate_resume_score(
                ats_score,
                skill_score,
                metrics,
                sections
            )

            from modules.history import save_analysis

            save_analysis(

                uploaded_resume.name,

                resume_score,

                ats_score,

                skill_score,

                breakdown["Content Quality"],

                breakdown["Resume Structure"],

                matched,

                missing
            )

            suggestions = generate_suggestions(
                resume_text,
                missing
            )


            st.success("✅ Analysis Completed Successfully!")

            # -----------------------------
            # Grade
            # -----------------------------

            if resume_score >= 90:
                grade = "Excellent"
                color = "#2ecc71"

            elif resume_score >= 75:
                grade = "Good"
                color = "#3498db"

            elif resume_score >= 60:
                grade = "Average"
                color = "#f39c12"

            else:
                grade = "Needs Improvement"
                color = "#e74c3c"

            # -----------------------------
            # Layout
            # -----------------------------

            left, center, right = st.columns([1.2, 2, 1.2])

            # -----------------------------
            # LEFT
            # -----------------------------

            with left:

                st.metric(
                    "ATS",
                    f"{ats_score}/20"
                )

                st.metric(
                    "Content",
                    f"{breakdown['Content Quality']}/20"
                )

            # -----------------------------
            # CENTER
            # -----------------------------

            with center:

                option = {
                    "series": [
                        {
                            "type": "gauge",
                            "startAngle": 90,
                            "endAngle": -270,
                            "pointer": {
                                "show": False
                            },
                            "progress": {
                                "show": True,
                                "overlap": False,
                                "roundCap": True,
                                "clip": False,
                                "itemStyle": {
                                    "color": color
                                }
                            },
                            "axisLine": {
                                "lineStyle": {
                                    "width": 22
                                }
                            },
                            "splitLine": {
                                "show": False
                            },
                            "axisTick": {
                                "show": False
                            },
                            "axisLabel": {
                                "show": False
                            },
                            "detail": {
                                "fontSize": 42,
                                "offsetCenter": [0, "0%"],
                                "formatter": "{value}/100"
                            },
                            "title": {
                                "offsetCenter": [0, "78%"],
                                "fontSize": 22
                            },
                            "data": [
                                {
                                    "value": resume_score,
                                    "name": grade
                                }
                            ]
                        }
                    ]
                }

                st_echarts(
                    options=option,
                    height="420px"
                )

            # -----------------------------
            # RIGHT
            # -----------------------------

            with right:

                st.metric(
                    "Job Match",
                    f"{skill_score}/40"
                )

                st.metric(
                    "Structure",
                    f"{breakdown['Resume Structure']}/20"
                )

            st.subheader("📊 Score Breakdown")

            limits = {
                "ATS Compatibility": 20,
                "Skill Match": 40,
                "Content Quality": 20,
                "Resume Structure": 20
            }

            for key, value in breakdown.items():

                st.write(f"**{key}**")

                st.progress(value / limits[key])

                st.caption(f"{value}/{limits[key]}")
            
            st.divider()
            st.subheader("🎯 ATS Compatibility Report")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### ✅ Strengths")

                for item in ats_report["strengths"]:
                    st.success(item)

            with col2:

                st.markdown("### ⚠ Improvements")

                for item in ats_report["improvements"]:
                    st.warning(item)

            
            st.subheader("🛠 Skills Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### ✅ Matched Skills")

                if matched:
                    for skill in sorted(matched):
                        st.success(skill)
                else:
                    st.info("No matched skills found.")

            with col2:

                st.markdown("### ❌ Missing Skills")

                if missing:
                    for skill in sorted(missing):
                        st.error(skill)
                else:
                    st.success("No missing skills 🎉")

            st.subheader("💡 Resume Suggestions")

            for suggestion in suggestions:
                st.write(f"• {suggestion}")

            with st.expander("View Extracted Resume Text"):
                st.text_area(
                    "Resume Text",
                    resume_text,
                    height=300
                )
                st.subheader("📊 Resume Metrics")

            col1, col2 = st.columns(2)

            st.subheader("📊 Resume Metrics")

            cols = st.columns(4)

            metrics_to_show = [
                ("Words", metrics["Words"]),
                ("Lines", metrics["Lines"]),
                ("Bullet Points", metrics["Bullet Points"]),
                ("Characters", metrics["Characters"])
            ]

            for col, (name, value) in zip(cols, metrics_to_show):

                with col:
                    st.metric(name, value)
            st.markdown("### 📇 Contact Information")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                if metrics["Email"]:
                    st.success("📧 Email")
                else:
                    st.error("📧 Email Missing")

            with c2:
                if metrics["Phone"]:
                    st.success("📱 Phone")
                else:
                    st.error("📱 Phone Missing")

            with c3:
                if metrics["LinkedIn"]:
                    st.success("💼 LinkedIn")
                else:
                    st.error("💼 LinkedIn Missing")

            with c4:
                if metrics["GitHub"]:
                    st.success("🐙 GitHub")
                else:
                    st.error("🐙 GitHub Missing")


            st.subheader("📝 Content Quality Analysis")

            col1, col2 = st.columns(2)

            items = list(content_quality.items())

            for i, (metric, score) in enumerate(items):

                if metric == "Overall":
                    continue

                with col1 if i % 2 == 0 else col2:

                    st.write(f"**{metric}**")
                    st.progress(score / 10)
                    st.caption(f"{score}/10")

            st.subheader("📑 Resume Sections")

            cols = st.columns(2)

            items = list(sections.items())

            half = (len(items) + 1) // 2

            with cols[0]:

                for section, present in items[:half]:

                    if present:
                        st.success(f"✅ {section}")
                    else:
                        st.error(f"❌ {section}")

            with cols[1]:

                for section, present in items[half:]:

                    if present:
                        st.success(f"✅ {section}")
                    else:
                        st.error(f"❌ {section}")

            with st.spinner("🤖 AI is reviewing your resume..."):
                ai_review = analyze_resume_ai(
                    resume_text,
                    job_description
                )

            st.subheader("🤖 AI Resume Review")

            with st.expander("View AI Review", expanded=True):
                st.markdown(ai_review)

            with st.spinner("🛣️ Generating Career Roadmap..."):
                roadmap = generate_career_roadmap(
                    resume_text,
                    job_description,
                    missing
                )

            st.subheader("🛣️ AI Career Roadmap")

            with st.expander("View Career Roadmap", expanded=False):
                st.markdown(roadmap)
# -------------------------------
# PROGRESS TRACKER
# -------------------------------

elif page == "📈 Progress Tracker":

    st.header("📈 Resume Progress Tracker")

    history = get_analysis_history()

    if not history:

        st.info("No previous analyses found.")

    else:

        # -----------------------------
        # Create DataFrame
        # -----------------------------

        df = pd.DataFrame(
            history,
            columns=[
                "Resume",
                "Date",
                "Overall",
                "ATS",
                "Job Match",
                "Content",
                "Structure"
            ]
        )

        # Make sure score columns are integers
        score_cols = [
            "Overall",
            "ATS",
            "Job Match",
            "Content",
            "Structure"
        ]

        for col in score_cols:
            df[col] = df[col].astype(int)

        # -----------------------------
        # Summary Cards
        # -----------------------------

        total = len(df)
        best = df["Overall"].max()
        latest = df.iloc[0]["Overall"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Analyses", total)

        with col2:
            st.metric("Best Score", f"{best}/100")

        with col3:
            st.metric("Latest Score", f"{latest}/100")

        # -----------------------------
        # Overall Score Chart
        # -----------------------------

        st.subheader("📈 Overall Score Progress")

        chart_df = df.iloc[::-1]

        st.line_chart(
            chart_df.set_index("Date")["Overall"]
        )

        # -----------------------------
        # Resume History Table
        # -----------------------------

        st.subheader("📋 Resume History")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # -----------------------------
        # Latest Comparison
        # -----------------------------

        if len(df) >= 2:

            current = df.iloc[0]
            previous = df.iloc[1]

            st.subheader("📊 Latest Comparison")

            c1, c2, c3, c4, c5 = st.columns(5)

            comparisons = [
                ("Overall", "Overall"),
                ("ATS", "ATS"),
                ("Job Match", "Job Match"),
                ("Content", "Content"),
                ("Structure", "Structure")
            ]

            for col, (title, key) in zip(
                [c1, c2, c3, c4, c5],
                comparisons
            ):

                with col:

                    st.metric(
                        title,
                        current[key],
                        current[key] - previous[key]
                    )