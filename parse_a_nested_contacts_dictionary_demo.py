contacts = {
    'number': 4,
    'students':
    [   
        {'name': 'Thomas Muller', 'email': 'thomasmuller@example.de'},
        {'name': 'Manuel Neuer', 'email': 'maunuelneuer@example.de'},
        {'name': 'Tony Kroos', 'email': 'tonykroos@example.de'},
        {'name': 'Kai Havert', 'email': 'kaihavert@example.de'}]
}
print('Student name & emails: ')
for student in contacts['students']:
    print(student['name'], ':', student['email'])