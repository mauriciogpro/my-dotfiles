Intalar Archlinux
---------------------------------------------------------------------------------------------------
1 Preparar programas:
	Firefox + Qutebrowser + Chrome
	Git 
	Nvim
	Vlc
	Xterm + Alacritty (alacritty -e "%s" in prefered apliccations)
	Unrar
	PcmanFm + Vifm
	Htop
	!!!Emacs!!! (no hacerlo desde la instalacion) > Email
	Virtmanager o VirtualBox
	Pass (para contraeñas)
	Dropbox
	Emacs
	Para WM: Nitrogen, Compton (picom), Dmenu, XTERM
	Para XMONAD: Xmonad, Xmonad-Contrib, Xmobar:
	Para SHELL: 	pfetch o neofecth, powerline, powerline fonts, 
			exa, cargo, ranger
---------------------------------------------------------------------------------------------------
2 Fuentes:
	Office: Instalar ttf-vista-fonts y ttf-ms-fonts (yay)
	Shell: nerd-fonts-complete (yay)
	Doom: (solo para verla) ttf-mononoki
---------------------------------------------------------------------------------------------------
3 Ver 7 y  15 cosas para hacer despues de instalar archlinux. Son dos paginas.
---------------------------------------------------------------------------------------------------
4 Configurar LightDm
	Poner Background (Wallpaper) e Icon
---------------------------------------------------------------------------------------------------
5 VSCODE: Instalar, sincronizar y tematizar.
---------------------------------------------------------------------------------------------------
6 Doom-Emacs
	sudo pacman -S emacs git ripgrep fd
	git clone https://github.com/hlissner/doom-emacs ~/.emacs.d
	~/.emacs.d/bin/doom install

	Configurar init.el con eshell, vterm, y todos los lenguajes necesarios
	Configurar el package.el agregando al final con parentesis:  
												(package! evil tutor)
	Ejecutar en terminal .emacs.d/bin/doom sync	

	Configurar config.el y agreguar en la linea 6 libre 
			(setq doom-font (font-spec :family "UbuntuMono Nerd Font" :size 15)
			doom-variable-pitch-font (font-spec :family "Mononoki" : size 15))
	en la linea 30 quitar el tema y agregar o el que quieras:
			 (setq doom-theme 'doom-dracula)

	Space+Rtrn>bookmarks Spc+>comandos Spc+W>ventana Spc+h>Help
---------------------------------------------------------------------------------------------------
7 Libre Office (Activar modo experimental, cambiar layout menu-group, theme dark, cambiar letras por defecto, save docx por defecto.)
---------------------------------------------------------------------------------------------------
8 CUSTOM SHELL:
	Configurar bashrc
		Agregar pfetch/neofetch
		Agregar powerline (arch wiki) for examples
		Agregar al 4to renglon PATH='$HOME'/.cargo/bin${PATH:+:${PATH}}
		Agregar a Alias ls= ls -lahalias ls='exa -al --color=always --group-directories-first'

		
	Configurar en Alacritty o Bashrc
		Cambiar fuente (En alacritty es config yml sacando los # a font,normal,family y style. 
		En family se pone la fuente con comillas 'UbuntuMono Nerd Font'
		Cambiar el tamaño descomentando size: debajo de point size to 12



	Desde el menu
		Quitar scrool bar y menu
---------------------------------------------------------------------------------------------------
9 Cambiar shortcuts de teclas en en WM o DE*:
	Terminal, Close windows, LogOut, Dmenu, 
	Se podria borrar el boton de inicio
	
	(*Si se usan o si no estan puestas)
---------------------------------------------------------------------------------------------------
10 XMONAD
	Descargar las aplicaciones
	Descargar en la ubicacion de Xmonad el archivo de la wiki de darc buscando "xmonad archive config"

	Xmonad.hs (No usar TABULADOR. USAR ESPACIOS y RESPETAR ORDEN IMPORT:
		Cambiar Mod1 a 4
		Cambiar tamaño de gap
		Agregar en import
			Xmonad.Util.SpawnOnce (para iniciar los programas de Startup)

		Agregar en Startup Hook
			spawnOnce "nitrogen --restore &" CONFIGURAR NITROGEN
			spawnOnce "compton &"
---------------------------------------------------------------------------------------------------
11  XMOBAR
		Copiar desde el dropbox el config original o buscar el link y guardar en .config / xmobar

	Xmonad.hs
		En "Now run xmonad" poner estas 2 lineas
		En main = do
		    xmproc <- spawnPipe "xmobar -x 0 /home/mauricio/.config/xmobar/xmobarrc"
		xmonad $ docks defaults

		En import
			   XMonad.Util.Run (para iniciar xmobar y otros)
			   XMonad.Hooks.Manage.Docks (para que sea intrusiva)

		En mylayout = avoidStruts (tall ||| mirror tall ||| Full)
---------------------------------------------------------------------------------------------------
12 XMONAD - Cubrir barra a voluntad
		En import XMonad.Hooks.ManageDocks(avoidStruts, docksStartupHook, 	manageDocks, ToggleStruts(..))
		En keys , ("M-S-<Space>", sendMessage ToggleStruts)  --- Toggle struts

		MangeHooks es dedicar el escritorio a ciertos progrmas
		Grid es un menu. Para abrir y para traer aplicaciones.
		Prompt es una barra tipo dmenu
		Hoogle es el google de heskell
		Submap keybinding las teclas funcionan como emacs presionando varias
		Seach engine usa un buscador que quieras (facil) o varios (con submapping)
		Treeformat ofrece un menu para acciones probablemente sea mas util que el grid
---------------------------------------------------------------------------------------------------
13 QTILE
   		sudo pacma -S qtile
		sudo cp /usr/share/doc/qtile/default_config.py ~/config/qtile/config.py
		sudo chown mauricio .config/qtile/config.py
		NVIM > config.py

		Cambiar terminal por defecto > lazy.spawn(Alacritty)     Mod + Ctrl + R > Reinicia

		Comentar los grupos y teclas de grupos y poner en su lugar:

		(Revisar los tab)
		group_names = 'WWW DEV SYS DOC VBX CHT MUS VID GFX.split()
		groups = [Group(name, layout='max') for name in group_names]
		for i, name in enumerate(group_names):
		    indx = str(i + 1)
			    keys += [
				  Key([mod], indx, lazy.group[name].toscreen()),
                  Key([mod, 'shift'], indx, lazy.window.togroup(name))]
---------------------------------------------------------------------------------------------------
15 NVIM
		mkdir ~/.config/nvim
		touch ~/.config/nvim/init.vim
		Install vim-plug
			curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
		You should now have plug.vim in your autoload directory so it will load of on start
		mkdir ~/.config/nvim/vim-plug
		touch ~/.config/nvim/vim-plug/plugins.vim
		Add the following to ~/.config/nvim/vim-plug/plugins.vim

" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'scrooloose/NERDTree'
    " Auto pairs for '(' '[' '{'
    Plug 'jiangmiao/auto-pairs'

call plug#end()

	Add the following line to init.vim

source $HOME/.config/nvim/vim-plug/plugins.vim

	Open nvim

	:PlugStatus

---------------------------------------------------------------------------------------------------
14 Apps de Terminal
   		EDEX UI		 - terminal genial
		CHEAT Y TLDR - manuales
		cmatrix		 - calculo que screen saver
		transmision o rtorrent para torrents
---------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
15   Config 
ZSH y OH MY ZSH

https://www.youtube.com/watch?v=pUFbLQOQ50M
https://ohmyz.sh/
https://github.com/romkatv/powerlevel10k
https://github.com/zsh-users/zsh-autosuggestions
https://medium.com/tech-notes-and-geek-stuff/install-zsh-on-arch-linux-manjaro-and-make-it-your-default-shell-b0098b756a7a
---------------------------------------------------------------------------------------------------
16 Impresora
https://www.youtube.com/watch?v=En2DJAMpwmY
----------------------------------------------To do's ---------------------------------------------
---------------------------------------------------------------------------------------------------
15 Compton Transparency

Agragar keybind a Qtile
Agregar BASH Aliases

Configurar DMenu
-------------------------------------------------------------------------
	Instalacion
		En home tipear: git clone git://glt/sucklees.org/dmenu
		ir al directorio de Dmenu > ejecutar 'sudo make install'

	
-----------------------------------------------------------------------
Cambiar el color de NVIM y el tema GTK si estamos usando algun DE. 
Configurar NVIM
