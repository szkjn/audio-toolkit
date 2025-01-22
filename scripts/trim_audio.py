import os
import argparse
from pydub import AudioSegment

def trim_to_first_30_seconds(input_file, output_file, duration_ms = 30000):
    """
    Trims the input audio file to the first 30 seconds and saves it as a new file.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the trimmed audio file.
    """
    # Determine format from extension; default to 'wav' if not mp3
    ext = os.path.splitext(input_file)[1].lower()
    audio_format = "mp3" if ext == ".mp3" else "wav"

    print(f"Processing '{input_file}' as {audio_format}...")

    # Load the audio file
    audio = AudioSegment.from_file(input_file, format=audio_format)

    # Trim to the first 30 seconds (30,000 milliseconds)
    trimmed_audio = audio[:duration_ms]

    # Save the trimmed audio file
    trimmed_audio.export(output_file, format="wav")
    print(f"Trimmed audio saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim audio files to the first n seconds.")
    parser.add_argument("input_file", type=str, help="Path to the input audio file.")
    parser.add_argument("output_file", type=str, help="Path to save the trimmed audio file.")
    parser.add_argument("duration_ms", type=str, help="Trimming duration (in milliseconds)")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        exit(1)

    trim_to_first_30_seconds(args.input_file, args.output_file, int(args.duration_ms))
