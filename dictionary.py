#acronyms = { 'LOL': 'laugh out loud', 'IDK': "I don't know", 'TBH': 'to be honest'}

#sentence = 'IDK' + ' what happened ' + 'TBH'
#translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

#print('sentence: ', sentence)
#print('translation: ', translation)

#acronyms = { 'LOL': 'laugh out loud', 'IDK': "I don't know", 'TBH': 'to be honest'}
#acronyms['LOL'] = 'laugh'
#print(acronyms)

#acronyms = { 'LOL': 'laugh out loud', 'IDK': "I don't know", 'TBH': 'to be honest'}
#key = input('Please choose a key: IDK or BSR?')
#definition = acronyms.get(key)
#if definition:
#    print("Right! It means: ", definition)
#else:
#    print("The key you choose doesn't exist in this code:))))))))")

movies = {
    'Harry Potter and the Chamber of Secret': '11:30',
    'Rush Hour 3': '12:10',
    'Home Alone 1': '12:50',
    'Harry Potter and the Half Blood Prince': '13:20'
}
movies_b = input("These are the movie that we will play today. Please choose one.")
if movies_b in movies:
    print(movies_b + ' plays at ' + movies.get(movies_b))
else:
    print(("The movie you entered doesn't exist. Please watch another movie"))