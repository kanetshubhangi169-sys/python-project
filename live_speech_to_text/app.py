import streamlit as st
from recorder import record_audio
from groq_client import speech_to_text

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Multilingual Speech-to-Text",
    page_icon="🎤",
    layout="wide"
)

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("⚙️ Settings")

language = st.sidebar.selectbox(
    "Select Language",
    [
        "Auto Detect",
        "English",
        "Hindi",
        "Marathi",
        "Gujarati"
    ]
)

duration = st.sidebar.slider(
    "Recording Duration (Seconds)",
    min_value=5,
    max_value=60,
    value=30
)

st.sidebar.markdown("---")

st.sidebar.write("### Model")
st.sidebar.success("whisper-large-v3-turbo")

st.sidebar.markdown("---")

st.sidebar.info(
    """
This project converts speech into text
using the **Groq API** and
**Whisper Large V3 Turbo**.
"""
)

# -----------------------------------
# Language Mapping
# -----------------------------------

language_map = {
    "Auto Detect": None,
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu"
}

selected_language = language_map[language]

# -----------------------------------
# Main UI
# -----------------------------------

st.title("🎤 Multilingual Speech-to-Text")

st.write(
    """
Record your voice and convert it into text
using **Groq Whisper Large V3 Turbo**.
"""
)

st.divider()

# -----------------------------------
# Record Button
# -----------------------------------

if st.button("🎙️ Start Recording", use_container_width=True):

    try:

        st.info(f"🎤 Recording for {duration} seconds...")

        audio_path = record_audio(duration)

        st.success("✅ Recording Completed")

        st.divider()

        st.subheader("🎵 Recorded Audio")

        st.audio(audio_path)

        st.info("☁️ Uploading audio to Groq...")

        text = speech_to_text(
            audio_path,
            selected_language
        )

        st.success("✅ Transcription Completed")

        st.divider()

        st.subheader("📝 Recognized Text")

        st.text_area(
            label="Transcript",
            value=text,
            height=220
        )

        st.download_button(
            label="📄 Download Transcript",
            data=text,
            file_name="transcript.txt",
            mime="text/plain",
            use_container_width=True
        )

    except Exception as e:

        st.error(f"❌ {e}")

st.divider()

st.caption(
    "Powered by Groq API • Whisper Large V3 Turbo • Streamlit"
)