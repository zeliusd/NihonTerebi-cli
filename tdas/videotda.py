import subprocess

ERROR_01 = "Did you select a bangumi?"
ERROR_02 = "Did you select a quality video?"
ERROR_03 = "Don't have a playing video now"


class Video:
    def __init__(self, videoUrl, bangumiName, quality):
        self.videoUrl = videoUrl
        self.bangumiName = bangumiName
        self.quality = quality
        self.process = None

    def playVideo(self):

        command = f'mpv --ytdl-format="bestvideo[height<={self.quality}][fps<=30][vcodec!=vp9]+bestaudio/best" {self.videoUrl}'
        try:
            self.process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("El video se está reproduciendo en segundo plano.")
        except Exception as e:
            print(f"El comando falló con la excepción: {e}")

    def stopVideo(self):
        if not self.process:
            print(ERROR_03)
            return

        self.process.terminate()
        try:
            self.process.wait(timeout=5)
            print("El video ha sido detenido.")
        except subprocess.TimeoutExpired:
            self.process.kill()
            print("El video ha sido forzado a detenerse.")


def create_video(videoUrl, bangumiName, quality):
    if not videoUrl or not bangumiName:
        print(ERROR_01)
        return None
    if not quality:
        print(ERROR_02)

    v = Video(videoUrl, bangumiName, quality)

    print(v.videoUrl)
    print(v.bangumiName)
    print(v.quality)

    return v
