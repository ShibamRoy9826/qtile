from libqtile.config import Key
from libqtile.lazy import lazy
from functions import shiftBar,randomWall,prevWall,nextWall
from variables import *

keys = [
    Key(
        [mod, "shift"],
        "b",
        shiftBar(),
        desc="Shifts bar from top to bottom or vice-versa",
    ),
    Key([mod], "n", lazy.spawn("xournalpp"), desc="Launch Note taking app"),
    Key(
        [mod, "shift"],
        "w",
        randomWall(),
        desc="Change to random wallpaper",
    ),
    Key(
        [mod, "shift"],
        "left",
        prevWall(),
        desc="Change to previous wallpaper",
    ),
    Key(
        [mod, "shift"],
        "right",
        nextWall(),
        desc="Change to next wallpaper",
    ),
    Key([mod], "m", lazy.spawn("st ncmpcpp"), desc="Start ncmpcpp"),
    Key([mod, "shift"], "p", lazy.spawn("mpc -p 6200 toggle"), desc="Toggle Mpd music"),
]



