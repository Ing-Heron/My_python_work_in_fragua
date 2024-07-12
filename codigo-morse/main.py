abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z", " "]
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.",
         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]


def textToMorse(text: str) -> str:
    morse_code = ""
    for letter in text:
        morse_code += morse[abc.index(letter)]
        morse_code += " "
    return morse_code


def morseToText(text: str) -> str:
    text_code = ""
    letter = text.split(" ")
    for code in letter:
        text_code += abc[morse.index(code)]
    return text_code


print(len(abc))
print(len(morse))
is_morse = input("Do you want to convert natural text to morse (T) "
                 "or you want to convert morse to natural text (M): ").upper()
if is_morse == "T":
    morse_text = textToMorse(input("input your text that you want to convert to morse: ").lower())
    print(morse_text)
elif is_morse == "M":
    text_morse = morseToText(input("input your morse text that you want to convert to text: "))
    print(text_morse)
else:
    print("You enter wrong option")
