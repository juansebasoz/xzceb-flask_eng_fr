from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchText= machinetranslation.english_to_french(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = machinetranslation.french_to_english(textToTranslate)
    return englishText

@app.route("/")
def renderIndexPage():
    return "Hello from translator"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

