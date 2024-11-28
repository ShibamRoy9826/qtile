## Qtile related stuff
# More
from variables import *
from modes import *
from libqtile.config import Screen 

#### Bar ==============================================================================

b= md[config["mode_settings"]["mode"]][1]

if config["bar"]["bar_position"]=="top":
    screens = [Screen(top=b)]
else:
    screens = [Screen(bottom=b)]
