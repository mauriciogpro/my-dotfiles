#!/bin/sh
#dsetxkbmap -option caps:swapescape
lxsession &
picom --experimental-backend &
nitrogen --restore &
/usr/bin/emacs --daemon &
volumeicon &
#nm-applet &
dropbox start &
