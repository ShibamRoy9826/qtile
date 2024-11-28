from libqtile.config import DropDown
from variables import term

scratchpads = [
    DropDown("term", term, opacity=1.0, height=0.5),
    DropDown("recorder", "simplescreenrecorder", opacity=1.0, height=0.5),
]
