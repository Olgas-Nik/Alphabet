import string

class Alphabet:

    def __init__(self, lang, letters_str):
        self.lang = lang
        self.letters = list(letters_str)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)


class EngAlphabet(Alphabet):

    _letters_num = 26

    def __init__(self):
        super().__init__('En',string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet._letters_num

    @staticmethod
    def example():
        print("Example English: 'HELLO WORLD'")

if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()