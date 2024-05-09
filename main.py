
morse_dic = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "0": "_____",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    "'": ".____.",
    "!": "_._.__",
    "/": "_.._.",
    "(": "_.__.",
    ")": "_.__._",
    "&": "._...",
    ":": "___...",
    ";": "_._._.",
    "=": "_..._",
    "+": "._._.",
    "-": "_...._",
    "_": "..__._",
    '"': "._.._.",
    "$": "..._.._",
    "@": ".__._.",
    ' ': '|'
}

flipped_dict = {value: key for key, value in morse_dic.items()}

morse_output = []
text_output = []
keep_translating = True

while keep_translating:
    choice = input("Please enter 1 for Text to Morse Code, 2 for Morse Code to Text , or 3 to Quit: ")
    text = input("Please enter what you want to translate: ")
    if choice == "2":
        for code in text.lower().split(" "):
            if code in flipped_dict:
                text_output.append(flipped_dict[code])
        print("".join(text_output))

    elif choice == "1":
        for _ in text.lower():
            if _ in morse_dic:
                morse_output.append(morse_dic[_])
        print(" ".join(morse_output))

    elif choice == "3":
        keep_translating = False
        print("Goodbye!")

    else:
        print("Sorry, that is an invalid entry. Try again.")










