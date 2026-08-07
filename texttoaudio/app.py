import os
import streamlit as st
import soundfile as sf
from ollama import chat
from kokoro import KPipeline

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Text to Speech",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 AI Text to Speech using Ollama + Kokoro")

# ----------------------------
# Create Audio Folder
# ----------------------------
AUDIO_FOLDER = "audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

# ----------------------------
# Load Kokoro Pipeline (Loads Only Once)
# ----------------------------
@st.cache_resource
def load_pipeline():
    return KPipeline(lang_code="a")

pipeline = load_pipeline()

st.success("✅ Kokoro Model Loaded Successfully!")

# ----------------------------
# User Input
# ----------------------------
prompt = st.text_area(
    "Enter your prompt",
    height=180,
    placeholder="Ask anything..."
)

# ----------------------------
# Generate Button
# ----------------------------
if st.button("Generate Response"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:

        with st.spinner("Generating response from Ollama..."):

            try:

                # Generate text using Ollama
                response = chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                response_text = response["message"]["content"]

                st.subheader("Generated Text")
                st.write(response_text)

                output_path = os.path.join(
                    AUDIO_FOLDER,
                    "output.wav"
                )

                with st.spinner("Generating speech..."):

                    generator = pipeline(
                        response_text,
                        voice="af_heart"
                    )

                    for _, _, audio in generator:
                        sf.write(
                            output_path,
                            audio,
                            24000
                        )

                st.success("✅ Audio Generated Successfully!")

                st.audio(output_path)

                with open(output_path, "rb") as file:

                    st.download_button(
                        label="⬇ Download Audio",
                        data=file,
                        file_name="output.wav",
                        mime="audio/wav"
                    )

            except Exception as e:

                st.error(f"Error: {e}")