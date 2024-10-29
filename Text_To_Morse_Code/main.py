def text_to_morse(text):

    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': ' '  # Space character
    }

    morse_text = []
    for char in text.upper():
        if char in morse_dict:
            morse_text.append(morse_dict[char])
        else:
            morse_text.append("?")

    return ' '.join(morse_text)


def morse_to_text(morse_code):

    letter_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '-..-.': '/', '-....-': '-',
        '.-.-.': '+', '.-..-.': '"', '.----.': "'", '-.-.--': '!', '---...': ':',
        '...-..-': '$', '.--.-.': '@'
    }

    words = morse_code.split(' / ')
    decoded_text = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(letter_dict.get(letter, '') for letter in letters)
        decoded_text.append(decoded_word)
    return ' '.join(decoded_text)

should_continue = True

print("Welcome to the Morse Code Converter.")

while should_continue:
    user_choice = input("If you would like to convert a message into morse code type '1'.\n"
                        "If you would like to convert morse code into text type '2'.\n"
                        "Otherwise type 'quit' to exit.\n").upper()
    if user_choice == '1':
        text = input("Please type a message to convert into morse code:\n")
        morse = text_to_morse(text)
        print(f"Morse Code: {morse}")
    elif user_choice == '2':
        morse_code = input("Please enter morse code:\n")
        text = morse_to_text(morse_code)
        print(f"Text: {text}")
    else:
        print("Thank you for using the Morse Code Converter. Goodbye!")
        should_continue = False
