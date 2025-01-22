import os
import argparse
from pydub import AudioSegment

def slice_audio_file(input_file, output_dir, slice_duration_ms=2000, fade_duration_ms=50):
    """
    Slices the given audio file into segments of slice_duration_ms with fade in/out applied,
    and saves them into the specified output directory with unique names.

    Args:
        input_file (str): Path to the input audio file.
        output_dir (str): Directory to save the sliced audio files.
        slice_duration_ms (int): Duration of each slice in milliseconds (default: 2000 ms).
        fade_duration_ms (int): Duration in milliseconds for both fade in and fade out (default: 50 ms).
    """
    # Determine format from extension; default to 'wav' if not mp3
    ext = os.path.splitext(input_file)[1].lower()
    audio_format = "mp3" if ext == ".mp3" else "wav"

    print(f"\nProcessing '{input_file}' as {audio_format}...")
    audio = AudioSegment.from_file(input_file, format=audio_format)
    total_duration = len(audio)
    print(f"Total duration: {total_duration / 1000.0:.2f} seconds.")
    
    num_slices = total_duration // slice_duration_ms
    print(f"Creating {num_slices} slices of {slice_duration_ms / 1000.0:.1f} seconds each with {fade_duration_ms} ms fade.")

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    for i in range(int(num_slices)):
        start = i * slice_duration_ms
        end = start + slice_duration_ms
        segment = audio[start:end]
        # Apply fade-in and fade-out
        segment = segment.fade_in(fade_duration_ms).fade_out(fade_duration_ms)
        # Create a unique filename combining the base name and the slice index.
        output_filename = os.path.join(output_dir, f"{base_name}_slice_{i:04d}.wav")
        segment.export(output_filename, format="wav")
        print(f"Exported {output_filename}")

    print("Slicing complete for:", input_file)

def process_all_audio_files(input_folder, slice_duration_ms=2000, fade_duration_ms=50):
    """
    Processes all audio files in the input_folder (supported formats: .wav and .mp3)
    and saves all slices into a 'slices/' subfolder within the input folder.
    """
    # Create the slices folder inside the input folder
    output_folder = os.path.join(input_folder, "slices")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        lower_file = filename.lower()
        if lower_file.endswith('.mp3') or lower_file.endswith('.wav'):
            input_file = os.path.join(input_folder, filename)
            slice_audio_file(input_file, output_folder, slice_duration_ms, fade_duration_ms)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Slice audio files into segments and save to a 'slices/' folder in the input folder.")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing input audio files.")
    parser.add_argument(
        "--slice_duration_ms",
        type=int,
        default=2000,
        help="Duration of each slice in milliseconds (default: 2000 ms).",
    )
    parser.add_argument(
        "--fade_duration_ms",
        type=int,
        default=50,
        help="Fade duration in milliseconds for each slice (default: 50 ms).",
    )

    args = parser.parse_args()

    process_all_audio_files(
        args.input_folder,
        slice_duration_ms=args.slice_duration_ms,
        fade_duration_ms=args.fade_duration_ms,
    )
