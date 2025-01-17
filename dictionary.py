#acronyms = { 'LOL': 'laugh out loud', 'IDK': "I don't know", 'TBH': 'to be honest'}

#sentence = 'IDK' + ' what happened ' + 'TBH'
#translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

#print('sentence: ', sentence)
#print('translation: ', translation)

#acronyms = { 'LOL': 'laugh out loud', 'IDK': "I don't know", 'TBH': 'to be honest'}
#acronyms['LOL'] = 'laugh'
#print(acronyms)

acronyms = { 'LOL': 'laugh out loud', 'IDK': "I don't know", 'TBH': 'to be honest'}
key = input('Please choose a key: IDK or BSR?')
definition = acronyms.get(key)
if definition:
    print("Right! It means: ", definition)
else:
    print("The key you choose doesn't exist in this code:))))))))")