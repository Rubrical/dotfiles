import os
import subprocess
from libqtile import hook
from libqtile.config import Drag, Match
from libqtile.command import lazy
from core import (  # noqa: F401
    widget_defaults, widgets_screen1, widgets_screen2, screens, keys, layouts,
    floating_layout, mod, groups)

# MOUSE CONFIGURATION
mouse = [
    Drag([mod],
         "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []
match_discord = Match(wm_class="discord")

main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


@hook.subscribe.client_new
def move_discord_to_group(window):
    """move discord to the last group"""
    if match_discord.compare(window):
        window.togroup("7")


floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
