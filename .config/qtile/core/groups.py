from libqtile.config import Key, Group
from libqtile.command import lazy
from core.variables import groups, group_names, group_labels, group_layouts, mod
from core.keys import keys


for i, name in enumerate(group_names):
    groups.append(
        Group(
            name=name,
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))


for group in groups:
    keys.extend([

        # CHANGE WORKSPACES
        Key([mod], group.name, lazy.group[group.name].toscreen()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name),
            lazy.group[group.name].toscreen()),
    ])
