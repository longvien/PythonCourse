# movies = {
#    'Harry Potter 2': '11:30', 
#     'Rush Hour 3': '12:10', 
#     'Home Alone 1': '12:50', 
#     'Harry Potter 6': '13:20'
# }
# print('These are the movie that we will play today.')
# 
# for movie in range(1):
#     print(movies)
# 
# movie_choice = input("Please choose one.\n")
# showtime = movies.get(movie_choice)
# 
# if showtime == None:
#     print(("The movie you entered doesn't exist. Please watch another movie!!!"))
# else:
#     print(movie_choice + ' plays at ' + showtime)
# 

movies = {'Harry Potter 2': ['11:30', 'Room 1'], 
          'Rush Hour 3': ['12:10', 'Room 2'], 
          'Home Alone 1': ['12:50', 'Room 3'], 
          'Harry Potter 6': ['13:20', 'Room 4']}
print('We are currently showing these movies:')
for movie in movies:
    print(movie)
customer_choice = input('Please choose a movie:\n')
showtime_room = movies.get(customer_choice)
if showtime_room:
    print(customer_choice, 'will be show at', showtime_room[0], 'in', showtime_room[1])
else:
    print('Invalid choice, pls choose another movie')