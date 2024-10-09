ru_to_tr = {
    ("А", "а"): ("A", "a"),
    ("Б", "б"): ("B", "b"),
    ("В", "в"): ("V", "v"),
    ("Г", "г"): ("G", "g"),
    ("Д", "д"): ("D", "d"),
    ("Е", "е"): ("Ye", "ye"),
    ("Ё", "ё"): ("Yo", "yo"),
    ("Ж", "ж"): ("J", "j"),
    ("З", "з"): ("Z", "z"),
    ("И", "и"): ("İ", "i"),
    ("Й", "й"): ("Y", "y"),
    ("К", "к"): ("K", "k"),
    ("Л", "л"): ("L", "l"),
    ("М", "м"): ("M", "m"),
    ("Н", "н"): ("N", "n"),
    ("О", "о"): ("O", "o"),
    ("П", "п"): ("P", "p"),
    ("Р", "р"): ("R", "r"),
    ("С", "с"): ("S", "s"),
    ("Т", "т"): ("T", "t"),
    ("У", "у"): ("U", "u"),
    ("Ф", "ф"): ("F", "f"),
    ("Х", "х"): ("H", "h"),
    ("Ц", "ц"): ("Ts", "ts"),
    ("Ч", "ч"): ("Ç", "ç"),
    ("Ш", "ш"): ("Ş", "ş"),
    ("Щ", "щ"): ("Şç", "şç"),
    ("Ъ", "ъ"): ("'", "'"),
    ("Ы", "ы"): ("I", "ı"),
    ("Ь", "ь"): ("\u005E", "\u005E"),
    ("Э", "э"): ("E", "e"),
    ("Ю", "ю"): ("Yu", "yu"),
    ("Я", "я"): ("Ya", "ya"),
}


tr_to_ru = {value: key for key, value in ru_to_tr.items()}


def transliterate(text: str):
    russian_chars = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    if any(char in russian_chars for char in text):
        for (ru_upper, ru_lower), (tr_upper, tr_lower) in ru_to_tr.items():
            text = text.replace(ru_upper, tr_upper).replace(ru_lower, tr_lower)
    else:
        for (tr_upper, tr_lower), (ru_upper, ru_lower) in tr_to_ru.items():
            text = text.replace(tr_upper, ru_upper).replace(tr_lower, ru_lower)

    return text


print(transliterate("На улице светит солнце, и птицы поют веселые песниь."))
print(transliterate("orospu çocuğu vakıfbank"))
