# Audio Toolkit

A Python toolkit for performing various audio processing tasks, such as:

- Removing silent audio files from a folder.
- Trimming silence from a single large audio file.
- Slicing audio files into smaller segments.
- Trimming audio to the first 30 seconds.

## Features

1. **Batch Remove Silent Files**:

   - Scan a folder of audio files and move files below a specified volume threshold to a subfolder.
   - Script: `batch_remove_silent_files.py`.
   - **Usage :**
     ```bash
     python scripts/batch_remove_silent_files.py /path/to/input/folder --threshold 0.02
     ```

2. **Trim Silence From Large Audio**:

   - Remove silent segments from a single large audio file, generating a continuous output.
   - Script: `remove_silence_from_audio.py`.
   - **Usage :**
     ```bash
     python scripts/remove_silent_from_audio.py input.wav output.wav --silence_thresh -40 --min_silence_len 300 --padding 200
     ```

3. **Slice Audio Into Segments**:

   - Slice a large audio file into smaller segments based on specified time intervals or silence thresholds.
   - Script: `slice_audio.py`.
   - **Usage :**
     ```bash
     python scripts/slice_audio.py /path/to/audio/file --slice_duration_ms 2000 --fade_duration_ms 50
     ```

4. **Trim Audio to First $n$ Seconds**:
   - Extract the first $n$ seconds of an audio file and save it as a new file.
   - Script: `trim_audio.py`.
   - **Usage :**
     ```bash
     python scripts/trim_audio.py input.wav output.wav
     ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/audio-toolkit.git
   cd audio-toolkit
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Additional notes

### How Loudness is Measured

RMS (Root Mean Square):

- The most common way to measure loudness is to calculate the RMS of the audio signal. It computes the average power of the waveform over its duration. RMS gives a single value representing the "overall" loudness of the file.

The formula for calculating RMS is:

$$
\text{RMS} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} x[i]^2}
$$

Where:

- $x[i]$ is the audio amplitude at sample $i$,
- $N$ is the total number of samples.

**Limitation:** RMS averages the loudness over the entire file. If 1.9 seconds are silent and the last 0.1 seconds is loud, the loud portion will affect the RMS but may not be representative of the whole file's "perceived" silence.
