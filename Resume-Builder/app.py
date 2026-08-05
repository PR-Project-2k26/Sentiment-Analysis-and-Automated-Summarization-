import os
import streamlit as st
import pandas as pd

from streamlit_echarts import st_echarts

# -----------------------------
# Backend Modules
# -----------------------------
from modules.suggestions import generate_suggestions
from modules.database import create_tables
from modules.parser import extract_resume_text
from modules.metrics import calculate_metrics
from modules.sections import detect_sections
from modules.ats import calculate_ats
from modules.skills import analyze_job_match
from modules.content_quality import evaluate_content_quality
from modules.score import calculate_resume_score
from modules.suggestions import generate_suggestions
from modules.ai_analyzer import analyze_resume_ai
from modules.career_roadmap import generate_career_roadmap

from modules.history import (
    save_analysis,
    get_analysis_history,
    get_dashboard_stats
)

# ---------------------------------
# Database
# ---------------------------------

create_tables()

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
}

.stMetric{
    border-radius:15px;
}

.hero{

padding:30px;

border-radius:18px;

background:linear-gradient(135deg,#2563eb,#7c3aed);

color:white;

margin-bottom:20px;

}

.small-card{

padding:18px;

border-radius:15px;

background:#111827;

border:1px solid #2d3748;

}

</style>
""", unsafe_allow_html=True)

# =====================================
# Sidebar
# =====================================

with st.sidebar:

    st.title("📄 AI Resume Analyzer")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📈 Progress Tracker"
        ]
    )

    st.markdown("---")

    st.markdown("### Features")

    st.success("✓ ATS Compatibility")

    st.success("✓ Skill Gap Analysis")

    st.success("✓ AI Resume Review")

    st.success("✓ Career Roadmap")

    st.success("✓ Progress Tracker")


# =====================================
# Dashboard
# =====================================

if page == "🏠 Dashboard":

    st.markdown(
        """
        <div class="hero">

        <h1>🚀 AI Resume Analyzer Pro</h1>

        <p style="font-size:18px;">
        Upload your resume, compare it with any Job Description,
        discover missing skills, improve ATS score,
        and receive AI-powered career guidance.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    stats = get_dashboard_stats()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 Total Analyses",
            stats["total"]
        )

    with col2:
        st.metric(
            "🏆 Highest Score",
            f"{stats['best']}/100"
        )

    with col3:
        st.metric(
            "📈 Latest Score",
            f"{stats['latest']}/100"
        )

        st.write("")

    st.subheader("✨ What This Analyzer Does")

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.markdown("### 🎯 ATS Compatibility")

            st.caption(
                "Evaluate formatting, resume structure and ATS friendliness."
            )

        with st.container(border=True):

            st.markdown("### 🤖 AI Resume Review")

            st.caption(
                "AI checks grammar, readability, tone and resume quality."
            )

    with right:

        with st.container(border=True):

            st.markdown("### 🧠 Skill Gap Analysis")

            st.caption(
                "Compare your resume with the Job Description."
            )

        with st.container(border=True):

            st.markdown("### 🛣 Career Roadmap")

            st.caption(
                "Get a personalized roadmap to improve missing skills."
            )
            st.write("")
    st.divider()

    st.subheader("📄 Resume Analysis")

    left, right = st.columns([1, 1.5])

    # -----------------------------
    # Resume Upload
    # -----------------------------
    with left:

        st.markdown("### Upload Resume")

        uploaded_resume = st.file_uploader(
            "Choose a PDF Resume",
            type=["pdf"],
            help="Upload your resume in PDF format."
        )

        if uploaded_resume:
            st.success(f"✅ {uploaded_resume.name}")

    # -----------------------------
    # Job Description
    # -----------------------------
    with right:

        st.markdown("### Job Description")

        job_description = st.text_area(
            "Paste the Job Description",
            height=280,
            placeholder="Paste the complete job description here..."
        )

        st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True,
            type="primary"
        )

        if analyze:

            if uploaded_resume is None:

                st.error("Please upload your resume.")

            elif job_description.strip() == "":

                st.error("Please paste the Job Description.")

            else:

                os.makedirs("uploads", exist_ok=True)

                upload_path = os.path.join(
                    "uploads",
                    uploaded_resume.name
                )

                with open(upload_path, "wb") as f:
                    f.write(uploaded_resume.getbuffer())

                with st.spinner("Analyzing your resume..."):

                    resume_text = extract_resume_text(upload_path)

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

                    job_match = analyze_job_match(
                        resume_text,
                        job_description
                    )

                    resume_score, breakdown = calculate_resume_score(
                        ats_score,
                        job_match,
                        metrics,
                        sections,
                        content_quality
                    )
                    matched = (
                        job_match["technical"]["matched"]
                        + job_match["frameworks"]["matched"]
                    )

                    missing = (
                        job_match["technical"]["missing"]
                        + job_match["frameworks"]["missing"]
                    )
                    suggestions = generate_suggestions(

                        metrics,

                        sections,

                        missing,

                        job_match,

                        ats_report,

                        content_quality

                    )

                                    # ============================================
                # RESULT HEADER
                # ============================================

                st.write("")
                st.divider()
                st.header("📊 Resume Analysis Results")

                # -----------------------------
                # Verdict
                # -----------------------------

                if resume_score >= 90:
                    verdict = "🟢 Excellent Resume"
                    color = "#22c55e"

                elif resume_score >= 75:
                    verdict = "🔵 Good Resume"
                    color = "#2563eb"

                elif resume_score >= 60:
                    verdict = "🟡 Average Resume"
                    color = "#f59e0b"

                else:
                    verdict = "🔴 Needs Improvement"
                    color = "#ef4444"

                matched = (
                    job_match["technical"]["matched"]
                    + job_match["frameworks"]["matched"]
                )

                missing = (
                    job_match["technical"]["missing"]
                    + job_match["frameworks"]["missing"]
                )

                save_analysis(
                    uploaded_resume.name,
                    resume_score,
                    ats_score,
                    job_match["score"],
                    breakdown["Content Quality"],
                    breakdown["Resume Structure"],
                    matched,
                    missing
                )

                st.markdown(
                    f"""
                    <div style="
                        background:{color};
                        padding:25px;
                        border-radius:18px;
                        text-align:center;
                        color:white;
                        margin-bottom:20px;
                    ">

                    <h1 style="margin:0;font-size:60px;">
                    {resume_score}/100
                    </h1>

                    <h3>{verdict}</h3>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "🎯 ATS Compatibility",
                        f"{ats_score}/20"
                    )

                with col2:
                    st.metric(
                        "💼 Job Match",
                        f"{job_match['score']}/40"
                    )

                with col3:
                    st.metric(
                        "📝 Content",
                        f"{breakdown['Content Quality']}/20"
                    )

                with col4:
                    st.metric(
                        "📑 Structure",
                        f"{breakdown['Resume Structure']}/20"
                    )

                st.write("")
                st.subheader("📈 Score Breakdown")

                score_data = [
                    ("ATS Compatibility", breakdown["ATS Compatibility"], 20),
                    ("Job Match", breakdown["Job Match"], 40),
                    ("Content Quality", breakdown["Content Quality"], 20),
                    ("Resume Structure", breakdown["Resume Structure"], 20),
                ]

                for title, score, total in score_data:

                    st.markdown(f"**{title}**")

                    st.progress(score / total)

                    st.caption(f"{score}/{total}")

                    st.write("")

                    st.divider()

                analysis_tab1, analysis_tab2, analysis_tab3, analysis_tab4, analysis_tab5, analysis_tab6 = st.tabs(
                    [
                        "🎯 ATS Compstibility Analysis",
                        "📊 Resume Analysis of skills",
                        "📝 Content Quality",
                        "🤖 AI Review",
                        "🛣 Career Roadmap",
                        "📄 Resume Details",
                    ]
                )

                with analysis_tab1:

                    st.subheader("🎯 ATS Compatibility Report")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.markdown("#### ✅ Strengths")

                        for item in ats_report["strengths"]:
                            st.success(item)

                    with col2:

                        st.markdown("#### ⚠ Improvements")

                        for item in ats_report["improvements"]:
                            st.warning(item)


                with analysis_tab2:

                    st.subheader("📊 Job Match Breakdown")

                    c1, c2, c3, c4, c5 = st.columns(5)

                    with c1:
                        st.metric("Technical", f'{job_match["technical"]["score"]}/15')

                    with c2:
                        st.metric("Frameworks", f'{job_match["frameworks"]["score"]}/8')

                    with c3:
                        st.metric("Projects", f'{job_match["projects"]["score"]}/7')

                    with c4:
                        st.metric("Experience", f'{job_match["experience"]["score"]}/5')

                    with c5:
                        st.metric("Action", f'{job_match["action"]["score"]}/5')

                    st.divider()

                    st.subheader("🛠 Skills Analysis")

                    left, right = st.columns(2)

                    with left:

                        st.markdown("### ✅ Matched Skills")

                        if matched:
                            for skill in sorted(matched):
                                st.success(skill)
                        else:
                            st.info("No matched skills found.")

                    with right:

                        st.markdown("### ❌ Missing Skills")

                        if missing:
                            for skill in sorted(missing):
                                st.error(skill)
                        else:
                            st.success("No missing skills 🎉")

                    st.divider()

                    # ==========================================
                    # PROJECT EVALUATION
                    # ==========================================

                    st.subheader("📂 Project Evaluation")

                    st.info(job_match["projects"]["reason"])

                    st.write("")

                    # ==========================================
                    # EXPERIENCE EVALUATION
                    # ==========================================

                    st.subheader("💼 Experience Evaluation")

                    st.info(job_match["experience"]["reason"])

                    st.write("")

                    # ==========================================
                    # ACTION KEYWORDS
                    # ==========================================

                    st.subheader("🚀 Strong Action Keywords")

                    if job_match["action"]["keywords"]:

                        cols = st.columns(4)

                        for i, word in enumerate(job_match["action"]["keywords"]):

                            with cols[i % 4]:
                                st.success(word)

                    else:

                        st.info("No strong action keywords detected.")

                    
                    st.divider()

                    st.subheader("💡 Resume Suggestions")

                    for level in [
                        "High Priority",
                        "Medium Priority",
                        "Low Priority"
                    ]:

                        if suggestions[level]:

                            st.markdown(f"### {level}")

                            for item in suggestions[level]:
                                st.write(f"• {item}")

                with analysis_tab3:

                    st.subheader("📝 Content Quality")

                    cols = st.columns(4)

                    items = [
                        (k, v)
                        for k, v in content_quality.items()
                        if k not in ("Overall", "Feedback")
                    ]

                    for i, (metric, score) in enumerate(items):

                        with cols[i % 4]:

                            if score >= 8:
                                st.success(f"### {score}/10")
                            elif score >= 6:
                                st.warning(f"### {score}/10")
                            else:
                                st.error(f"### {score}/10")

                            st.caption(metric)

                    st.divider()

                    st.subheader("💡 AI Writing Suggestions")

                    for item in content_quality["Feedback"]:
                        st.info(item)


                with analysis_tab4:

                    st.subheader("🤖 AI Resume Review")

                    with st.spinner("Analyzing resume..."):

                        ai_review = analyze_resume_ai(
                            resume_text,
                            job_description
                        )

                    st.markdown(ai_review)


                with analysis_tab5:

                    st.subheader("🛣 Personalized Career Roadmap")

                    with st.spinner("Generating roadmap..."):

                        roadmap = generate_career_roadmap(
                            resume_text,
                            job_description,
                            missing
                        )

                    st.markdown(roadmap)
                   



# ==========================================================
# PROGRESS TRACKER
# ==========================================================

elif page == "📈 Progress Tracker":

    st.title("📈 Resume Progress Tracker")

    history = get_analysis_history()

    if not history:

        st.info("No previous resume analyses found.")

    else:

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

        score_columns = [
            "Overall",
            "ATS",
            "Job Match",
            "Content",
            "Structure"
        ]

        for col in score_columns:
            df[col] = df[col].astype(int)

        st.subheader("📊 Summary")

        total = len(df)
        best = df["Overall"].max()
        latest = df.iloc[0]["Overall"]

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Analyses",
            total
        )

        c2.metric(
            "Best Score",
            f"{best}/100"
        )

        c3.metric(
            "Latest Score",
            f"{latest}/100"
        )

        st.divider()

        st.subheader("📈 Overall Score Progress")

        chart_df = df.iloc[::-1]

        st.line_chart(
            chart_df.set_index("Date")["Overall"]
        )

        st.divider()

        st.subheader("📋 Resume History")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        if len(df) >= 2:

            st.divider()

            st.subheader("📊 Latest Comparison")

            current = df.iloc[0]
            previous = df.iloc[1]

            cols = st.columns(5)

            comparisons = [
                ("Overall", "Overall"),
                ("ATS", "ATS"),
                ("Job Match", "Job Match"),
                ("Content", "Content"),
                ("Structure", "Structure"),
            ]

            for col, (title, key) in zip(cols, comparisons):

                with col:

                    st.metric(
                        title,
                        current[key],
                        current[key] - previous[key]
                    )