movies = {
    'Harry Potter and the Chamber of Secret': '11:30', 
    'Rush Hour 3': '12:10', 
    'Home Alone 1': '12:50', 
    'Harry Potter and the Half Blood Prince': '13:20'
}
print('These are the movie that we will play today.')

for movie in movies:
    print(movies)

movie_choice = input("Please choose one.\n")
showtime = (movies.get(movie_choice))

if showtime == None:
    print(("The movie you entered doesn't exist. Please watch another movie!!!"))
else:
    print(movie_choice + ' plays at ' + showtime)