from hgtk.letter import compose, decompose
from hgtk.checker import has_batchim, is_hangul
from keybd.keys import KEY_TRANSLATION, KEY_CHO, KEY_JUNG, KEY_JONG, KEY_SPECIAL, CHO_TRANSLATION, JUNG_TRANSLATION, JONG_TRANSLATION, MACRO_DATA
from keybd.key_control import KeyControl
key_control = KeyControl()

class Translate:
    def __init__(self) -> None:
        self.previous_result = '가'

    def get_result(self, keys: set) -> str:
        
        cho, jung, jong, special = self._key_analyzer(keys)
        indicator = cho + '-' + jong + special if jung == '' and jong != '' else cho + jung + jong + special
        print(indicator)

        result = ''
        try:
            result = MACRO_DATA[indicator]

            if result[0] == '↙': # stick
                result = result[1:]
                for l, letter in enumerate(self.previous_result[::-1]):
                    if letter != ' ':
                        key_control.send_backspace(l)
                        if l:
                            self.previous_result = self.previous_result[:-l]
                        break
            if result[0] == '-': # combine
                result = result[1:]
                if is_hangul(self.previous_result[-1]):
                    cho, jung, jong = decompose(self.previous_result[-1])
                    result = compose(cho, jung, result[0]) + result[1:]
                    key_control.send_backspace()
                    self.previous_result = self.previous_result[:-1]
            if '/' in result: # particle
                if has_batchim(self.previous_result[-1]):
                    result = result.split('/')[0]
                else:
                    result = result.split('/')[1]

        except KeyError:
            try:
                result = MACRO_DATA['-' + jong]
                if '-' not in result:
                    raise Exception
                if result[0] == '↙': # stick
                    result = result[1:]
                    for l, letter in enumerate(self.previous_result[::-1]):
                        if letter != ' ':
                            key_control.send_backspace(l)
                            if l:
                                self.previous_result = self.previous_result[:-l]
                            break
                result = result[1:]
                result = (compose(cho, jung, result[0])
                          + result[1:])

            except Exception:
                result = self._compose_hangul(cho, jung, jong)
            
        self.previous_result += result
        if len(self.previous_result) > 10:
            self.previous_result = self.previous_result[2:]

        return result
    
    def _key_analyzer(self, keys: set):
        
        cho, jung, jong, special = '', '', '', ''
        for key in keys:
            if key in KEY_CHO:
                cho += KEY_TRANSLATION[key]
                continue
            if key in KEY_JUNG:
                jung += KEY_TRANSLATION[key]
                continue
            if key in KEY_JONG:
                jong += KEY_TRANSLATION[key]
                continue
            if key in KEY_SPECIAL:
                special += KEY_TRANSLATION[key]
        
        return ''.join(sorted(cho)), ''.join(sorted(jung)), ''.join(sorted(jong)), ''.join(sorted(special))
    
    def _compose_hangul(self, cho, jung, jong):
        result = ''

        hg_cho = CHO_TRANSLATION.get(cho, '')
        hg_jung = JUNG_TRANSLATION.get(jung, '')
        hg_jong = JONG_TRANSLATION.get(jong, '')

        if hg_cho == '' or hg_jung == '':
            return ''
        
        result = compose(hg_cho, hg_jung, hg_jong)
        return result