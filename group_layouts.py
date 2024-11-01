from libqtile import layout
from libqtile.config import DropDown, Group, Match, ScratchPad

layout_var = [
    layout.Columns(
        border_focus="#89b4fa",
        border_normal="#595959aa",
        border_width=3,
        border_on_single=2,
        margin=10,
    ),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_focus="#89b4fa",
        border_normal="#595959aa",
        border_width=3,
        border_on_single=2,
        margin=10,
    ),
    layout.Matrix(
        border_focus="#89b4fa",
        border_normal="#595959aa",
        border_width=3,
        border_on_single=2,
        margin=10,
    ),
    layout.MonadTall(
        border_focus="#89b4fa",
        border_normal="#595959aa",
        border_width=3,
        border_on_single=2,
        margin=10,
    ),
    layout.MonadWide(
        border_focus="#89b4fa",
        border_normal="#595959aa",
        border_width=3,
        border_on_single=2,
        margin=10,
    ),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.Zoomy(
        border_focus="#89b4fa",
        border_normal="#595959aa",
        border_width=3,
        border_on_single=2,
        margin=10,
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
    border_focus="#89b4fa",
    border_normal="#595959aa",
    border_width=3,
)

groups = [
    ScratchPad("scratchpad", [DropDown("term", "kitty", opacity=1.0, height=0.5)]),
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
]
