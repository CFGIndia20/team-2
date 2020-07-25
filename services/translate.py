from googletrans import Translator


def detectLang(message):
    translator=Translator()
    return translator.detect(message)


def translateInLanguage(message, lang='en'):
    translator=Translator()
    return translator.translate(message, dest=lang)