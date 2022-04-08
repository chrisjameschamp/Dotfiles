#   ___  _   _ _
#  / _ \| |_(_) | ___
# | | | | __| | |/ _ \
# | |_| | |_| | |  __/
#  \__\_\\__|_|_|\___|
#
# https://github.com/chrisjameschamp

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

#---------------#
#     THEME     #
#---------------#

#---    Neon      ---#
theme = {
    "colors": {
        "background":   "#171717",
        "foreground":   "#f8f8f8",
        "normal": {
            "black":    "#171717",
            "red":      "#d81765",
            "green":    "#97d01a",
            "yellow":   "#ffa800",
            "blue":     "#16b1fb",
            "magenta":  "#ff2491",
            "cyan":     "#0fdcb6",
            "white":    "#ebebeb"
        },
        "bright": {
            "black":    "#38252c",
            "red":      "#ff0000",
            "green":    "#76b639",
            "yellow":   "#e1a126",
            "blue":     "#289cd5",
            "magenta":  "#ff2491",
            "cyan":     "#0a9b81",
            "white":    "#f8f8f8"
        },
        "dark": {
            "black":    "#0d0a06"
        },
        "grad": [
            "#171717",
            "#1b1b1b",
            "#252525",
            "#2b2a2b",
            "#343233",
            "#3f3c3d",
            "#494647",
            "#504d4e",
            "#565253"
        ],
    }
}

#---------------#
#   SUPER KEY   #
#---------------#
mod = "mod4"

#---------------#
#   KEYBINDINGS #
#---------------#
 
keys = [

    #---    Switch between windows  ---#
    Key([mod], "j", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "i", lazy.layout.up()),
    Key([mod], "p", lazy.layout.next()),

    #---    Move windows    ---#
    Key([mod, "shift"], "j", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up()),

    #---    Resize windows  ---#
    Key([mod, "control"], "j", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "k", lazy.layout.grow_down()),
    Key([mod, "control"], "i", lazy.layout.grow_up()),

    #---    Get windows original size   ---#
    Key([mod, "shift"], "n", lazy.layout.normalize()),

    #---    Toggle floating ---#
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    #---    Browser     ---#
    Key([mod], "b", lazy.spawn("google-chrome-stable")),

    #---    Terminal    ---#
    Key([mod], "Return", lazy.spawn('alacritty')),

    #---    Launcher    ---#
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    #---    Explorer    ---#
    Key([mod], "e", lazy.spawn('alacritty -e ranger')),

    #---    Screenshot  ---#

    #---    Toogle layout   ---#
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    #---    Kill window     ---#
    Key([mod], "w", lazy.window.kill()),

    #---    Reload Qtile    ---#
    Key([mod, "shift"], "r", lazy.reload_config()),

    #---    Exit Qtile      ---#
    Key([mod, "shift"], "q", lazy.shutdown()),

    # Not Currently Working 
    #---    Brightness up   ---#
    #Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),

    #---    Brightness down ---#
    #Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
]

#---------------#
#   GROUPS      #
#---------------#

#groups = [Group(i) for i in "123456789"]
#groups = [Group(i) for i in [
#    " >_ ", " www ", " A ", " B ", " C ", " D ",
#]]
groups = [Group(i) for i in [
    "  ", "  ", " 阮 ", " ﭮ ", " 異 ", "  ", 
]]

#---------------#
#   WORKSPACES  #
#---------------#

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.Bsp(
        border_focus=theme['colors']['normal']['red'],
        border_normal=theme['colors']['background'],
        border_width=1,
        margin=12,
        margin_on_single=0
    ),
    layout.MonadTall(
        order_focus=theme['colors']['normal']['red'],
        border_normal=theme['colors']['background'],
        border_width=1,
        margin=12,
        single_margin=0,
        single_border_width=0
    ),
    layout.MonadWide(
        order_focus=theme['colors']['normal']['red'],
        border_normal=theme['colors']['background'],
        border_width=1,
        margin=12,
        single_margin=0,
        single_border_width=0
    ),
    #layout.Columns(),
    #layout.Max(),
    #layout.Stack(),
    #layout.Matrix(),
    #layout.RatioTile(),
    #layout.Floating(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

#---------------#
#   FONT        #
#---------------#

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=6
)
extension_defaults = widget_defaults.copy()

#---------------#
#   TOPBAR      #
#---------------#

def powerline_left(bg, fg):
    return widget.TextBox(
        background=bg,
        foreground=fg,
        text="",
        fontsize=37,
        padding=-3,
        width=15
    )

def powerline_right(bg, fg):
    return widget.TextBox(
        background=bg,
        foreground=fg,
        text="",
        fontsize=37,
        padding=-3,
        width=13
    )

def icon(fontsize, text, bg, fg):
    return widget.TextBox(
        background=bg,
        foreground=fg,
        fontsize=fontsize,
        text=text,
        padding=4
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    background=theme['colors']['normal']['yellow'],
                    filename="~/.config/qtile/logo_dark.png",
                    scale="True",
                    margin=2
                ),
                powerline_left(theme['colors']['normal']['black'], theme['colors']['normal']['yellow']),
                widget.CurrentLayout(
                    background=theme['colors']['normal']['black'],
                    foreground=theme['colors']['normal']['red']
                ),
                powerline_left(theme['colors']['grad'][2], theme['colors']['normal']['black']),
                widget.GroupBox(
                    background=theme['colors']['grad'][2],
                    highlight_method="line",
                    highlight_color=theme['colors']['grad'][2],
                    borderwidth=0,
                    active=theme['colors']['foreground'],
                    block_highlight_text_color=theme['colors']['normal']['green'],
                    hide_unused=True
                ),
                powerline_left(theme['colors']['dark']['black'], theme['colors']['grad'][2]),
                #widget.Prompt(),
                widget.WindowName(
                    foreground=theme['colors']['foreground'],
                ),
                #widget.Chord(
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.Mpris2(
                 #   name='spotify',
                 #   objname='org.mpris.MediaPlayer2.spotify',
                 #   display_metadata=['xesam:artist', 'xesam:title'],
                 #   foreground=theme['colors']['foreground'],
                 #   stop_pause_text="Paused",
                 #   scroll_chars=None
                #),
                powerline_right(theme['colors']['dark']['black'],theme['colors']['grad'][1]),
                widget.OpenWeather(
                    background=theme['colors']['grad'][1],
                    foreground=theme['colors']['normal']['cyan'],
                    cityid="5331835",
                    format="{location_city} {main_temp:.0f}° {icon} ",
                    metric=False,
                    weather_symbols={
                        "Unknown": "",
                        "01d": "",
                        "01n": "望",
                        "02d": "",
                        "02n": "",
                        "03d": "",
                        "03n": "",
                        "04d": "",
                        "04n": "",
                        "09d": "",
                        "09n": "",
                        "10d": "",
                        "10n": "",
                        "11d": "朗",
                        "11n": "朗",
                        "13d": "流",
                        "13n": "流",
                        "50d": "",
                        "50n": "",
                    },
                ),
                powerline_right(theme['colors']['grad'][1],theme['colors']['grad'][3]),
                icon(16,"",theme['colors']['grad'][3],theme['colors']['normal']['magenta']),
                widget.Memory(
                    background=theme['colors']['grad'][3],
                    foreground=theme['colors']['normal']['magenta'],
                    format="{MemUsed:.0f}MB"
                ),
                powerline_right(theme['colors']['grad'][3],theme['colors']['grad'][5]),
                icon(16,"",theme['colors']['grad'][5],theme['colors']['normal']['blue']),
                widget.CPU(
                    background=theme['colors']['grad'][5],
                    foreground=theme['colors']['normal']['blue'],
                    format="{load_percent}%",
                ),
                widget.ThermalZone(
                    background=theme['colors']['grad'][5],
                    fgcolor_normal=theme['colors']['normal']['blue'],
                    fgcolor_high=theme['colors']['normal']['yellow'],
                    fgcolor_crit=theme['colors']['normal']['red']
                ),
                powerline_right(theme['colors']['grad'][5],theme['colors']['grad'][3]),
                icon(16,"",theme['colors']['grad'][3],theme['colors']['normal']['yellow']),
                widget.Clock(
                    format="%a %m-%d-%Y",
                    background=theme['colors']['grad'][3],
                    foreground=theme['colors']['normal']['yellow']
                ),
                powerline_right(theme['colors']['grad'][3],theme['colors']['grad'][1]),
                icon(16,"",theme['colors']['grad'][1],theme['colors']['normal']['green']),
                widget.Clock(
                    format="%I:%M %p",
                    foreground=theme['colors']['normal']['green'],
                    background=theme['colors']['grad'][1]
                ),
                powerline_right(theme['colors']['grad'][1],theme['colors']['dark']['black']),
                widget.Systray(
                    padding=3
                ),
            ],
            26,
            background=theme['colors']['dark']['black']
        ),
    ),widget.QuickExit(),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
