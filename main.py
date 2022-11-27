import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    print('\n🎥 Picking Random movie...')
    url = 'https://www.coolgenerator.com/random-movie-generator'
    page = requests.get(url)

    images = []
    steps = 0
    count = 0
    title = ''
    genre = ''
    imdb = ''

    soup = BeautifulSoup(page.content, 'html.parser')

    local = soup.find('ul', {'class': 'list-unstyled content-list'})

    for imgs in local.select('img'):
        src = 'https:' + imgs.get('src')
        images.append(src)

    for i in local.select('span'):
        if steps != 3:
            if steps == 0:
                title = i.text.replace("(", " (")
            if steps == 1:
                genre = i.text
            if steps == 2:
                imdb = i.text

        else:
            url = f'https://www.imdb.com/find?q={title.replace(" ", "+")}'
            web = requests.get(url)
            soup = BeautifulSoup(web.content, 'html.parser')

            imdblink = soup.find('a', {'class': 'ipc-metadata-list-summary-item__t'})
            url = 'https://www.imdb.com' + imdblink.attrs['href']
            web = requests.get(url)
            soup = BeautifulSoup(web.content, 'html.parser')
            imdbcheck = soup.find(
                'span', {
                    'class':
                    'sc-7ab21ed2-1 jGRxWM'
                })
            imdb = imdbcheck.text if imdbcheck else imdb
            
            print(f'Title: {title}')
            print(f'Genre: {genre}')
            print(f'IMDb: {imdb}')
            print(f'Image: {images[count]}\n')

            count = count + 1
            steps = 0

            if steps == 0:
                title = i.text.replace("(", " (")

        steps = steps + 1
    print()
