"""
 ██████╗ ████████╗  ████████╗██╗██╗     ███████╗
██╔═══██╗╚══██╔══╝  ╚══██╔══╝██║██║     ██╔════╝
██║   ██║   ██║        ██║   ██║██║     █████╗  
██║▄▄ ██║   ██║        ██║   ██║██║     ██╔══╝  
╚██████╔╝   ██║███████╗██║   ██║███████╗███████╗
 ╚══▀▀═╝    ╚═╝╚══════╝╚═╝   ╚═╝╚══════╝╚══════╝
        - By Shibam Roy
"""

# Modules
import group_layouts
import keybindings
import screens_and_bars
from variables import *

###### Hooks ========================================================================

@hook.subscribe.startup_once
def autostart():
    home = path.expanduser("~/.config/qtile/autostart/autostart.sh")
    run(home,capture_output=False,shell=True)


@hook.subscribe.resume
def toggle_mute():
    run("pactl set-sink-mute @DEFAULT_SINK@ toggle",capture_output=False,shell=True)

@hook.subscribe.startup
def _():
    # Checking Modes
    if config["mode_settings"]["mode"]=="focus":
        run("pkill picom",capture_output=False,shell=True)
    else:
        run("picom -b",capture_output=False,shell=True)

    # Temporary fix to a problem
    # screens_and_bars.mybar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)


########## Some variables ==========================================================================
keys = keybindings.keybinds
layouts = group_layouts.layout_var
mouse = keybindings.mouse

# Other options
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = group_layouts.floating
auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Wayland stuff
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"

# Widgets / Bar
widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
groups = group_layouts.groups

screens = screens_and_bars.screens
