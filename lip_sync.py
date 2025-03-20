import os          # OS functions
import subprocess  # Run shell commands
 

class LipSyncProcessor:
    def __init__(self, base_dir: str) -> None:
        # Initialize paths for Wav2Lip and required files.
        self.base_dir = base_dir
        self.wav2lip_dir = os.path.join(self.base_dir, "Wav2Lip-master")   # Wav2Lip directory
        self.silent_video = os.path.join(base_dir, "video.mp4")
        self.audio_path = os.path.join(base_dir, "audio.wav")
        self.output_path = os.path.join(base_dir, "final_output.mp4")  # Path to output video
        self.checkpoint_path = os.path.join(self.wav2lip_dir, "checkpoint", "wav2lip_gan.pth")   # Model checkpoint
        self.face_det_model = os.path.join(self.wav2lip_dir, "face_detection", "detection", "sfd", "s3fd.pth")  # Face detection model
        
    def run_lip_sync(self) -> None:  # Run lip-sync process using Wav2Lip.
        
        try:
            # Change working directory to Wav2Lip-master
            os.chdir(self.wav2lip_dir)
            print(f"Changed working directory to: {os.getcwd()}")  

            # Command to execute inference.py for lip-syncing
            command = [
                       "python", "inference.py",
                        "--checkpoint_path", self.checkpoint_path,
                        "--face", self.silent_video,
                        "--audio", self.audio_path,
                        "--outfile", self.output_path,
                        ]


            subprocess.run(command, check=True) # Run the command
            print("Created:", self.output_path)
        except subprocess.CalledProcessError as e:
            print("Error:", e)



           