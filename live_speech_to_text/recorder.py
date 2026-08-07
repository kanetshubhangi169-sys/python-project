import os
import sounddevice as sd
import soundfile as sf

# ---------------------------------------
# Audio Configuration
# ---------------------------------------

SAMPLE_RATE = 16000
CHANNELS = 1
OUTPUT_FOLDER = "recordings"
OUTPUT_FILE = "recording.wav"


# ---------------------------------------
# Check Microphone
# ---------------------------------------

def check_microphone():
    """
    Check whether an input microphone is available.
    """

    devices = sd.query_devices()

    input_devices = [
        device for device in devices
        if device["max_input_channels"] > 0
    ]

    if len(input_devices) == 0:
        raise RuntimeError("No microphone detected.")

    return True


# ---------------------------------------
# Record Audio
# ---------------------------------------

def record_audio(duration=30):

    # Validate duration
    if duration <= 0:
        raise ValueError("Duration must be greater than 0 seconds.")

    # Check microphone
    check_microphone()

    # Create recordings folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        OUTPUT_FILE
    )

    print(f"\n🎤 Recording for {duration} seconds...\n")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32"
    )

    sd.wait()

    sf.write(
        output_path,
        audio,
        SAMPLE_RATE
    )

    print("✅ Recording Saved")

    return output_path