from libqtile import layout
from libqtile.config import Match


def init_layout_theme():
    """it defines the layout style in the list of layouts"""
    return {
        "margin": 3,
        "border_width": 3,
        "border_focus": "#1f023a",
        "border_normal": "#5b0163"
    }


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='Arcolinux-welcome-app.py'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(wm_class='archlinux-logout'),
        Match(wm_class='xfce4-terminal'),
    ],
    fullscreen_border_width=0,
    border_width=0)

layout_theme = init_layout_theme()

layouts = [layout.MonadTall(**layout_theme), layout.Max()]
