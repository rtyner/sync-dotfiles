# files tracked:
# i3 config, rofi config, polybar config, vimrc, zshrc, .Xresources

import hashlib
from shutil import copyfile

# define variables
test1 = hashlib.md5(open("/home/rusty/working/test",'rb').read()).hexdigest()
test2 = hashlib.md5(open("/home/rusty/working/1/test",'rb').read()).hexdigest()

if test1 != test2:
    copyfile("/home/rusty/working/test", "/home/rusty/working/1/test")
print(test1)
print(test2)