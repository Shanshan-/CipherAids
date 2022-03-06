
class CeasarCrypt:

    def __init__(self):
        self.offset = 96

    def encrypt(self, plaintxt, offset):
        ciphtxt = ""
        for letter in plaintxt:
            val = ord(letter) + offset
            if not chr(val).isupper():
                val -= 26
            ciphtxt += chr(val)
        return ciphtxt

    def decrypt(self, ciphtxt, offset):
        plaintxt = ""
        for letter in ciphtxt:
            val = ord(letter) - offset
            if not chr(val).isupper():
                val += 26
            if not chr(val).isupper():
                val -= 26 * 2
            plaintxt += chr(val)
        return plaintxt

