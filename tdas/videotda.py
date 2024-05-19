from mpv import *

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

        player = MPV(ytdl=True)
        player = MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)
        player = MPV(
            player_operation_mode="pseudo-gui",
            script_opts="osc-layout=box,osc-seekbarstyle=bar,osc-deadzonesize=0,osc-minmousemove=3",
            input_default_bindings=True,
            input_vo_keyboard=True,
            osc=True,
        )

        player.play(self.videoUrl)
        # player.wait_for_playback()

    def stopVideo(self):
        if not self.process:
            print(ERROR_03)
            return

        return


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
