import streamlit as st

def dashboard():

    st.title("🏠 Dashboard")

    st.success("Successfully Logged In")

    st.write("Welcome to AI Resume Analyzer Pro")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Resume Readiness", "--")

    with col2:
        st.metric("ATS Score", "--")

    st.divider()

    st.subheader("Upcoming Features")

    st.write("✅ Resume Analysis")
    st.write("✅ Skill Gap Analysis")
    st.write("✅ Recruiter Assessment")
    st.write("✅ Progress Tracker")