from libqtile.config import Key
from libqtile.lazy import lazy

from variables import *

keys = [
    Key([mod], "n", lazy.spawn("xournalpp"), desc="Launch Note taking app"),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn("easyfeh -r"),
        desc="Change to random wallpaper",
    ),
    Key(
        [mod, "shift"],
        "left",
        lazy.spawn("easyfeh -p"),
        desc="Change to previous wallpaper",
    ),
    Key(
        [mod, "shift"],
        "right",
        lazy.spawn("easyfeh -n"),
        desc="Change to next wallpaper",
    ),
    Key([mod], "m", lazy.spawn("st ncmpcpp"), desc="Start ncmpcpp"),
    Key([mod, "shift"], "p", lazy.spawn("mpc -p 6200 toggle"), desc="Toggle Mpd music"),
]
