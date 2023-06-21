import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

for page in range(31, 0,-1):
    url = f'https://dpzblog.com/category/%E9%9B%BB%E7%9A%84%E6%97%85%E7%A8%8B/page/{page}/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(response.text)
    articles = soup.find_all(class_=['post','type-post','status-publish','format-standard','hentry'])
    # print(articles)


    for article in reversed(articles):
        # title = article.find('h2', class_='entry-title').text.strip()
        # print(title)
        h3_tags = article.find('div', class_='entry-content').find_all('h3')
        for h3 in h3_tags:
            text = h3.text.split('…')[0]
            with open('output.txt', 'a', encoding='utf-8') as f:
                f.write(text + '\n')