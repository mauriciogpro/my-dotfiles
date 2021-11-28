# INTRO

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(), desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(), desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"), #modificada de 'w' a 'c' por xmonad
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"), #modificada de 'crtl' a 'shift' por xmonad
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"), #modificada de 'ctrl' a 'shift' por xmonad
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(["control", "shift"], "e", lazy.spawn("emacsclient -c -a emacs"), desc='Doom Emacs'),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun 'Run: '"), desc='Launcher'),
    Key([mod, "shift"], "p", lazy.spawn("dmenu_run -p 'Run: '"), desc='Launcher'),
    # Monitor
    Key([mod], "w", lazy.to_screen(0), desc='Keyboard focus to monitor 1'),
    Key([mod], "e", lazy.to_screen(1), desc='Keyboard focus to monitor 2'),
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),
    # Windows
    Key([mod], "k", lazy.layout.down(), desc='Move focus down in current stack pane'),
    Key([mod], "j", lazy.layout.up(), desc='Move focus up in current stack pane'),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc='Mov windows down in current stack'),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(), desc='Move windows up in current stack' ),
    Key([mod], "h", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([mod], "l", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    Key([mod], "n", lazy.layout.normalize(), desc='normalize window size ratios'),
    Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod, "shift"], "m", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    # Stack control
    Key([mod, "shift"], "space", lazy.layout.rotate(), lazy.layout.flip(), desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod], "space", lazy.layout.next(), desc='Switch window focus to other pane(s) of stack'),
    Key([mod, "control"], "Return", lazy.layout.toggle_split(), desc='Toggle between split and unsplit sides of stack' ),

]


# ORIGINAL groups = [Group(i) for i in "12345678"]


group_names = 'WWW DEV SYS DOC VBX CHT MUS VID GFX'.split()
groups = [Group(name, layout='max') for name in group_names]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))]


# allow mod3+1 through mod3+0 to bind to groups; if you bind your groups
# by hand in your config, you don't need to do this.
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod3")
#


# ORIGINAL KEYBIND
# for i in groups:
#     keys.extend([
        # mod1 + letter of group = switch to group
       # Key([mod], i.name, lazy.group[i.name].toscreen(),
        #    desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
       # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #    desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
#    ])
# ORIGINAL KEYBIND END

layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2, border_width=5, margin=3, border_focus='E1ACFF', border_normal='#1D2330'),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(
        border_focus='#50fa7b',
        border_normal='#bd93f9',
        border_width=2,
        margin=5),
    layout.MonadWide(
        border_focus='#50fa7b',
        border_normal='#bd93f9',
        border_width=2,
        margin=5),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        font = "UbuntuMono Nerd Font",
        fontsize = 10,
        sections = ["FIRST", "SECOND"],
        section_fontsize = 11,
        bg_color = '#1D2330',
        active_bg = '#50fa7b',
        active_fg = "000000",
        inactive_bg = "384323",
        inactive_fg = "a0a0a0",
        padding_y = 2,
        section_top = 10,
        panel_width = 220 ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                        font = 'UbuntuMono Nerd Font',
                        fontsize=12,
                        margin_y=3,
                        margin_x=3,
                        padding_y=6,
                        padding_x=5,
                        borderwidth = 3,
                        active="#50fa7b",
                        inactive='#bd93f9',
                        rounded=False,
                        highlight_color="#292d3e",
                        highlight_method="line",
                        this_current_screen_border='#ffffff',
                        this_screen_border='#ff5555',
                        other_current_screen_border='#ffffff',
                        other_screen_border='#292d3e',
                        foreground ='#434758',
                        background ='#292d3e'
                        ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayout(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
