from requests import get
from bs4 import BeautifulSoup

def movie_details(input):
    input = '+'.join(input.split(' ')).lower()

    imdb_url = 'https://www.imdb.com'
    url = imdb_url + '/search/title?title=' + input + '&title_type=feature'

    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    search_results = html_soup.find_all('h3', class_ = 'lister-item-header')
    top_result = str(search_results[0])
    result_title = top_result.split('/">')[1].split('</a>')[0]
    result_date = top_result.split('unbold">')[1].split('</span>')[0]
    result_link = imdb_url + top_result.split('href="')[1].split('">')[0]

    url2 = result_link
    response2 = get(url2)
    html_soup2 = BeautifulSoup(response2.text, 'html.parser')

    text = []
    for wrapper in html_soup2.find_all('div', class_ = 'plot_summary'):
        text.append(wrapper.text)

    print('\nYour chosen film is: ', result_title, result_date)
    print((len('Your chosen film is: ' + result_title +result_date )+2)*'-', '\n')

    summary = str(text).split('Director:')[0]
    summary = summary.replace('\\n', '').replace('["', '').replace('  ','').replace("['", '')

    director = str(text).split('Director:')[1].split('Writers')[0]
    director = director.replace('\\n', '').replace('["', '').replace('  ','')
    reviews = html_soup2.find_all('div', class_ = 'ratingValue')
    score = str(reviews).split('title="')[1].split(' based on')[0]
    num_reviews = str(reviews).split('based on ')[1].split('"><')[0]

    print('Summary:\n', summary, '\n')
    print('Director:\n', director, '\n')
    print('IMDB score:\n', score, '\n')
    print('Number of User Ratings\n', num_reviews)
