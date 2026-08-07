from groq import Groq
from config import GROQ_API_KEY

# ---------------------------------------
# Create Groq Client
# ---------------------------------------

client = Groq(api_key=GROQ_API_KEY)


# ---------------------------------------
# Speech-to-Text Function
# ---------------------------------------

def speech_to_text(audio_path, language=None):
    """
    Converts speech to text using Groq Whisper.

    Parameters:
        audio_path (str): Path of recorded audio.
        language (str): Language code (en, hi, mr, gu)
                        None = Auto Detect

    Returns:
        str : Transcribed text
    """

    try:

        with open(audio_path, "rb") as audio_file:

            # Auto Detect Language
            if language is None:

                transcription = client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-large-v3-turbo",
                    response_format="text"
                )

            # Selected Language
            else:

                transcription = client.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-large-v3-turbo",
                    language=language,
                    response_format="text"
                )

        return transcription

    except FileNotFoundError:
        return "❌ Audio file not found."

    except Exception as e:
        return f"❌ Groq API Error:\n{e}"