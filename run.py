import os
from tdas.menutda import Menu
from tdas.videotda import Video


def Run():

    m = Menu()
    m.Open()
    os.system("clear")
    m.Quality()

    v = Video(m.selectUrl, m.selectName, m.selectQuality)

    v.playVideo()

    os.system("clear")

    if m.playingMenu():
        v.stopVideo()


