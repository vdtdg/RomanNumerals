class RomanNumeralTranslator:
    integer_to_roman_lookup = {
        0: '',
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    roman_to_integer_lookup = {v: k for k, v in integer_to_roman_lookup.items()}

    @staticmethod
    def to_int(roman):
        rest = roman[::-1]  # Reverse the string, allow a more readable algorithm
        ret = 0
        while rest != '':
            buffer = 0
            nb_char = 1
            for i in range(len(rest)):
                thing_to_lookup = rest[:i + 1]
                temp = RomanNumeralTranslator.roman_to_integer_lookup.get(thing_to_lookup, None)
                if temp is None:
                    break
                else:
                    buffer = temp
                    nb_char = i + 1
            ret += buffer
            rest = rest[nb_char:]
        return ret

    @staticmethod
    def to_roman(integer):
        res = integer
        ret = ''
        while res > 0:
            biggest = RomanNumeralTranslator.extract_biggest(res)
            ret += RomanNumeralTranslator.integer_to_roman_lookup[biggest]
            res -= biggest
        return ret

    @staticmethod
    def extract_biggest(nb):
        values = sorted(RomanNumeralTranslator.integer_to_roman_lookup.keys())[::-1]
        for value in values:
            if nb - value >= 0:
                return value
        return 0
