import os
import sys
import shutil
import argparse

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.audio_utils import is_silent

def move_silent_files(input_folder, threshold):
    """
    Scan WAV files in `input_folder` and move silent/low-volume files to a subfolder.

    Parameters:
        input_folder (str): Path to the folder containing WAV files.
        threshold (float): Volume threshold for classifying silence.
    """
    # Define the output folder as a subfolder of the input folder
    output_folder = os.path.join(input_folder, "silent_files")
    os.makedirs(output_folder, exist_ok=True)
    
    # Initialize counters
    total_files = 0
    silent_files = 0

    # Scan through files in the input folder
    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)
        if filename.lower().endswith(".wav"):
            total_files += 1
            try:
                # Check if the file is silent
                if is_silent(filepath, threshold):
                    silent_files += 1
                    shutil.move(filepath, os.path.join(output_folder, filename))
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Summary of the process
    print(f"Total WAV files in folder: {total_files}")
    print(f"Silent files flagged and moved: {silent_files}")
    print(f"Remaining files in folder: {total_files - silent_files}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Filter and move silent WAV files.")
    parser.add_argument("input_folder", help="Path to the folder containing WAV files.")
    parser.add_argument("--threshold", type=float, default=0.1,
                        help="Volume threshold for classifying silence (default: 0.1).")
    args = parser.parse_args()

    move_silent_files(args.input_folder, args.threshold)
