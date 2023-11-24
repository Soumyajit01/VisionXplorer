from googletrans import Translator
def translateToHindi(text):
    translator = Translator()

    translated_text = translator.translate(text,dest="hi")
    return translated_text.text.strip()