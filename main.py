from recommender import movie_recommender
from details import movie_details

print('Welcome to a worse version of imdb!')
print('What \'feature\' would you like to use?\n')
print('\'1\' - Movie Recommendations')
print('\'2\' - Movie Details')
print('\'Q\' - Quit')

choice = input()

if choice == '1':
    input = input('Please enter a movie you like:\n')
    movie_recommender(input=input)
elif choice == '2':
    input = input('Please enter a movie you want the details of:\n')
    movie_details(input=input)
elif choice == 'q' or choice == 'Q':
    print('Quitting...')
    pass
else:
    print('CAnt u fUcking read')
