import click
import pyfiglet
from functions import movie_recommender, movie_details

@click.group()
def main():
    banner = pyfiglet.figlet_format('py-mdb')
    print(banner)

@main.command()
def recommendations():
    query = click.prompt('Please enter a movie')
    movie_recommender(query)

@main.command()
def details():
    query = click.prompt('Please enter a movie')
    movie_details(query)

if __name__ == '__main__':
    main()
