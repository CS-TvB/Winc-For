from itertools import count
from helpers import get_countries
from collections import Counter

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"

""" Write your functions here. """
# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

def shortest_names(countries):
    for i in countries:
        shortest_str = []
        if i in countries:
            shortest_str.append(min(countries, key = len))
    print (shortest_str)
    return (shortest_str)

def most_vowels(countries, empty_count, k = 3):
    klink = ['a', 'e', 'i', 'o', 'u']
    empty_count = []
    for c in countries:
        for i in c:
            while i in klink:
                empty_count.append(c)
                break
    c = Counter(empty_count)
    most_common = [key for key, val in c.most_common(k)]
    print (most_common)

def alphabet_set(countries):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_alpha = []
    for z in countries:
        for x in z:
            x = (x.lower())
            if x in alpha[:]:
                alpha.remove(x)
                new_alpha.append(z)
                new_alpha = list(dict.fromkeys(new_alpha))
                if alpha == []:
                    print(new_alpha)

""" Write the calls to your functions here. """
shortest_names(countries)
most_vowels(countries, empty_count = [])
alphabet_set(countries)