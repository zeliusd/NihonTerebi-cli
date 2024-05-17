import subprocess

ERROR_01 = "Did you select a bangumi?"
ERROR_02 = "Did you select a quality video?"


class Video:
    def __init__(self, videoUrl, bangumiName, quality):
        self.videoUrl = videoUrl
        self.bangumiName = bangumiName
        self.quality = quality

    def playVideo(self):

        # command = f'mpv --ytdl-format="bestvideo[height=?{self.quality}][fps<=?30][vcodec!=?vp9]+bestaudio/best {self.videoUrl}'
        command = f'mpv --ytdl-format="bestvideo[height<={self.quality}][fps<=30][vcodec!=vp9]+bestaudio/best" {self.videoUrl}'
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True, check=True
            )
            print("Salida:", result.stdout)
            print("Código de retorno:", result.returncode)
        except subprocess.CalledProcessError as e:
            print("El comando falló con el código de retorno", e.returncode)
            print("Error:", e.stderr)


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


video = create_video("https://mov3.co/tvtokyo/", "TvTokyo", "720")

if video:
    video.playVideo()
