from functions import movie_details, movie_recommender

def welcome_text():
    print('Welcome to a worse version of imdb!')
    print('What \'feature\' would you like to use?\n')
    print('\'1\' - Movie Recommendations')
    print('\'2\' - Movie Details')
    print('\'Q\' - Quit')

def continue_text():
    print('\nSelect Again')
    print('\'1\' - Movie Recommendations')
    print('\'2\' - Movie Details')
    print('\'Q\' - Quit')

def welcome(choice):

    if choice == '1':
        movie = input('Please enter a movie you like:\n')
        movie_recommender(input=movie)
        continue_text()
        welcome(choice=input())
    elif choice == '2':
        movie = input('Please enter a movie you want the details of:\n')
        movie_details(input=movie)
        continue_text()
        welcome(choice=input())
    elif choice == 'q' or choice == 'Q':
        print('Quitting...')
        pass
    else:
        print('Please select a valid option.')
        continue_text()
        welcome(choice=input())

if __name__ == '__main__':
    welcome_text()
    welcome(choice=input())
