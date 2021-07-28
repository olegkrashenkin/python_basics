from utils import currency_rates as cr
from sys import argv

name, id = argv
print(cr(id))
