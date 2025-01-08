import os
from src.config import DEEPGRAM_API_KEY
from pathlib import Path
import ffmpeg

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

class TTSHandler:
    def __init__(self):
        self.deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    def generate_audio(self, text, voice_id, output_filename):
        """
        Generate audio for the given text using Deepgram.
        Args:
            text (str): The text to convert to speech.
            voice_id (str): The Deepgram voice model ID.
            output_filename (str): The filename for the generated audio.
        Returns:
            str: Path to the generated audio file.
        """
        try:
            options = SpeakOptions(model=voice_id)
            _ = self.deepgram.speak.v("1").save(output_filename, {"text": text}, options)
            print("Speech generated successfully as file: " + output_filename)
            return output_filename
        except Exception as e:
            print(f"Error generating TTS audio: {e}")
            return None
    
    def combine_audio(self, input_files, output_file):
        """
        Combines a list of MP3 files into a single output file.

        Args:
            input_files: A list of paths to the input MP3 files.
            output_file: The path to the output MP3 file.

        Returns:
            str: The path to the combined output file, or None if an error occurs.
        """
        try:

            # Normalize paths and check existence
            normalized_files = []
            for file in input_files:
                normalized_path = Path(file).resolve().as_posix()
                print(f" - {normalized_path}")
                if not os.path.exists(normalized_path):
                    print(f"   [ERROR] File not found: {normalized_path}")
                    return None
                normalized_files.append(normalized_path)

            # Normalize output file path
            output_path = Path(output_file).resolve().as_posix()
            print(f"Output file will be saved as: {output_path}")

            # Run ffmpeg
            input_args = [ffmpeg.input(f) for f in normalized_files]
            ffmpeg.concat(*input_args, v=0, a=1).output(output_path).run()
            print(f"Successfully combined audio files into: {output_path}")
            return output_path
        except ffmpeg.Error as e:
            print(f"Error combining audio files: {e.stderr.decode() if hasattr(e, 'stderr') else str(e)}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        