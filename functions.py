from requests import get
from bs4 import BeautifulSoup
import sys

def movie_search(movie_input):
    movie_input = '+'.join(movie_input.split(' ')).lower()

    imdb_url = 'https://www.imdb.com'
    url = imdb_url + '/search/title?title=' + movie_input + '&title_type=feature'

    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    search_results = html_soup.find_all('h3', class_ = 'lister-item-header')

    if len(search_results) == 0:
        print('No film found')
        sys.exit(1)

    else:
        top_result = str(search_results[0])
        result_title = top_result.split('/">')[1].split('</a>')[0]
        result_date = top_result.split('unbold">')[1].split('</span>')[0]
        result_link = imdb_url + top_result.split('href="')[1].split('">')[0]

        url2 = result_link
        response2 = get(url2)
        html_soup2 = BeautifulSoup(response2.text, 'html.parser')

        print('\nYour chosen film is: ', result_title, result_date)
        print((len('Your chosen film is: ' + result_title +result_date )+2)*'-', '\n')

        print('Is this correct?, Press 1 to continue or press anything else to quit')
        choice = input()
        if choice == '1':
            return html_soup2
            print('Film comfirmed')
        else:
            print('\nSorry about that, here are the search results which may help narrow down your search:\n')
            num_results = len(search_results)
            if num_results > 15:
                for i in range(15):
                    print(i+1, ': ', str(search_results[i]).split('/">')[1].split('</a>')[0])
            else:
                for i in range(num_results):
                    print(i+1, ': ', str(search_results[i]).split('/">')[1].split('</a>')[0])
            print('\nPlease try again')
            sys.exit()

################################################################################

def movie_details(input):

    soup = movie_search(input)

    text = []
    for wrapper in soup.find_all('div', class_ = 'plot_summary'):
        text.append(wrapper.text)

    summary = str(text).split('Director')[0]
    summary = summary.replace('\\n', '').replace('["', '').replace('  ','').replace("['", '')

    try:
        director = str(text).split('Director:')[1].split('Writer')[0]
        director = director.replace('\\n', '').replace('["', '').replace('  ','')
    except IndexError:
        director = 'Cannot Find Director'

    try:
        reviews = soup.find_all('div', class_ = 'ratingValue')
        score = str(reviews).split('title="')[1].split(' based on')[0]
        num_reviews = str(reviews).split('based on ')[1].split('"><')[0]
    except IndexError:
        score = 'Unreleased'
        num_reviews=0

    cast_table = soup.findAll('tr')

    chars =[]
    rest=[]

    for row in cast_table:
        character = row.find('td', class_='character')
        chars.append(str(character))
        restful = row.find('td')
        rest.append(str(restful))

    chars = chars[1:-2]
    rest = rest[1:-2]

    for i in range(len(chars)):
        try:
            chars[i] = chars[i].split('">')[2].split('</a>')[0]
        except IndexError:
            chars[i] = chars[i].split('">')[1].split('</a>')[0].split('</td>')[0]
            chars[i] = chars[i].strip()

    rest = [x.split('png" title="')[1].split('" width="')[0] for x in rest]
    limit = 20

    print('Cast (first billed):\n')
    for i in range(len(rest)):
        print(rest[i][:limit].rjust(limit), '|', chars[i])


    print('\nSummary:\n', summary, '\n')
    print('Director:\n', director, '\n')
    print('IMDB score:\n', score, '\n')
    print('Number of User Ratings\n', num_reviews)

################################################################################

def movie_recommender(input):

    soup = movie_search(input)

    rec_titles = soup.find_all('div', class_ = 'rec-title')
    rec_dates = soup.find_all('span', class_ ='nobr')

    rec_titles_text = []
    for x in rec_titles:
        x_str = str(x)
        rec_titles_text.append(x_str.split('<b>')[1].split('</b')[0])

    rec_dates_text = []
    for x in rec_dates:
        x_str = str(x)
        rec_dates_text.append(x_str.split('">')[1].split('</span')[0])

    if len(rec_titles_text) > 8:
        rec_titles_text = rec_titles_text [:8]
        rec_dates_text = rec_dates_text[:8]

    for i in range(len(rec_titles_text)):
        print(i+1, ': ', rec_titles_text[i], '-', rec_dates_text[i])
