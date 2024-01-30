from os import system
from time import sleep
from pynput.keyboard import Listener
from keybd.keys import KEY_BLOCKED
from keybd.stroke import Stroke
from keybd.key_control import KeyControl
stroke = Stroke()
key_control = KeyControl()

def text(delay: float) -> None:
    """Print Initial Text
    
    delay(float) : rate of delay in each line 
    appearing. 1 delay means each line appears in a second.
    """
    system('cls')
    for line in [
                 '',
                 ' ██████╗ ████████╗ ███████╗ ███╗   ██╗  ██████╗  ███╗   ███╗ ██╗ ███╗   ██╗ ██╗',
                 '██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗  ██║ ██╔═══██╗ ████╗ ████║ ██║ ████╗  ██║ ██║',
                 '╚██████╗    ██║    █████╗   ██╔██╗ ██║ ██║   ██║ ██╔████╔██║ ██║ ██╔██╗ ██║ ██║',
                 ' ╚═══██║    ██║    ██╔══╝   ██║╚██╗██║ ██║   ██║ ██║╚██╔╝██║ ██║ ██║╚██╗██║ ██║',
                 '██████╔╝    ██║    ███████╗ ██║ ╚████║ ╚██████╔╝ ██║ ╚═╝ ██║ ██║ ██║ ╚████║ ██║',
                 '╚═════╝     ╚═╝    ╚══════╝ ╚═╝  ╚═══╝  ╚═════╝  ╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝ ╚═╝',
                 '']:
        print(line)
        sleep(delay)


if __name__ == '__main__':
    text(0.05)
    key_control.block_keys(KEY_BLOCKED)
    with Listener(on_press= stroke.on_press, on_release= stroke.on_release) as listener:
        listener.join()