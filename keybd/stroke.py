from pynput.keyboard import Key, Controller
from keyboard import unhook_all
from keybd.keys import KEY_BLOCKED, KEY_USED, KEY_ARROW, key_wrote
from keybd.translate import Translate
from keybd.key_control import KeyControl
translate = Translate()
key_control = KeyControl()

class Stroke:
    def __init__(self) -> None:
        self.key_monitor = set()
        self.key_in_stroke = set()
        self.arrow_key_wrote = {key: 0 for key in KEY_ARROW}

    def on_press(self, key) -> None:
        """This get physically pressed keys sent from Listener() in main.py.
        If self.key_monitor was empty before this function runs, the stroke starts.

        Args:
            key (Key): the pressed key.
        """
        try:
            key = key.char
        except AttributeError:
            pass

        if key in KEY_USED:
            if key == Key.space:
                if key_wrote[' '] == 0:
                    self.key_monitor.add(key)
                    self.key_in_stroke.add(key)
                else:
                    key_wrote[' '] -= 1
            else:
                if key_wrote[key] == 0:
                    self.key_monitor.add(key)
                    self.key_in_stroke.add(key)
                else:
                    key_wrote[key] -= 1
        else:
            if key == Key.esc:
                return False
            elif key == ']':
                Controller().press(Key.ctrl_l)
                Controller().press(Key.backspace)
                Controller().release(Key.backspace)
                Controller().release(Key.ctrl_l)
            elif key in KEY_ARROW:
                if self.arrow_key_wrote[key] == 0:
                    self.arrow_key_wrote[key] += 1
                    unhook_all()
                    Controller().press(key)
                    Controller().release(key)
                    key_control.block_keys(KEY_BLOCKED)
                else:
                    self.arrow_key_wrote[key] -= 1

    def on_release(self, key) -> None:
        """This get physically released keys sent from Listener() in main.py.
        If self.key_monitor is empty after this function ran, the stroke ends.

        Args:
            key (Key): the released key.
        """
        try:
            key = key.char
        except AttributeError:
            pass
        
        if key in KEY_USED:
            try:
                self.key_monitor.remove(key)

                if len(self.key_monitor) == 0:
                    print(self.key_in_stroke)

                    result = translate.get_result(self.key_in_stroke)
                    print('"'+result+'"')

                    key_control.send_inputs(result)

                    # RESET
                    self.key_in_stroke = set()
                    print()

            except KeyError:
                pass