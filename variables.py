from os import getlogin,path
####### Variables =====================================================================
mod = "mod4"
launcher = "rofi -show drun -theme " + path.expanduser(
    "~/.config/rofi/Launcher.rasi"
)
powermenu_cmd = "sh -c ~/.config/rofi/powermenu.sh"
music_toggle = "mpc -p 6200 toggle"
start_music = "kitty ncmpcpp"
browser = "zen-browser"
notes = "xournalpp"
explorer = "thunar"
config_file = f"/home/{getlogin()}/.config/qtile/config.toml"

defaultConf=f"""
[general]
screenshot_directory="/home/{getlogin()}/Pictures/Screenshots"
[mode_settings]
# 0 -> Normal , 1 -> Focus
mode=0
"""

