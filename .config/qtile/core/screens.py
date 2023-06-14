from libqtile import bar
from libqtile.config import Screen
from core.bar_widgets import widgets_screen1, widgets_screen2


def init_screens():
    """start the top bar"""
    return [
        Screen(top=bar.Bar(
            widgets=widgets_screen1, size=35, opacity=0.8, margin=7, )),
        Screen(top=bar.Bar(widgets=widgets_screen2, size=26, opacity=0.8))
    ]


screens = init_screens()
