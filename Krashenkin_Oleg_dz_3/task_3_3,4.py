def thesaurus(*args):
    name = {}
    for i in args:
        name[i[0]].append(i) if i[0] in name else name.setdefault(i[0], [i])
    return name


print(thesaurus("Иван", "Мария", "Петр", "Илья", 'Олег', 'Сергей', 'Павел', 'Игнат', 'Степан'))


def thesaurus_adv(*args):
    dict = {}
    for i in args:
        x = i.rindex(' ') + 1
        if i[x] in dict:
            if i[0] in dict[i[x]].keys():
                dict[i[x]][i[0]].append(i)
            else:
                dict.setdefault(i[x], {})
                dict[i[x]].setdefault(i[0], [i])
        else:
            dict.setdefault(i[x], {})
            dict[i[x]].setdefault(i[0], [i])
    return dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))


def thesaurus_adv_v2(*args):
    x = {}
    for i in args:
        x.setdefault(i[i.rindex(' ') + 1], {}).setdefault(i[0], []).append(i)
    return x


print(thesaurus_adv_v2("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
