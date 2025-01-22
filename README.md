# Silence Processor

A Python toolkit for performing various audio processing tasks, such as:

- Removing silent audio files from a folder.
- Trimming silence from a single large audio file.

## How Loudness is Measured

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

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/silence-processor.git
   cd silence-processor

   ```

2. Create a virtual environment

3. Install dependencies
