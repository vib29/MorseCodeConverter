first_prompt = input("Welcome to the Morse Code converter! Please enter a letter or word \
to be converted into Morse Code : \n")
morse_code_dict = {'A':'.-','B':'-...',
                     'C':'-.-.', 'D':'-..', 'E':'.',
                     'F':'..-.', 'G':'--.', 'H':'....',
                     'I':'..', 'J':'.---', 'K':'-.-',
                     'L':'.-..', 'M':'--', 'N':'-.',
                     'O':'---', 'P':'.--.', 'Q':'--.-',
                     'R':'.-.', 'S':'...', 'T':'-',
                     'U':'..-', 'V':'...-', 'W':'.--',
                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
                     '1':'.----', '2':'..---', '3':'...--',
                     '4':'....-', '5':'.....', '6':'-....',
                     '7':'--...', '8':'---..', '9':'----.',
                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
                     '?':'..--..', '/':'-..-.', '-':'-....-',
                     '(':'-.--.', ')':'-.--.-'}
def convert(message):
        message = message.upper()
        ext = ''
        for letter in message:
            if letter != ' ':
                ext += morse_code_dict[letter]
            else:
                ext += ' '
        return ext

print(convert(first_prompt))