menus = {'breakfast': 'Ham, Toast, Cheese',
         'lunch': 'Fried chicken, french fries, cola',
         'dinner': 'noodles, tomato sauce, beef'}
for i in range(1):
    for name, menu in menus.items():
        print(name, ':', menu)