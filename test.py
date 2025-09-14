menu = {
    'Breakfast': ['a', 'b', 'c'],
    'Lunch': ['d', 'e', 'f'],
    'Dinner': ['g', 'h', 'i']
}

for a, i in menu.items():
    print(a, ':', i)

menu = [
    ('Breakfast', ['a', 'b', 'c']),
    ('Lunch', ['d', 'e', 'f']),
    ('Dinner', ['g', 'h', 'i'])
]
print(menu[0][1])