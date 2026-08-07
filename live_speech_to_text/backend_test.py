from recorder import record_audio
from groq_client import speech_to_text

# ---------------------------------------
# Language Selection
# ---------------------------------------

language_map = {
    1: ("Auto Detect", None),
    2: ("English", "en"),
    3: ("Hindi", "hi"),
    4: ("Marathi", "mr"),
    5: ("Gujarati", "gu"),
}

print("\n========== Multilingual Speech-to-Text ==========\n")

print("Select Language")

print("1. Auto Detect")
print("2. English")
print("3. Hindi")
print("4. Marathi")
print("5. Gujarati")

choice = int(input("\nEnter your choice (1-5): "))

if choice not in language_map:
    print("Invalid choice. Using Auto Detect.")
    choice = 1

language_name, language_code = language_map[choice]

# ---------------------------------------
# Recording Duration
# ---------------------------------------

duration = int(input("\nEnter recording duration (seconds): "))

print(f"\nSelected Language : {language_name}")
print(f"Recording Duration : {duration} seconds")

# ---------------------------------------
# Record Audio
# ---------------------------------------

audio_path = record_audio(duration)

print("\nUploading audio to Groq...")

# ---------------------------------------
# Speech to Text
# ---------------------------------------

text = speech_to_text(
    audio_path,
    language_code
)

print("\n========== RESULT ==========\n")

print(text)