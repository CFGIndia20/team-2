from googletrans import Translator

#Detection of language of message
def detectLang(message):
    translator=Translator()
    return translator.detect(message)

#Translating message to language stated
def translateInLanguage(message, lang='en'):
    translator=Translator()
    return translator.translate(message, dest=lang)