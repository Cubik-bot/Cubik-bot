import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import dateutil


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def make_plot(value):
    url = "http://www.finmarket.ru/currency/rates/?id=10148&pv=1&cur="
    day = datetime.date(datetime.now())
    Dict = {"dollar": "52148", "euro": "52170",
            "pound": "52146", "frank": "52133", "cron": "52132", "yena": "52246"}
    search = Dict[value]
    search += "&bd=" + str(day.day) + "&bm=" + \
        str(day.month) + "&by=" + str(day.year)
    month = dateutil.relativedelta.relativedelta(months=1)
    day = day - month
    search += "&ed=" + str(day.day) + "&em=" + \
        str(day.month) + "&ey=" + str(day.year)
    search += "&x=25&y=3#archive"
    url += search
    request = requests.get(url)

    soup = BeautifulSoup(request.text, "html.parser")

    data = soup.find("table", class_="karramba")
    data = data.find("tbody")
    data = data.findAll("tr")

    date = []
    price = []

    for point in data:
        date.append(point.findAll('td')[:-3][0].text)
        price.append(
            float((point.findAll('td')[2:-1][0].text).replace(',', '.')))

    fig, ax = plt.subplots()
    ax.plot(date, price, linewidth=0.3, marker='d', markersize=5,
            markeredgecolor='red', markerfacecolor='red', markeredgewidth=2)
    fig.set_size_inches(16, 9)

    y_labels = ax.get_yticks()
    ax.yaxis.set_major_formatter(
        ticker.FormatStrFormatter('%.2f ₽'))
    ax.fill_between(date, min(price), price, alpha=0.1)
    plt.xticks(rotation=45)
    plt.title("Exchange rate of " + value + " for the past month",
              fontfamily='serif',
              fontstyle='italic',
              fontsize=30)

    Dict2 = {"dollar": "доллара", "euro": "евро",
             "pound": "фунта стерлингов", "frank": "Швейцарского франка",
             "cron": "Шведской кроны", "yena": "Японской йены"}
    cap = "Курс " + Dict2[value] + " за прошедший месяц!\n"
    change = (price[-1] - price[0]) / price[0] * 100
    if change > 0:
        lift = 'Вырос на целых ' + str(toFixed(change, 2)) + ' процента!'
    elif change < 0:
        lift = 'Упал на целых ' + str(toFixed(-change, 2)) + ' процента!'
    else:
        lift = 'Даже не изменился!'
    cap += lift
    cap += '\n\nИнформация взята с сайта finmarket.ru'
    return fig, cap
