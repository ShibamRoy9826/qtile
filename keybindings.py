import os
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key 
from libqtile.lazy import lazy

####### Variables =====================================================================
mod = "mod4"
launcher = "rofi -show drun -theme " + os.path.expanduser(
    "~/.config/rofi/Launcher.rasi"
)
powermenu_cmd = "sh -c ~/.config/rofi/powermenu.sh"
music_toggle = "mpc -p 6200 toggle"
start_music = "kitty ncmpcpp"
browser = "zen-browser"
notes = "xournalpp"
explorer = "thunar"

# Terminal
if qtile.core.name == "x11":
    # term = "kitty"
    term="st"
else:
    term = "foot"

###### Functions ========================================================================
def checkFocus():
    with open(os.path.expanduser("~/.config/qtile/vars.txt"),"r") as f:
        a=f.readlines()[0]
        if a.lower=="true":
            return True
        else:
            return False
def writeFocus(bool_val):
    with open(os.path.expanduser("~/.config/qtile/vars.txt"),"w") as f:
        if bool_val:
            f.write("true")
        else:
            f.write("false")

@lazy.function
def toggleFocusMode(event):
    focus_mode = not checkFocus()
    writeFocus(focus_mode)
    qtile.restart()

focus_mode=checkFocus()

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
    Key([mod], "Return", lazy.spawn(term), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod], "e", lazy.spawn(explorer), desc="Launch File manager"),
    Key([mod], "n", lazy.spawn(notes), desc="Launch Note taking app"),
    Key([mod], "d", lazy.spawn(launcher), desc="Run rofi"),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(powermenu_cmd),
        desc="Run a rofi powermenu script",
    ),
    Key([mod], "m", lazy.spawn(start_music), desc="Start ncmpcpp"),
    Key([mod,"shift"], "p", lazy.spawn(music_toggle), desc="Toggle Mpd music"),

    # Toggle between layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "s",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle between layouts",
    ),

    # Other Essentials
    Key([mod,"shift"], "f", toggleFocusMode(), desc="Enter Focus Mode"),
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
    Key([mod], "r", lazy.spawncmd(), desc="Run a command using a prompt widget"),
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

## Checking for Focus Mode
if focus_mode:
    keybinds=[

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

    # Toggle splitting
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Run Applications/Commands
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod], "n", lazy.spawn(notes), desc="Launch Note taking app"),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(powermenu_cmd),
        desc="Run a rofi powermenu script",
    ),
    Key([mod], "m", lazy.spawn(start_music), desc="Start ncmpcpp"),
    Key([mod,"shift"], "p", lazy.spawn(music_toggle), desc="Toggle Mpd music"),

    # Toggle between layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Other Essentials
    Key([mod,"shift"], "f", toggleFocusMode(), desc="Enter Focus Mode"),
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

]
## Mouse bindings
mouse = [
    Drag(
        [mod, "control"],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
