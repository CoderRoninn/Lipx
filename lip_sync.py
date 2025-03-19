import os
import subprocess

class LipSyncProcessor:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        self.wav2lip_dir = os.path.join(self.base_dir, "Wav2Lip-master")  # ✅ Wav2Lip ana dizini
        self.silent_video = os.path.join(base_dir, "video.mp4")
        self.audio_path = os.path.join(base_dir, "audio.wav")
        self.output_path = os.path.join(base_dir, "final_output.mp4")
        self.checkpoint_path = os.path.join(self.wav2lip_dir, "checkpoint", "wav2lip_gan.pth")
        self.face_det_model = os.path.join(self.wav2lip_dir, "face_detection", "detection", "sfd", "s3fd.pth")
        
    def run_lip_sync(self) -> None:
        """
        Bu fonksiyon, sessiz video ile ses dosyasını kullanarak Wav2Lip modelini çalıştırır
        ve dudak senkronizasyonlu final videoyu üretir.
        """
        try:
            # ✅ Önce Wav2Lip-master klasörüne geç
            os.chdir(self.wav2lip_dir)
            print(f"Changed working directory to: {os.getcwd()}")  # ✅ Çalışma dizinini ekrana yazdır

            # ✅ inference.py'yi çalıştırırken tam yolları kullan
            command = [
                "python",
                "inference.py",
                "--checkpoint_path", self.checkpoint_path,
                "--face", self.silent_video,
                "--audio", self.audio_path,
                "--outfile", self.output_path,
                ]

            subprocess.run(command, check=True)
            print("✅ Dudak senkronizasyon işlemi tamamlandı. Çıktı:", self.output_path)
        except subprocess.CalledProcessError as e:
            print("❌ Lip sync işlemi sırasında hata oluştu:", e)



           