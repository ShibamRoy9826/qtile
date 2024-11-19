from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy
import toml
from variables import *
from os import mkdir, system
from time import strftime

# Terminal
if qtile.core.name == "x11":
    term = "st"
else:
    term = "foot"

###### Modes ===========================================================================

with open(config_file, "r") as f:
    config = toml.load(f)

@lazy.function
def switchMode(event):
    config["mode_settings"]["mode"]= int(not int(config["mode_settings"]["mode"]))
    with open(config_file,"w") as f:
        toml.dump(config,f)
    qtile.cmd_restart()

@lazy.function
def takeScreenshot(event,select=False):
    scrDir=config["general"]["screenshot_directory"]
    filename=strftime("Screenshot-%d-%b-%y__%H-%M-%S.png")
    filepath=path.join(scrDir,filename)
    if not path.exists(scrDir):
        mkdir(config["general"]["screenshot_directory"])
    
    if select:
        system(command=f"scrot -z -s -F '{filepath}'")
        system(command="scrot -z -F '-' | xclip -sel clipboard -t image/png")
        system(command=f"notify-send 'Screenshot captured:)' 'Screenshot has been copied and is saved as {filepath}'")
    else:
        system(command=f"scrot -z -F '{filepath}'")
        system(command="scrot -z -F '-' | xclip -sel clipboard -t image/png")
        system(command=f"notify-send 'Screenshot captured:)' 'Screenshot has been copied and is saved as {filepath}'")

    
    

####### Keybindings =====================================================================
keybinds = [
    # Moving in between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving windows
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resizing windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Group
    Key([mod], "Right", lazy.screen.next_group(), desc="Move to next workspace"),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Move to previous workspace"),
    # Resetting window sizes
    Key([mod, "shift"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle splitting
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Run Applications/Commands
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn("python /home/shibam/dev/easyfeh/easyfeh/easyfeh.py -random"),
        desc="Change to random wallpaper",
    ),
    Key(
        [mod, "shift"],
        "left",
        lazy.spawn("python /home/shibam/dev/easyfeh/easyfeh/easyfeh.py -prev"),
        desc="Change to previous wallpaper",
    ),
    Key(
        [mod, "shift"],
        "right",
        lazy.spawn("python /home/shibam/dev/easyfeh/easyfeh/easyfeh.py -next"),
        desc="Change to next wallpaper",
    ),
    Key([mod], "Return", lazy.spawn(term), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod], "e", lazy.spawn(explorer), desc="Launch File manager"),
    Key([mod], "n", lazy.spawn(notes), desc="Launch Note taking app"),
    Key([mod], "c", lazy.spawn("surf chatgpt.com"), desc="Launch ChatGpt"),
    Key([mod], "y", lazy.spawn("surf youtube.com"), desc="Launch Youtube"),
    Key([mod], "g", lazy.spawn("surf google.com"), desc="Launch Google"),
    Key([mod], "d", lazy.spawn(launcher), desc="Run rofi"),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(powermenu_cmd),
        desc="Run a rofi powermenu script",
    ),
    Key([mod], "m", lazy.spawn(start_music), desc="Start ncmpcpp"),
    Key([mod, "shift"], "p", lazy.spawn(music_toggle), desc="Toggle Mpd music"),
    # Toggle between layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "s",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Starting dropdown terminal",
    ),
    Key(
        [mod],
        "r",
        lazy.group["scratchpad"].dropdown_toggle("recorder"),
        desc="Start recorder",
    ),
    # Other Essentials
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "v",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Run a command using a prompt widget"),
    Key([],"Print", takeScreenshot(), desc="Take a screenshot"),
    Key([mod],"Print", takeScreenshot(select=True), desc="Take a screenshot"),
    
    #Volume Control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),

    ## Mode Shift
    Key([mod, "shift"], "m", switchMode(), desc="Switch Modes"),
]


## adding keybindings to change workspaces (wayland)
for vt in range(1, 8):
    keybinds.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


## Adding keybindings to change and work with workspaces/groups (x11/wayland)
groups = [Group(i) for i in "123456789"]

for i in groups:
    keybinds.extend(
        [
            # Switching between workspaces
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # Move windows to workspaces (also switches to that workspace/group)
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )


## Mouse bindings
mouse = [
    Drag(
        [mod ],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
