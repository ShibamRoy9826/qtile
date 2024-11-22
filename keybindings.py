from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy
from modes import *
from custom import custom_keybindings

# Terminal
if qtile.core.name == "x11":
    term = config["general"]["terminal_x11"]
else:
    term = config["general"]["terminal_wayland"]


####### Keybindings =====================================================================

keybinds=md[config["mode_settings"]["mode"]][0]

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
keybinds.extend(custom_keybindings.keys)

## Mouse bindings ==================================================================================
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
