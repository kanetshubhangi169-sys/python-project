import os
import whisper
import streamlit as st

# ---------------------------------
# Streamlit Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Speech to Text using Whisper",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Speech to Text using Whisper")

# ---------------------------------
# Create Upload Folder
# ---------------------------------
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------------------------
# Load Whisper Model (Only Once)
# ---------------------------------
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")   # tiny, base, small, medium, large

with st.spinner("Loading Whisper Model..."):
    model = load_whisper_model()

st.success("✅ Whisper Tiny Model Loaded Successfully!")

# ---------------------------------
# Upload Audio File
# ---------------------------------
uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:

    # Save uploaded file
    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Play uploaded audio
    st.audio(filepath)

    # Convert Button
    if st.button("🎤 Convert Speech to Text"):

        with st.spinner("Converting audio to text..."):

            try:

                # Speech-to-Text
                result = model.transcribe(filepath)

                recognized_text = result["text"]

                st.success("✅ Conversion Completed!")

                st.subheader("Recognized Text")

                st.write(recognized_text)

                # Save transcription
                text_file = os.path.join(
                    UPLOAD_FOLDER,
                    "transcription.txt"
                )

                with open(
                    text_file,
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write(recognized_text)

                # Download Button
                with open(text_file, "rb") as f:

                    st.download_button(
                        label="📥 Download Transcription",
                        data=f,
                        file_name="transcription.txt",
                        mime="text/plain"
                    )

            except Exception as e:

                st.error(f"❌ Error: {e}")