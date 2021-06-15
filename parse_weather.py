from bs4 import BeautifulSoup
import requests


def temperature(city):
    url = "https://yandex.ru/pogoda/"
    if city == 'moscow':
        url += city
    elif city == 'peter':
        url += '2'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    temp = soup.find("span", class_='temp__value_with-unit')
    cond = soup.find("div", class_='link__condition')
    str = temp.text + '°C, ' + cond.text + '!'
    return str + '\n\nИнформация взята с сайта yandex.ru/pogoda'
