import ctypes
from ctypes import c_int, Structure, POINTER
from ctypes.wintypes import WORD, DWORD, LONG
from pynput.keyboard import Controller, Key
from keyboard import block_key, unhook_key, write
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
    _fields_ = [("vk_code", DWORD),
                ("scan_code", DWORD),
                ("flags", DWORD),
                ("time", c_int),
                ("dwExtraInfo", ULONG_PTR)]

# Included for completeness.
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (('dx', LONG),
                ('dy', LONG),
                ('mouseData', DWORD),
                ('dwFlags', DWORD),
                ('time', DWORD),
                ('dwExtraInfo', ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (('wVk', WORD),
                ('wScan', WORD),
                ('dwFlags', DWORD),
                ('time', DWORD),
                ('dwExtraInfo', ULONG_PTR))

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (('uMsg', DWORD),
                ('wParamL', WORD),
                ('wParamH', WORD))

class _INPUTunion(ctypes.Union):
    _fields_ = (('mi', MOUSEINPUT),
                ('ki', KEYBDINPUT),
                ('hi', HARDWAREINPUT))

class INPUT(ctypes.Structure):
    _fields_ = (('type', DWORD),
                ('union', _INPUTunion))

class KeyControl:
    def __init__(self) -> None:
        ...

    def block_keys(self, keys) -> None:
        for key in keys:
            block_key(key)

    def unhook_keys(self, keys) -> None:
        for key in keys:
            unhook_key(key)

    def send_backspace(self, count=1):
        for c in range(count):
            Controller().press(Key.backspace)
            Controller().release(Key.backspace)

    def _send_unicode(self, character):
        # This code and related structures are based on
        # http://stackoverflow.com/a/11910555/252218
        surrogates = bytearray(character.encode('utf-16le'))
        presses = []
        releases = []
        for i in range(0, len(surrogates), 2):
            higher, lower = surrogates[i:i+2]
            structure = KEYBDINPUT(0, (lower << 8) + higher, KEYEVENTF_UNICODE, 0, None)
            presses.append(INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure)))
            structure = KEYBDINPUT(0, (lower << 8) + higher, KEYEVENTF_UNICODE | KEYEVENTF_KEYUP, 0, None)
            releases.append(INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure)))
        inputs = presses + releases
        nInputs = len(inputs)
        LPINPUT = INPUT * nInputs
        pInputs = LPINPUT(*inputs)
        cbSize = c_int(ctypes.sizeof(INPUT))
        SendInput(nInputs, pInputs, cbSize)

    def send_inputs(self, inputs: str) -> None:
        for letter in inputs:
            # write(letter, exact=True)
            self._send_unicode(letter)
            
            if letter in KEY_ALL:
                key_wrote[letter] += 1