from flask import Flask, render_template, request
import os
port = 8080
app = Flask(__name__)

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encode():
    sentence = request.form['plain_text']
    encoded = ""
    for char in sentence.upper():
        if char in MORSE_CODE_DICT:
            encoded += MORSE_CODE_DICT[char] + " "
        elif char == " ":
            encoded += "/ "
    
    return render_template("index.html", encoded=encoded)

@app.route("/decode", methods=["POST"])
def decode():
    morse_input = request.form['morse_code']
    decoded = ""
    for code in morse_input.split():
        if code in MORSE_CODE_DICT.values():
            for letter, morse in MORSE_CODE_DICT.items():
                if morse == code:
                    decoded += letter
                    break
        elif code == "/":
            decoded += " "
    
    return render_template("index.html", decoded=decoded)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
