from bs4 import BeautifulSoup
import requests


def temperature(city):
    url = "https://weather.com/ru-RU/weather/today/l/"
    if city == "moscow":
        url += "34f2aafc84cff75ae0b014754856ea5e7f8ddf618cf9735549dfb5e016c28e10"
    elif city == "peter":
        url += "4edb4827c7f66b1542f84ce1d8d644970e9b935d45d21d4d143e87d94925a4bf"

    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    temp = soup.find("span", class_='CurrentConditions--tempValue--MHmYY')
    extra = soup.find("div", class_='CurrentConditions--phraseValue--mZC_p')
    return temp.text + 'C, ' + extra.text + '!\n\nИнформация взята с сайта weather.com'
