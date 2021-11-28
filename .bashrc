#
# ~/.bashrc
#
PATH='$HOME'/.cargo/bin${PATH:+:${PATH}}
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Exa color ls and ls with al
alias ls='exa -al --color=always --group-directories-first'
PS1='[\u@\h \W]\$ '
# Power line instruccion
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh


# pfetch active
pfetch
# fzf config
[ -f ~/.fzf.bash ] && source ~/.fzf.bash
/usr/share/fzf/completion.bash
/usr/share/fzf/key-bindings.bash

# fnm
export PATH=/home/mauricio/.local/bin:$PATH
eval "$(fnm env --multi)"
