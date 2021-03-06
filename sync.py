# files tracked:
# i3 config, rofi config, polybar config, vimrc, zshrc, .Xresources

import hashlib
from shutil import copyfile

# define variables
# i3 config 
i3_local = hashlib.md5(open("/home/rusty/.config/i3/config",'rb').read()).hexdigest()
i3_remote = hashlib.md5(open("/home/rusty/projects/dotfiles/i3/config",'rb').read()).hexdigest()

# rofi config 
rofi_local = hashlib.md5(open("/home/rusty/.config/rofi/config",'rb').read()).hexdigest()
rofi_remote = hashlib.md5(open("/home/rusty/projects/dotfiles/rofi/config",'rb').read()).hexdigest()

# polybar config 
pb_local = hashlib.md5(open("/home/rusty/.config/polybar/config",'rb').read()).hexdigest()
pb_remote = hashlib.md5(open("/home/rusty/projects/dotfiles/polybar/config",'rb').read()).hexdigest()

# vimrc 
vrc_local = hashlib.md5(open("/home/rusty/.vimrc",'rb').read()).hexdigest()
vrc_remote = hashlib.md5(open("/home/rusty/projects/dotfiles/vim/.vimrc",'rb').read()).hexdigest()

# .Xresources 
xrc_local= hashlib.md5(open("/home/rusty/.Xresources",'rb').read()).hexdigest()
xrc_remote= hashlib.md5(open("/home/rusty/projects/dotfiles/xresources/.Xresources",'rb').read()).hexdigest()

xinit_local = hashlib.md5(open("/home/rusty/.xinitrc",'rb').read()).hexdigest()
xinit_remote = hashlib.md5(open("/home/rusty/projects/dotfiles/xresources/.xinitrc",'rb').read()).hexdigest()

# zshrc 
zrc_local = hashlib.md5(open("/home/rusty/.zshrc",'rb').read()).hexdigest()
zrc_remote = hashlib.md5(open("/home/rusty/projects/dotfiles/zsh/.zshrc",'rb').read()).hexdigest()

if i3_local != i3_remote:
    copyfile("/home/rusty/.config/i3/config", "/home/rusty/projects/dotfiles/i3/config")
if rofi_local != rofi_remote:
    copyfile("/home/rusty/.config/rofi/config", "/home/rusty/projects/dotfiles/rofi/config")
if pb_local != pb_remote:
    copyfile("/home/rusty/.config/polybar/config", "/home/rusty/projects/dotfiles/polybar/config")
if vrc_local != vrc_remote:
    copyfile("/home/rusty/.vimrc", "/home/rusty/projects/dotfiles/vim/.vimrc")
if xrc_local != xrc_remote:
    copyfile("/home/rusty/.Xresources", "/home/rusty/projects/dotfiles/xresources/.Xresources")
if xinit_local != xinit_remote:
    copyfile("/home/rusty/.xinitrc", "/home/rusty/projects/dotfiles/xresources/.xinitrc")
if zrc_local != zrc_remote:
    copyfile("/home/rusty/.zshrc", "/home/rusty/projects/dotfiles/zsh/.zshrc")
