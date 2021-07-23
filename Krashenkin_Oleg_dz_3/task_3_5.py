from random import choice


def get_jokes_adv(n, uniq=False):
    """
        Функция возвращает случайные шутки, собранные из трех списков слов

        :param n: колличество шуток
        :param uniq: уникальные/неуникальные
        :return: список случайных шуток

    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if uniq:
        if n < 6:
            result = []
            for i in range(0, n):
                result.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
                nouns.remove(result[i].split(' ')[0])
                adverbs.remove(result[i].split(' ')[1])
                adjectives.remove(result[i].split(' ')[2])
            return result
        else:
            return 'Максимум пять уникальных шуток'
    else:
        result = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for i in range(0, n)]
        return result


print(get_jokes_adv(5, True))
