## Qtile related stuff
from libqtile import bar, qtile
from libqtile import widget as wdg
from libqtile.config import Key
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from functions import *
from variables import *

# Terminal
if qtile.core.name == "x11":
    term = config["general"]["terminal_x11"]
else:
    term = config["general"]["terminal_wayland"]

#######| Switch modes |#######################################################

@lazy.function
def switchMode(event):
    curr_mode=config["mode_settings"]["mode"]
    ind=mode_list.index(curr_mode)
    if ind==(len(mode_list)-1):
        ind=0
        config["mode_settings"]["mode"]=mode_list[ind]
    else:
        config["mode_settings"]["mode"]=mode_list[ind+1]

    with open(config_file,"w") as f:
        dump(config,f)
    qtile.restart()

#####################| Modes |######################################################################### 

md={"normal":[[],[]],"focus":[[],[]]} # first list for keybindings, second for bars
mode_list=["normal","focus"]
showing_time = True

## Functions
def toggle_time_date(widget):
    global showing_time
    if showing_time:
        widget.format = date_format
    else:
        widget.format = time_format
    showing_time = not showing_time
    widget.tick()

#####################| Keybindings |########################################################################

md["normal"][0]=[
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
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch File manager"),
    Key([mod], "d", lazy.spawn(launcher), desc="Run application launcher"),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn(powermenu_cmd),
        desc="Run powermenu",
    ),

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

    # Screenshot
    Key([],"Print", takeScreenshot(), desc="Take a screenshot"),
    Key([mod],"Print", takeScreenshot(select=True), desc="Take a screenshot"),
    
    #Volume Control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),

    # Brightness Control

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

    ## Mode Shift
    Key([mod, "shift"], "m", switchMode(), desc="Switch Modes"),
]

md["focus"][0]=md["normal"][0]


##############################################| Bars |############################################################################

decor = [
    RectDecoration(colour="#11111b", radius=10, filled=True, padding_y=6, group=True)
]

clock_widget = widget.Clock(
    format=time_format,  # Start by showing the time
    foreground=fg,
    fontsize=15,
    padding=20,
    mouse_callbacks={
        "Button1": lambda: toggle_time_date(clock_widget),  # Left-click to toggle
    },
)

md["normal"][1]= bar.Bar(
    [
        widget.Spacer(length=15),
        widget.TextBox(
            text="󰣇 ",
            fontsize=15,
            padding=15,
            foreground=primary,
            mouse_callbacks={
                "Button1": lazy.spawn(launcher),
            },
        ),
        widget.GroupBox(
            active=fg,
            background=bg2,
            highlight_method="text",
            block_highlight_text_color=fg,
            highlight_color=fg,
            foreground=fg,
            urgent_text=urgent,
            fmt="󰝥",
            disable_drag=True,
            rounded=True,
            border_width=4,
            padding=6,
            border_color=bg,
            this_current_screen_border=primary,
            this_screen_border=fg2,
            decorations=decor,
        ),
        widget.Spacer(length=15),
        widget.CurrentLayoutIcon(foreground=fg, scale=0.7, padding=8),
        widget.Spacer(length=bar.STRETCH),
        ## Music
        widget.Mpd2(
            color_process=primary,
            port=6200,
            status_format="{play_status} {artist} - {title}",
            play_states={"pause": "󰐊", "play": "󰏤", "stop": "󰓛"},
            idle_message="No Music playing rn...",
            idle_format="󰝚   {idle_message}",
            fontsize=15,
            mouse_callbacks={
                "Button2": lazy.spawn("mpc -p 6200 next"),  # Left-click to toggle
            },
            padding=20,
            decorations=decor,
        ),
        #### Some Other stuff
        # widget.Sep(foreground=fg, size_percent=60, padding=16),
        widget.Backlight(
            backlight_name="intel_backlight",
            fontsize=15,
            change_command="brightnessctl set {0}%",
            step=5,
            padding=20,
            format="󰃞 {percent:2.0%}",
        ),
        wdg.PulseVolume(
            fontsize=15,
            scroll_interval=0.01,
            padding=20,
            step=1,
            scroll_step=1,
            mute_format="󰖁 ",
            unmute_format="󰕾 {volume}%",
            volume_app="pavucontrol",
            mouse_callbacks={
                "Button1": lambda: toggle_mute(),
                "Button3": lazy.spawn("kitty ncmpcpp"),
            },
        ),
        #### RESOURCE MONITOR
        widget.ThermalSensor(
            threshold=80,
            fontsize=15,
            update_interval=5,
            foreground=fg,
            format="󰔏 {temp:.1f}{unit}",
            padding=20,
            decorations=decor,
            mouse_callbacks={"Button1": lazy.spawn("st btop")},
        ),
        widget.GenPollText(
            func=update_memory,  # Function to call
            fmt="󰍛 {}Mib",
            fontsize=15,
            foreground=fg,
            update_interval=5,
            margin_x=8,
            padding=8,
            mouse_callbacks={"Button1": lazy.spawn("st btop")},
            decorations=decor,
        ),
        widget.CPU(
            format="󰘚 {load_percent}%",
            fontsize=15,
            foreground=fg,
            update_interval=5,
            margin_x=8,
            padding=20,
            mouse_callbacks={"Button1": lazy.spawn("st btop")},
            decorations=decor,
        ),

        ##### CLOCK WIDGET
        clock_widget,
        widget.Spacer(length=15),
    ],
    45,
    background="#11111b90",
    border_color=bg,
    border_width=[0, 0, 0, 0],
    margin=[6, 35, 2, 35],
)



md["focus"][1] = bar.Bar(
    [
        widget.Spacer(length=15),
        widget.TextBox(
            text="󰣇 ",
            fontsize=15,
            padding=15,
            foreground=primary,
            mouse_callbacks={
                "Button1": lazy.spawn(launcher),
            },
        ),
        widget.GroupBox(
            active=fg,
            background=bg2,
            highlight_method="text",
            block_highlight_text_color=fg,
            highlight_color=fg,
            foreground=fg,
            urgent_text=urgent,
            fmt="󰝥",
            disable_drag=True,
            rounded=True,
            border_width=4,
            padding=6,
            border_color=bg,
            this_current_screen_border=primary,
            this_screen_border=fg2,
            decorations=decor,
        ),
        widget.Spacer(length=bar.STRETCH),
        ## Music
        widget.Mpd2(
            color_process=primary,
            port=6200,
            status_format="{play_status} {artist} - {title}",
            play_states={"pause": "󰐊", "play": "󰏤", "stop": "󰓛"},
            idle_message="No Music playing rn...",
            idle_format="󰝚   {idle_message}",
            fontsize=15,
            mouse_callbacks={
                "Button2": lazy.spawn("mpc -p 6200 next"),  # Left-click to toggle
            },
            padding=20,
            decorations=decor,
        ),
        #### Some Other stuff
        widget.Backlight(
            backlight_name="intel_backlight",
            fontsize=15,
            change_command="brightnessctl set {0}%",
            step=5,
            padding=20,
            format="󰃞 {percent:2.0%}",
        ),
        wdg.PulseVolume(
            fontsize=15,
            scroll_interval=0.01,
            padding=20,
            step=1,
            scroll_step=1,
            mute_format="󰖁 ",
            unmute_format="󰕾 {volume}%",
            volume_app="pavucontrol",
            mouse_callbacks={
                "Button1": lambda: toggle_mute(),
                "Button3": lazy.spawn("kitty ncmpcpp"),
            },
        ),
        #### RESOURCE MONITOR
        widget.ThermalSensor(
            threshold=80,
            fontsize=15,
            update_interval=5,
            foreground=fg,
            format="󰔏 {temp:.1f}{unit}",
            padding=20,
            decorations=decor,
            mouse_callbacks={"Button1": lazy.spawn("kitty btop")},
        ),
        widget.GenPollText(
            func=update_memory,  # Function to call
            fmt="󰍛 {}Mib",
            fontsize=15,
            foreground=fg,
            update_interval=5,
            margin_x=8,
            padding=8,
            mouse_callbacks={"Button1": lazy.spawn("kitty btop")},
            decorations=decor,
        ),
        widget.CPU(
            format="󰘚 {load_percent}%",
            fontsize=15,
            foreground=fg,
            update_interval=5,
            margin_x=8,
            padding=20,
            mouse_callbacks={"Button1": lazy.spawn("kitty btop")},
            decorations=decor,
        ),
        ##### CLOCK WIDGET
        clock_widget,
        widget.Spacer(length=15),
    ],
    45,
    background="#11111b90",
    border_color=bg,
    border_width=[0, 0, 0, 0],
    margin=[0, 0, 0, 0],
)
