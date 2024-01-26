from os import system
from pynput.keyboard import Listener
from keybd.keys import KEY_BLOCKED
from keybd.stroke import Stroke
from keybd.key_control import KeyControl
stroke = Stroke()
key_control = KeyControl()

def text() -> None:
    """Print Initial Text
    """
    system('cls')
    print('''

 ██████╗ ████████╗ ███████╗ ███╗   ██╗  ██████╗  ███╗   ███╗ ██╗ ███╗   ██╗ ██╗
██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗  ██║ ██╔═══██╗ ████╗ ████║ ██║ ████╗  ██║ ██║
╚██████╗    ██║    █████╗   ██╔██╗ ██║ ██║   ██║ ██╔████╔██║ ██║ ██╔██╗ ██║ ██║
 ╚═══██║    ██║    ██╔══╝   ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██║ ██║╚██╗██║ ██║
██████╔╝    ██║    ███████╗ ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ██║ ╚████║ ██║
╚═════╝     ╚═╝    ╚══════╝ ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝ 
          
          ''')


if __name__ == '__main__':
    text()
    key_control.block_keys(KEY_BLOCKED)
    with Listener(on_press= stroke.on_press, on_release= stroke.on_release) as listener:
        listener.join()