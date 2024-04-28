"""
This class is created to configure the level generation.
pos - the position of the barrier (tubes)
width - the width of the barrier (tubes)
height - the length of the barrier (tubes)
updown - specifies where the barrier will be located, 1 - top, 0 - bottom
finish_ticks - the number of points needed to complete the level
"""


class maps:
    pos = [200, 500, 800, 1100, 1500, 2000, 2500, 3000, 3500, 4000, 4500]
    width = [700, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800]
    height = [250, 300, 250, 300, 250, 300, 250, 300, 250, 300, 250]
    updown = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    finish_ticks = 16000