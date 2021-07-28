from requests import get, utils
from re import split, findall


def currency_rates(id):
    if isinstance(id, str) and id.isalpha():
        response = get('http://www.cbr.ru/scripts/XML_daily.asp')
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        content = split(r'</V', content)
        date = ''.join(findall(r'\d{2}.\d{2}.\d{4}', content[0]))
        d, m, y = date.split('.')
        date = f'{y}-{m}-{d}'  # Непонятно зачем=)
        for i in content:
            if id.upper() in i:
                i = ''.join(findall(r'\d+,\d\d', i))
                i = float(i.replace(',', '.'))  # И тут непонятно зачем=)
                return f'{i}, {date}'
    else:
        None


if __name__ == '__main__':
    print(currency_rates('eUr'))
    print(currency_rates('Usd'))
    print(currency_rates('kdfhlbgjhdf'))
    print(currency_rates(22))
