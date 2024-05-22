import requests
from bs4 import BeautifulSoup
import datetime


def get_xml(url: str):
    return BeautifulSoup(requests.get(url).text, 'lxml')


def formatted_time() -> str:
    return f'{datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}'


def output_to_file(info: list[str]):
    title = formatted_time()

    with open(f"{title}.txt", 'w') as file:
        for e in info:
            file.write(e + "\n")

    print(f"{len(info)} proxies saved to: '{title}.txt'")


def scrape_freeproxylist():
    info = []

    site = get_xml('https://free-proxy-list.net/')

    proxy_table = site.find_all('table', class_='table table-striped table-bordered')

    for entries in proxy_table:
        entry = entries.find_all('tr')
        for block in entry:
            data = block.find_all('td')
            if data:
                info.append(f"{data[0].text}:{data[1].text}")

                # IP PORT COUNTRYCODE COUNTRY ANONYMITY GOOGLE HTTPS LASTCHECKED
                #  0    1           2       3         4      5     6           7
                # TODO: ADD TOGGLE FUNCTIONALITY TO CHOOSE INFO

    return info


if __name__ == '__main__':
    output_to_file(scrape_freeproxylist())