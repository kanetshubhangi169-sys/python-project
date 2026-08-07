import os
from datetime import datetime

import streamlit as st
import torch
import soundfile as sf

from transformers import AutoTokenizer, VitsModel

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Text to Speech",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Text to Speech using Hugging Face")
st.write("Convert text into speech using the Facebook MMS-TTS model.")

# ---------------------------
# Load Model (Loads Only Once)
# ---------------------------
@st.cache_resource
def load_model():
    model_name = "facebook/mms-tts-eng"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = VitsModel.from_pretrained(model_name)

    return tokenizer, model


with st.spinner("Loading Hugging Face Model..."):
    tokenizer, model = load_model()

st.success("✅ Model Loaded Successfully!")

# ---------------------------
# Create Audio Folder
# ---------------------------
os.makedirs("audio", exist_ok=True)

# ---------------------------
# User Input
# ---------------------------
text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type your text here..."
)

# ---------------------------
# Generate Button
# ---------------------------
if st.button("Generate Speech"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        with st.spinner("Generating Audio..."):

            inputs = tokenizer(text, return_tensors="pt")

            with torch.no_grad():
                output = model(**inputs).waveform

            filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"

            filepath = os.path.join("audio", filename)

            sf.write(
                filepath,
                output.squeeze().cpu().numpy(),
                model.config.sampling_rate
            )

        st.success("✅ Audio Generated Successfully!")

        # Play Audio
        st.audio(filepath)

        # Download Button
        with open(filepath, "rb") as file:
            st.download_button(
                label="⬇ Download Audio",
                data=file,
                file_name=filename,
                mime="audio/wav"
            )