import os
import whisper
import streamlit as st

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Speech to Text using Whisper",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Speech to Text using Whisper")

# -----------------------------
# Create Upload Folder
# -----------------------------
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Load Whisper Model (Only Once)
# -----------------------------
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")

model = load_whisper_model()

st.success("✅ Whisper Tiny Model Loaded Successfully")

# -----------------------------
# Upload Audio
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:

    # Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(filepath)

    if st.button("🎤 Convert Speech to Text"):

        with st.spinner("Converting... Please wait..."):

            result = model.transcribe(filepath)

        recognized_text = result["text"]

        st.success("✅ Conversion Completed")

        st.subheader("Recognized Text")

        st.write(recognized_text)