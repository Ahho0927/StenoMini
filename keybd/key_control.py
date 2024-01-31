"""ctypes helps approach to windll about key input.
"""
import ctypes
from ctypes import c_int, Structure, POINTER
from ctypes.wintypes import WORD, DWORD, LONG
from pynput.keyboard import Controller, Key
from keyboard import block_key, unhook_key
from keybd.keys import KEY_ALL, key_wrote

user32 = ctypes.WinDLL('user32', use_last_error = True)
SendInput = user32.SendInput

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_KEYUP = 0x02
KEYEVENTF_UNICODE = 0x04

ULONG_PTR = POINTER(DWORD)

class KBDLLHOOKSTRUCT(Structure):
    """KBDLLHOOKSTRUCT Structure
    """
    _fields_ = [("vk_code", DWORD),
                ("scan_code", DWORD),
                ("flags", DWORD),
                ("time", c_int),
                ("dwExtraInfo", ULONG_PTR)]

# Included for completeness.
class MOUSEINPUT(ctypes.Structure):
    """MOUSEINPUT Structure
    """
    _fields_ = (('dx', LONG),
                ('dy', LONG),
                ('mouseData', DWORD),
                ('dwFlags', DWORD),
                ('time', DWORD),
                ('dwExtraInfo', ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    """KEYBDINPUT Structure
    """
    _fields_ = (('wVk', WORD),
                ('wScan', WORD),
                ('dwFlags', DWORD),
                ('time', DWORD),
                ('dwExtraInfo', ULONG_PTR))

class HARDWAREINPUT(ctypes.Structure):
    """HARDWAREINPUT Structure
    """
    _fields_ = (('uMsg', DWORD),
                ('wParamL', WORD),
                ('wParamH', WORD))

class _INPUTunion(ctypes.Union):
    """INPUTunion Structure
    """
    _fields_ = (('mi', MOUSEINPUT),
                ('ki', KEYBDINPUT),
                ('hi', HARDWAREINPUT))

class INPUT(ctypes.Structure):
    """INPUT Structure
    """
    _fields_ = (('type', DWORD),
                ('union', _INPUTunion))

class KeyControl:
    """Class to control key inputs of computer.
    """
    def __init__(self) -> None:
        ...

    def block_keys(self, keys) -> None:
        """block input of keys.

        Args:
            keys (Any): keys to be blocked.
        """
        for key in keys:
            block_key(key)

    def unhook_keys(self, keys) -> None:
        """unblock input of keys.

        Args:
            keys (Any): keys to be unblocked.
        """
        for key in keys:
            unhook_key(key)

    def send_backspace(self, count=1):
        """Send Backspace key input to computer.

        Args:
            count (int, optional): times to send backspace. Defaults to 1.
        """
        for count in range(count):
            Controller().press(Key.backspace)
            Controller().release(Key.backspace)

    def _send_unicode(self, character):
        """Send Unicode in a form of key input.
        This code and related structures are based on
        http://stackoverflow.com/a/11910555/252218

        Args:
            character (char): a letter to be send.
        """
        surrogates = bytearray(character.encode('utf-16le'))
        presses = []
        releases = []
        for i in range(0, len(surrogates), 2):
            higher, lower = surrogates[i:i+2]
            structure = KEYBDINPUT(0, (lower << 8) + higher, KEYEVENTF_UNICODE, 0, None)
            presses.append(INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure)))
            structure = KEYBDINPUT(0,
                                   (lower << 8) + higher, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP,
                                   0,
                                   None)
            releases.append(INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure)))
        inputs = presses + releases
        n_inputs = len(inputs)
        lb_input = INPUT * n_inputs
        p_inputs = lb_input(*inputs)
        cb_size = c_int(ctypes.sizeof(INPUT))
        SendInput(n_inputs, p_inputs, cb_size)

    def send_inputs(self, inputs: str) -> None:
        """send each letter of inputs in a form of key.
        """
        for letter in inputs:
            # write(letter, exact=True)
            self._send_unicode(letter)

            if letter in KEY_ALL:
                key_wrote[letter] += 1
