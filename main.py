data1 = [
    {'name': '#hours', 'words': [f'{str(hour)}:{minute}' for hour in range(24) for minute in ['00', '15', '30', '45']]},
    {'name': '#before', 'words': ['before #hours']}]

data2 = [{'name': '#not', 'words': ['not']},
         {'name': '#interested', 'words': ['interested']},
         {'name': '#not_interested', 'words': ['#not #interested', 'i\'am #not_interested']}]

"""
Zadanie polega na stworzeniu funkcji, która umożliwia stworzenie iloczynu kartezjańskiego z zagnieżdżonych list,
na podstawie przygotowanych danych składających się z listy słowników w których pierwsza z wartości jest nazwą, a druga listą słów.

Dane testowe są pełne i w tych przykładach nie jest wymagana walidacja danych (czy taka lista istnieje).
Uwzględnić możliwość zagnieżdżenia tej samej listy (data2).
Trzeba pamiętać, by czas pełnego wykonania był jak najkrótszy (od import do return).

Przykład:
IN: [{'name': '#x', 'words': ['x', 'xx']}, {'name': '#y', 'words': ['y', 'yy', '#x #y']}]
OUT: [{'name': '#x', 'words': ['x', 'xx']}, {'name': '#y', 'words': ['y', 'yy', 'x y', 'x yy', 'xx y', 'xx yy']}]
"""

import itertools
from typing import Dict, List, Union


def cart_product(data: List[Dict[str, Union[str, List]]]):
    names = [x['name'] for x in data]
    words = [x['words'] for x in data]
    checked_combinations = {}
    
    for i in range(len(data)):
        expressions = words[i]
        products = []
        for expression in expressions:
            list_of_word = expression.split(" ")
            to_compute = []
            
            for word in list_of_word:
                if word in names:
                    index = names.index(word)
                    lst = [word for word in words[index] if word != expression]
                    for item in lst:
                        if item in checked_combinations.keys() and "#" in item:
                            to_compute.extend(checked_combinations[item])
                            break
                    else:
                        to_compute.append(lst)
                elif word not in names:
                    to_compute.append([word])
            
            value = [' '.join(x) for x in itertools.product(*to_compute)]
            products.extend(value)
            checked_combinations[expression] = to_compute
        data[i]['words'] = products
    return data
