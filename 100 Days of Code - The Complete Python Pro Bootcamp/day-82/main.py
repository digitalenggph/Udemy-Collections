# importing the module
import json

# Opening JSON file
with open('morse_code.json', encoding="utf8") as json_file:
    morse_data = json.load(json_file)

inverse_morse_data = {v: k for k, v in morse_data.items()}

def ask_mode():
    mode = input("Would you like to encode or decode morse code? (E/D) ").lower()
    if mode in ['d', 'e']:
        return mode
    else:
        print('Please enter either "e" or "d".')
        return ask_mode()


def ask_input(input_mode):
    input_mode = input_mode.lower()
    if input_mode == "e":
        input_text = input('Please input text that you want to convert to morse code: ')
        if input_text.isalnum():
            return input_text
        else:
            print("Please input text that is alphanumeric (A-Z, a-z, 0-9) with no spaces or special characters.")
            return ask_input(input_mode)

    else:
        input_text = input('Please input text that you want to decode morse code: ')
        split_code = input_text.split(' ')
        not_morse_code = []

        for code in split_code:
            if code in inverse_morse_data:
                continue
            else:
                not_morse_code.append(code)

        if not not_morse_code:
            return input_text

        else:
            print(f'The following strings have no morse code equivalent:{not_morse_code}. '
                  f'Please re-input text to be decoded.')
            return ask_input(input_mode)



def ask_continue():
    cont = input('Would you like to continue? (Y/N) ').lower()
    if cont in ['y', 'n']:
        return cont
    else:
        print('Please enter Y or N.')
        return ask_continue()

def morse_code_encoder(chars):
    encoded_chars = ''
    for char in chars.lower():
        encoded_chars += morse_data[char] + ' '

    return encoded_chars.strip()

def morse_code_decoder(chars):
    split_chars = chars.split(' ')
    decoded_chars = ''
    for char in split_chars:
        decoded_chars += inverse_morse_data[char] + ' '

    return decoded_chars.strip()



if __name__ == '__main__':
    to_continue = 'y'

    while to_continue == 'y':
        mode = ask_mode()
        text_to_convert = ask_input(mode)

        if mode == 'e':
            if text_to_convert == '':
                print('Please input text that you want to convert to morse code.')
            else:
                print(morse_code_encoder(text_to_convert))
        elif mode == 'd':
            if text_to_convert == '':
                print('Please input text that you want to convert to morse code.')
            else:
                print(morse_code_decoder(text_to_convert))

        to_continue = ask_continue()

    print('Thank you for using my Morse Code Encoder/Decoder!')








