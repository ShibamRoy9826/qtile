#!/bin/sh
sudo kanata -c $HOME/.config/kanata/config.kbd &              ─╯
libinput-gestures-setup start &
bash $HOME/Addons/CustomScripts/nightLight.sh &
mpd &
picom -b &
python $HOME/dev/easyfeh/easyfeh/easyfeh.py -restore &
dunst &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
