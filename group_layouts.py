from libqtile import layout
from libqtile.config import Group, Match, ScratchPad

from custom import custom_layouts
from variables import *

curr_mode = config["mode_settings"]["mode"]
ind = mode_list.index(curr_mode)
mode_num = mode_list[ind]

# Defaults
normal_color = "#595959aa"
focus_color = "#cba6f7"
border_w = 2
floating_border_w = 1
border_ws = 2
gaps = 5

for index, i in enumerate(config["modes"]):
    if index == ind:
        normal_color = i["normal_color"]
        focus_color = i["focus_color"]
        border_w = i["border_width"]
        floating_border_w = i["floating_border_width"]
        border_ws = i["border_width_single"]
        gaps = i["gaps"]


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
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_focus=focus_color,
    border_normal=normal_color,
    border_width=floating_border_w,
)

groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
]

if config["general"]["scratchpad_enabled"]:
    groups.append(ScratchPad("scratchpad", custom_layouts.scratchpads))
