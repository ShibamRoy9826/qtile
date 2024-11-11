import subprocess

import toml
from libqtile import bar, qtile
from libqtile import widget as wdg
from libqtile.config import Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from keybindings import launcher
from variables import *

###### Variables ===================================================================

time_format = "%-I:%M %p"
date_format = "%A , %-d %B %Y"
showing_time = True

#### Load TOML config ======================================================================

with open(config_file, "r") as f:
    config = toml.load(f)

###### Functions ====================================================================


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/powermenu.sh")


def toggle_time_date(widget):
    global showing_time
    if showing_time:
        widget.format = date_format
    else:
        widget.format = time_format
    showing_time = not showing_time
    widget.tick()


def toggle_mute():
    subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "toggle"])


def update_memory():
    try:
        # Run the 'free -m' command to get memory usage in megabytes
        process = subprocess.Popen(["free", "-m"], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        output_lines = output.decode().splitlines()
        used = output_lines[1].split()[2]
        return f"{used}"
    except Exception as e:
        return f"Error: {str(e)}"


#### Colors ==========================================================================
bg = "#11111b90"
bg2 = "#18182590"
fg = "#cdd6f4"
fg2 = "#bac2de"
urgent = "#f38ba8"
primary = "#89b4fa"

#### Bar ==============================================================================
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

mybar = bar.Bar(
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
        # widget.Sep(foreground=fg, size_percent=60, padding=16),
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
        # widget.Memory(
        #     format="󰍛 {MemUsed:.0f}Mib",
        #     fontsize=15,
        #     foreground=fg,
        #     update_interval=5,
        #     margin_x=8,
        #     padding=8,
        #     mouse_callbacks={"Button1": lazy.spawn("kitty btop")},
        #     decorations=decor
        # ),
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
        # widget.Sep(foreground=fg, size_percent=60, padding=16),
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


focus_bar = bar.Bar(
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
        # widget.Sep(foreground=fg, size_percent=60, padding=16),
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
        # widget.Memory(
        #     format="󰍛 {MemUsed:.0f}Mib",
        #     fontsize=15,
        #     foreground=fg,
        #     update_interval=5,
        #     margin_x=8,
        #     padding=8,
        #     mouse_callbacks={"Button1": lazy.spawn("kitty btop")},
        #     decorations=decor
        # ),
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
        # widget.Sep(foreground=fg, size_percent=60, padding=16),
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

## Using the focus bar if focus mode is turned on
focus = int(config["mode_settings"]["mode"])

if focus:
    screens = [Screen(top=focus_bar)]
else:
    screens = [Screen(top=mybar)]
