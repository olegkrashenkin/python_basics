def num_translate_adv(numeral):
    translation = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                   'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if numeral in translation:
        return translation.get(numeral)
    elif numeral.istitle():
        return translation.get(numeral.lower()).title()
    else:
        return 'None'


print(num_translate_adv('Eight'))
