from gtts import gTTS   # Google Text-to-Speech(TTS) library
import os               # Provides functions to interact with the operating system
import ffmpeg           # FFmpeg's Python API is used for processing video and audio
from pydub import AudioSegment   # Used to get the duration of an audio file
from typing import Optional  # `Optional[T]` means the value can be of type `T` or `None`. or 

class LipProcessor:
    def __init__(self, BASE_DIR: str) -> None:
        # Initialize file paths based on the base directory
        self.BASE_DIR = BASE_DIR
        self.avatar_path = os.path.join(BASE_DIR, "avatar.jpg") # Define file paths for avatar, audio, video, and final output
        self.audio_path = os.path.join(BASE_DIR, "audio.mp3")
        self.video_path = os.path.join(BASE_DIR, "video.mp4")
        #self.output_path = os.path.join(BASE_DIR, "final_output.mp4")

    def convert_mp3_to_wav(self, mp3_path: str, wav_path: str) -> bool:    # Convert an mp3 to file to wav format using ffmpeg
        try:
            ffmpeg.input(mp3_path).output(wav_path, ar=16000, ac=1).run(overwrite_output=True)
            print(f"Converted {mp3_path} to {wav_path}")
            return True
        except Exception as e:
            print(f"Failed to convert mp3 to wav. Error: {e}")  
            return False # Conversion failed

    def get_audio_duration(self) -> Optional[float]: # or float | None    Calculate and return the duration of speech audio file
        try:
            audio = AudioSegment.from_file(self.audio_path)   
            return audio.duration_seconds
        except Exception as e:
            print(f"Failed to retrieve audio duration. Error: {e}")  
            return None # No valid duration available

    def text_to_speech(self, text: str) -> Optional[str]:
        try:
            # Convert text to speech and save as an MP3 file
            tts = gTTS(text, lang="en") 
            tts.save(self.audio_path) 
            print("Audio file created (MP3).")  

            wav_path = self.audio_path.replace(".mp3", ".wav")
            flag = self.convert_mp3_to_wav(self.audio_path, wav_path) 

            if not flag:
                print("Error: Failed to convert Mp3 to wav.")
                return None  # Return None if conversion fails
            
            print("Converted MP3 to wav")
            return wav_path # Return the WAV file path

        except Exception as e:
            print(f"Failed to create speech audio. Error: {e}") 
            return None # Return None if there is an error

    def image_to_video(self) -> None: # Convert avatar image to a video
        duration = self.get_audio_duration() # Get the duration
        try:
            #ffmpeg.input(self.avatar_path, loop=1).output(self.video_path, t=duration, vf="scale=1920:1080", vcodec="libx264", pix_fmt="yuv420p", r=30).run(overwrite_output=True)
            ffmpeg.input(self.avatar_path, loop=1).output(self.video_path, t=duration, vf="scale=1280:720", vcodec="libx264", pix_fmt="yuv420p").run(overwrite_output=True)
            print("Video file created.")
        except Exception as e:
            print(f"Failed to create video. Error: {e}")
                   
                     

