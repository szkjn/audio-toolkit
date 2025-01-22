import os
import argparse
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def remove_silence(input_file, output_file, silence_thresh=-40, min_silence_len=300, padding=200, merge_distance=400):
    """
    Remove silent parts from a single large audio file with padding.

    Parameters:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the output audio file.
        silence_thresh (int): Silence threshold in dBFS. Default is -40 dBFS.
        min_silence_len (int): Minimum silence length in milliseconds. Default is 300 ms.
        padding (int): Padding in milliseconds to add around non-silent segments. Default is 200 ms.
        merge_distance (int): Minimum gap between non-silent segments to consider them separate (default: 400 ms).

    Returns:
        None
    """
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    print("Detecting non-silent parts...")

    # Detect non-silent intervals
    nonsilent_intervals = detect_nonsilent(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    if not nonsilent_intervals:
        print("No non-silent audio detected. Output will be empty.")
        return

    print(f"Detected {len(nonsilent_intervals)} non-silent segments. Merging close segments...")

    # Merge close intervals
    merged_intervals = []
    for start, end in nonsilent_intervals:
        if merged_intervals and start - merged_intervals[-1][1] <= merge_distance:
            merged_intervals[-1][1] = end  # Extend the last interval
        else:
            merged_intervals.append([start, end])

    print(f"Merged into {len(merged_intervals)} segments.")

    # Concatenate the non-silent segments with padding
    output_audio = AudioSegment.empty()
    for start, end in merged_intervals:
        start = max(0, start - padding)  # Extend the start backward
        end = min(len(audio), end + padding)  # Extend the end forward
        output_audio += audio[start:end]

    # Export the output audio
    output_audio.export(output_file, format="wav")
    print(f"Output saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove silent parts from a large audio file with padding.")
    parser.add_argument("input_file", type=str, help="Path to the input audio file.")
    parser.add_argument("output_file", type=str, help="Path to save the output audio file.")
    parser.add_argument(
        "--silence_thresh",
        type=int,
        default=-40,
        help="Silence threshold in dBFS (default: -40 dBFS).",
    )
    parser.add_argument(
        "--min_silence_len",
        type=int,
        default=100,
        help="Minimum silence length in milliseconds (default: 100 ms).",
    )
    parser.add_argument(
        "--padding",
        type=int,
        default=200,
        help="Padding in milliseconds to add around non-silent segments (default: 200 ms).",
    )

    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        exit(1)

    remove_silence(
        args.input_file,
        args.output_file,
        silence_thresh=args.silence_thresh,
        min_silence_len=args.min_silence_len,
        padding=args.padding,
    )
