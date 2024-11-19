from libqtile import layout
from libqtile.config import DropDown, Group, Match, ScratchPad
import toml
from variables import *

# normal_color="#1e1e2e"
# focus_color="#595959aa"

with open(config_file, "r") as f:
    config = toml.load(f)

if config["mode_settings"]["mode"]:
    normal_color="#595959aa"
    focus_color="#cba6f7"
    border_w=2
    floating_border_w=1
    border_ws=2
    gaps=5
else:
    normal_color="#595959aa"
    focus_color="#cba6f7"
    border_w=2
    floating_border_w=2
    border_ws=2
    gaps=10

layout_var = [
    layout.Columns(
        border_focus=focus_color,
        border_normal=normal_color,
        border_width=border_w,
        border_on_single=border_ws,
        margin=gaps,
    ),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_focus=focus_color,
        border_normal=normal_color,
        border_width=border_w,
        border_on_single=border_ws,
        margin=gaps,
    ),
    layout.Matrix(
        border_focus=focus_color,
        border_normal=normal_color,
        border_width=border_w,
        border_on_single=border_ws,
        margin=gaps,
    ),
    layout.MonadTall(
        border_focus=focus_color,
        border_normal=normal_color,
        border_width=border_w,
        border_on_single=border_ws,
        margin=gaps,
    ),
    layout.MonadWide(
        border_focus=focus_color,
        border_normal=normal_color,
        border_width=border_w,
        border_on_single=border_ws,
        margin=gaps,
    ),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.Zoomy(
        border_focus=focus_color,
        border_normal=normal_color,
        border_width=border_w,
        border_on_single=border_ws,
        margin=gaps,
        property_small="0.1",
    ),
]

floating = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=focus_color,
    border_normal=normal_color,
    border_width=floating_border_w,
)

groups = [
    ScratchPad("scratchpad", [
        DropDown("term", "st", opacity=1.0, height=0.5),
        DropDown("recorder", "simplescreenrecorder", opacity=1.0, height=0.5),
        ]),
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
]
