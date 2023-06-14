# import os
# import socket
from libqtile import widget
from libqtile.lazy import lazy
from core.variables import colors



# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(font="Noto Sans", fontsize=12, padding=4, background=colors['background'], border_width=4)


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.TextBox(
            background=colors['black'],
            foreground=colors['light_purple'],
            font="FontAwesome",
            fontsize=27,
            padding=10,
            text="",
            mouse_callbacks={
                'button1': lambda: lazy.cmd_spawn("kitty")
            }
        ),
        widget.Spacer(
            background=colors['black'],
            length=1
        ),
        widget.GroupBox(font="FontAwesome",
                        fontsize=16,
                        margin_y=4,
                        margin_x=0,
                        padding_y=6,
                        padding_x=5,
                        borderwidth=0,
                        disable_drag=True,
                        active=colors['violet'],
                        inactive=colors['white'],
                        rounded=False,
                        highlight_method="text",
                        this_current_screen_border=colors['light_purple'],
                        foreground=colors['white'],
                        background=colors['black']),
        widget.TextBox(
            background=colors['background'],
            foreground=colors['black'],
            fontsize=27,
            font='FontAwesome',
            padding=0,
            text=''
        ),
        widget.WindowName(
            font="Noto Sans",
            fontsize=12,
            format="{name}",
            foreground=colors['white'],
            background=colors['background'],
        ),
        # widget.Net(
        #          font="Noto Sans",
        #          fontsize=12,
        #          interface="enp0s31f6",
        #          foreground=colors[2],
        #          background=colors[1],
        #          padding = 0,
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.NetGraph(
        #          font="Noto Sans",
        #          fontsize=12,
        #          bandwidth="down",
        #          interface="auto",
        #          fill_color = colors[8],
        #          foreground=colors[2],
        #          background=colors[1],
        #          graph_color = colors[8],
        #          border_color = colors[2],
        #          padding = 0,
        #          border_width = 1,
        #          line_width = 1,
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # # do not activate in Virtualbox - will break qtile
        # widget.ThermalSensor(
        #          foreground = colors[5],
        #          foreground_alert = colors[6],
        #          background = colors[1],
        #          metric = True,
        #          padding = 3,
        #          threshold = 80
        #          ),
        # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # arcobattery.BatteryIcon(
        #          padding=0,
        #          scale=0.7,
        #          y_poss=2,
        #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
        #          update_interval = 5,
        #          background = colors[1]
        #          ),
        # # battery option 2  from Qtile
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.Battery(
        #          font="Noto Sans",
        #          update_interval = 10,
        #          fontsize = 12,
        #          foreground = colors[5],
        #          background = colors[1],
        #          ),
        # widget.TextBox(
        #          font="FontAwesome",
        #          text="  ",
        #          foreground=colors[6],
        #          background=colors[1],
        #          padding = 0,
        #          fontsize=16
        #          ),
        # widget.CPUGraph(
        #          border_color = colors[2],
        #          fill_color = colors[8],
        #          graph_color = colors[8],
        #          background=colors[1],
        #          border_width = 1,
        #          line_width = 1,
        #          core = "all",
        #          type = "box"
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.TextBox(
        #          font="FontAwesome",
        #          text="  ",
        #          foreground=colors[4],
        #          background=colors[1],
        #          padding = 0,
        #          fontsize=16
        #          ),
        # widget.Memory(
        #          font="Noto Sans",
        #          format = '{MemUsed}M/{MemTotal}M',
        #          update_interval = 1,
        #          fontsize = 12,
        #          foreground = colors[5],
        #          background = colors[1],
        #         ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        widget.TextBox(
            font="FontAwesome",
            fontsize=29,
            padding=0,
            foreground=colors['blue'],
            background=colors['background'],
            text=""
        ),
        widget.TextBox(
            font="FontAwesome",
            fontsize=27,
            foreground=colors['white'],
            background=colors['blue'],
            text=""
        ),
        widget.TextBox(
            font="FontAwesome",
            fontsize=29,
            padding=0,
            foreground=colors['white'],
            background=colors['blue'],
            text=""
        ),
        widget.CPU(
            font="FontAwesome",
            fontsize=12,
            padding=0,
            background=colors['white'],
            foreground=colors['black'],
            format="{load_percent}%"
        ),
        widget.Sep(
            linewidth=0,
            padding=3,
            background=colors['background'],
            foreground=colors['background']
        ),
        widget.TextBox(
            font="FontAwesome",
            fontsize=27,
            foreground=colors['white'],
            background=colors['red'],
            text=""
        ),
        widget.Memory(
            font="FontAwesome",
            fontsize="12",
            foreground=colors['black'],
            background=colors['white'],
        ),
        widget.TextBox(
            font="FontAwesome",
            fontsize=27,
            text="",
            background=colors['white'],
            foreground=colors['black'],
            padding=0
        ),
        widget.TextBox(font="FontAwesome",
                       text="  ",
                       foreground=colors['light_purple'],
                       background=colors['black'],
                       padding=0,
                       fontsize=18),
        widget.Clock(foreground=colors['white'],
                     background=colors['black'],
                     fontsize=12,
                     format="[%H:%M] %d/%m/%Y"),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        widget.Systray(
            background=colors['black'],
            icon_size=20,
            padding=4),
        widget.Sep(
            linewidth=2,
            padding=5,
            foreground=colors['black'],
            background=colors['black']
        ),
        widget.QuickExit(
            background=colors['red'],
            foreground=colors['white'],
            default_text="⏻",
            fontsize=18,
            countdown_format="",
        )
    ]
    return widgets_list


def init_widgets_screen1():
    return init_widgets_list()


def init_widgets_screen2():
    return init_widgets_list()


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
