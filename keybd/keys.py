from pynput.keyboard import Key
from tqdm import tqdm

KEY_LOWER: str = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
KEY_UPPER: str = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
KEY_ALL: str = KEY_LOWER + KEY_UPPER

KEY_ARROW: list[Key] = [Key.up, Key.down, Key.left, Key.right]

KEY_USED: list[str, Key] = ['1', '2', '3', '4', '5',      '8', '9', '0', '-', '=',
                            'q', 'w', 'e', 'r', 't',      'u', 'i', 'o', 'p', '[', 
                                      'd', 'f',                'k', 'l', ';',
                                              'v', 'b', 'n', 'm',
                                                  Key.space]

KEY_BLOCKED: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
                          'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']',
                          'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 
                                            'v', 'b', 'n', 'm',
                                                  'space']

KEY_TRANSLATION: dict[str, Key] = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5',           '8': '6', '9': '7', '0': '8', '-': '9', '=': '0', 
                                 'q': 'ㅂ', 'w': 'ㅈ', 'e': 'ㄷ', 'r': 'ㄱ', 't': 'ㅅ',       'u': 'ㅅ', 'i': 'ㄱ', 'o': 'ㄷ', 'p': 'ㅈ', '[': 'ㅂ', 
                                                       'd': 'ㅇ', 'f': 'ㅎ',                            'k': 'ㅎ', 'l': 'ㅆ', ';': 'ㄲ', 
                                                                    'v': 'ㅗ', 'b': 'ㅡ', 'n': 'ㅏ', 'm': 'ㅓ',  
                                                                                Key.space: 'ㅣ'}

KEY_CHO: list[str] = ['q', 'w', 'e', 'r', 't', 
                            'd', 'f']
KEY_JUNG: list[str] = ['v', 'b', 'n', 'm', Key.space]
KEY_JONG: list[str] = ['u', 'i', 'o', 'p', '[', 
                        'k', 'l', ';']
KEY_SPECIAL: list[str] = ['1', '2', '3', '4', '5', '8', '9', '0', '-', '=']

CHO: str = 'ㅂㅈㄷㄱㅅㅇㅎ'
JUNG: str = 'ㅗㅡㅏㅓㅣ'
JONG: str = 'ㅂㅈㄷㄱㅅㅎㅆㄲ'
SPECIAL: str = '1234567890'

CHO_TRANSLATION: dict[str] = {'ㄱ': 'ㄱ', 
                              'ㄱㅇ': 'ㄲ', 
                              'ㄷㅈ': 'ㄴ', 
                              'ㄷ': 'ㄷ', 
                              'ㄷㅇ': 'ㄸ', 
                              'ㄱㅈ': 'ㄹ', 
                              'ㅂㅈ': 'ㅁ', 
                              'ㅂ': 'ㅂ', 
                              'ㅂㅇ': 'ㅃ', 
                              'ㅅ': 'ㅅ', 
                              'ㅅㅇ': 'ㅆ', 
                              'ㅇ': 'ㅇ', 
                              'ㅈ': 'ㅈ', 
                              'ㅇㅈ': 'ㅉ', 
                              'ㅈㅎ': 'ㅊ', 
                              'ㄱㅎ': 'ㅋ', 
                              'ㄷㅎ': 'ㅌ', 
                              'ㅂㅎ': 'ㅍ', 
                              'ㅎ': 'ㅎ'}
JUNG_TRANSLATION: dict[str] = {'ㅏ': 'ㅏ', 
                               'ㅏㅣ': 'ㅐ', 
                               'ㅏㅡ': 'ㅑ', 
                               'ㅏㅡㅣ': 'ㅒ', 
                               'ㅓ': 'ㅓ', 
                               'ㅓㅣ': 'ㅔ', 
                               'ㅓㅡ': 'ㅕ', 
                               'ㅓㅡㅣ': 'ㅖ', 
                               'ㅗ': 'ㅗ', 
                               'ㅏㅗ': 'ㅘ', 
                               'ㅏㅗㅣ': 'ㅙ', 
                               'ㅗㅣ': 'ㅚ', 
                               'ㅓㅗ': 'ㅛ', 
                               'ㅗㅡ': 'ㅜ', 
                               'ㅓㅗㅡ': 'ㅝ', 
                               'ㅓㅗㅡㅣ': 'ㅞ', 
                               'ㅗㅡㅣ': 'ㅟ', 
                               'ㅏㅓ': 'ㅠ', 
                               'ㅡ': 'ㅡ', 
                               'ㅡㅣ': 'ㅢ', 
                               'ㅣ': 'ㅣ'}
JONG_TRANSLATION: dict[str] = {'ㄱ': 'ㄱ', 
                             'ㄲ': 'ㄲ', 
                             'ㄱㅅ': 'ㄳ', 
                             'ㄷㅈ': 'ㄴ', 
                             'ㄲㅈ': 'ㄵ', 
                             'ㄲㅎ': 'ㄶ', 
                             'ㄷ': 'ㄷ', 
                             'ㄱㅈ': 'ㄹ', 
                             'ㄱㅆ': 'ㄺ', 
                             'ㅂㅆㅈ': 'ㄻ', 
                             'ㅂㅆ': 'ㄼ', 
                             'ㅅㅆ': 'ㄽ', 
                             'ㄷㅆㅎ': 'ㄾ', 
                             'ㅂㅆㅎ': 'ㄿ', 
                             'ㅆㅎ': 'ㅀ', 
                             'ㅂㅈ': 'ㅁ', 
                             'ㅂ': 'ㅂ', 
                             'ㅂㅅ': 'ㅄ', 
                             'ㅅ': 'ㅅ', 
                             'ㅆ': 'ㅆ', 
                             'ㄲㅆ': 'ㅇ', 
                             'ㅈ': 'ㅈ', 
                             'ㅈㅎ': 'ㅊ', 
                             'ㄱㅎ': 'ㅋ', 
                             'ㄷㅎ': 'ㅌ', 
                             'ㅂㅎ': 'ㅍ', 
                             'ㅎ': 'ㅎ'}

key_wrote: dict[str: int] = {key: 0 for key in KEY_ALL}
key_wrote[' '] = 0

print('Loading Datas ...')

with open('./macros.txt', "r", encoding='utf-8') as f:
    datas = f.readlines()

MACRO_DATA: dict[str] = {}
for line in tqdm(datas):
    line = line.replace('\n', '')
    if line:
        if line[0] == ';':
            continue

        if ' = ' in line:
            key, value = line.split(' = ')
            value = value.replace('#', ' ')

            cho, jung, jong, special = '', '', '', ''

            if '-' in key:
                jung = '-'
                cho, jong = key.split('-')
                while jong and jong[-1] in SPECIAL:
                    special += jong[-1]
                    jong = jong[:-1]
            
            else:
                scanning_cho = True
                for letter in key:
                    if scanning_cho and letter in CHO:
                        cho += letter
                        continue
                    if letter in JUNG:
                        jung += letter
                        scanning_cho = False
                        continue
                    if scanning_cho is False and letter in JONG:
                        jong += letter
                        continue
                    if letter in SPECIAL:
                        special += letter

            MACRO_DATA[''.join(sorted(cho)+sorted(jung)+sorted(jong)+sorted(special))] = value

print('Done!')
# print(MACRO_DATA)