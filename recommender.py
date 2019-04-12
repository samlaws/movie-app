from requests import get
from bs4 import BeautifulSoup

def movie_recommender(input):
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
    rec_titles = html_soup2.find_all('div', class_ = 'rec-title')
    rec_dates = html_soup2.find_all('span', class_ ='nobr')


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


    print('\nYour chosen film is: ', result_title, result_date)
    print((len('Your chosen film is: ' + result_title + result_date)+1)*'-')

    for i in range(len(rec_titles_text)):
        print(i+1, ': ', rec_titles_text[i], '-', rec_dates_text[i])
