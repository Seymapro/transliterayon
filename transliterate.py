ru_to_tr = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "j",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "ts",
    "ч": "ç",
    "ш": "ş",
    "щ": "şç",
    "ъ": "",
    "ы": "ı",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}

tr_to_ru = {value: key for key, value in ru_to_tr.items()}
del tr_to_ru[""]


def transliterate_ru(text: str):
    text = text.lower()
    for ru, tr in ru_to_tr.items():
        text = text.replace(ru, tr)
    return text


def transliterate_tr(text: str):
    text = text.lower()
    for tr, ru in tr_to_ru.items():
        text = text.replace(tr, ru)
    return text


print(transliterate_ru("На улице светит солнце, и птицы поют веселые песни."))
print(transliterate_tr("orospu çocuğu vakıfbank"))
