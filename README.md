!!! Important Notice !!!

Due to my hardware limitations, running this project on a GPU caused my computer to crash. Therefore, I executed the project using CPU instead. As a result, the video quality may be lower. Please take this into consideration.

Lip Sync Project (Using Wav2Lip)

This project generates a talking avatar by syncing an audio file with a static image. It uses Wav2Lip to create realistic lip movements by mapping facial movements to speech audio.

** If your hardware is powerful, delete line 158 in the inference.py file inside Wav2Lip-master and uncomment line 157 to enable GPU   acceleration

📌 Features

Converts text to speech (TTS) using gTTS.

Creates a video from an image using FFmpeg.

Runs lip-sync processing with Wav2Lip.

Works with both CPU and GPU (faster performance on GPU).

Supports various audio and video formats.

Provides a modular structure for easy modification.

🛠️ Requirements

Make sure you have installed:

Python 3.x

FFmpeg

gTTS

pydub

Wav2Lip (download from GitHub)

torch and torchvision (for deep learning models)

dotenv (for managing environment variables)

🚀 How to Use

Set up environment variables by creating a .env file and adding:
BASE_DIR=your/project/path

Run the main script: python main.py

The final synced video will be saved as final_output.mp4.

🎞️ How It Works

Text-to-Speech (TTS) converts input text to speech using gTTS and saves it as an MP3 file.

The MP3 file is converted into WAV format for better compatibility with Wav2Lip.

The avatar image is turned into a video of the same duration as the audio.

Wav2Lip syncs the lip movements of the avatar with the generated audio.

The processed video is saved as final_output.mp4.

🖥️ Running on GPU (Optional but Recommended)

By default, Wav2Lip runs on CPU, which can be slow. To use a GPU, install CUDA-compatible PyTorch and modify the Wav2Lip command in lip_sync.py to enable GPU acceleration.


