import io
import streamlit as st
from utils import summarize_text, generate_wordcloud_image

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("🧠 Text Summarizer & Insight Dashboard")
st.caption("Summarize text and see sentiment, keywords, readability, and stats at a glance.")

if "history" not in st.session_state:
    st.session_state.history = []  # list of dicts: {input, result, length}

# ---------------------------------------------------------------------------
# Input controls
# ---------------------------------------------------------------------------
user_input = st.text_area("Enter your text here:", height=200)

col1, col2 = st.columns([2, 1])
with col1:
    length_choice = st.radio(
        "Summary length", ["Short", "Medium", "Long"], index=1, horizontal=True
    )
with col2:
    st.write("")
    st.write("")
    run_button = st.button("Summarize", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Run summarization
# ---------------------------------------------------------------------------
if run_button:
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner("Generating summary..."):
            result = summarize_text(user_input, length=length_choice)

        if result.get("error"):
            st.error(result["error"])
        else:
            st.session_state.history.insert(
                0, {"input": user_input, "result": result, "length": length_choice}
            )

# ---------------------------------------------------------------------------
# Render a single result (summary + dashboard)
# ---------------------------------------------------------------------------
def render_result(entry, key_prefix):
    result = entry["result"]

    st.subheader("Summary")
    st.write(result["summary"])
    st.download_button(
        "⬇ Download this summary",
        data=result["summary"],
        file_name="summary.txt",
        mime="text/plain",
        key=f"{key_prefix}_download",
    )

    # --- Stats row ---
    stats = result["stats"]
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Original words", stats["original_words"])
    m2.metric("Summary words", stats["summary_words"])
    m3.metric("Compression", f"{stats['compression_pct']}%")
    m4.metric("Reading time saved", f"{max(0, stats['reading_time_original_sec'] - stats['reading_time_summary_sec'])}s")

    # --- Sentiment ---
    st.subheader("Sentiment")
    sc1, sc2 = st.columns([1, 1])
    with sc1:
        st.write(f"**LLM tone label:** {result['emotion'] or 'N/A'}")
        st.write(f"**Readability:** {result['readability'] or 'N/A'}")
    with sc2:
        sentiment = result["sentiment"]
        st.bar_chart(
            {
                "Positive": sentiment.get("positive", 0),
                "Neutral": sentiment.get("neutral", 0),
                "Negative": sentiment.get("negative", 0),
            }
        )

    # --- Topics & Keywords ---
    tc1, tc2 = st.columns(2)
    with tc1:
        st.markdown("**Key Topics**")
        for topic in result["topics"]:
            st.markdown(f"- {topic}")
    with tc2:
        st.markdown("**Keywords**")
        st.write(", ".join(result["keywords"]) if result["keywords"] else "N/A")

    # --- Word cloud ---
    img = generate_wordcloud_image(result["keywords"], fallback_text=result["summary"])
    if img is not None:
        st.markdown("**Word Cloud**")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        st.image(buf.getvalue(), use_container_width=True)

    st.caption(f"Model latency: {result['latency_sec']}s · Length setting: {entry['length']}")


# ---------------------------------------------------------------------------
# Show latest result + history
# ---------------------------------------------------------------------------
if st.session_state.history:
    st.divider()
    render_result(st.session_state.history[0], key_prefix="latest")

    if len(st.session_state.history) > 1:
        st.divider()
        with st.expander(f"📜 History ({len(st.session_state.history) - 1} earlier)"):
            for i, entry in enumerate(st.session_state.history[1:], start=1):
                st.markdown(f"**#{i} — {entry['input'][:60]}{'...' if len(entry['input']) > 60 else ''}**")
                render_result(entry, key_prefix=f"hist_{i}")
                st.markdown("---")

        if st.button("Clear history"):
            st.session_state.history = []
            st.rerun()
