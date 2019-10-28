import requests
from bs4 import BeautifulSoup
import json


def check_currency(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    table_content = soup.find('table')
    headers = [th.text for th in table_content.find_all("th")]
    total = []

    for tr in table_content.find_all("tr"):
        row = []
        for td in tr.find_all("td"):
            row.append(td.text.replace("\n", "").replace(",", ""))
        total.append(row)

    with open("currency/coins.csv", "w") as f:
        f.write(",".join(headers[:len(headers)-2]))
        for coin in total[1:]:
            f.write("\n")
            f.write(",".join(coin[:len(coin)-2]))

    with open("currency/ccur.json", "w") as f2:
        jresult = []
        for coin in total[1:]:
            jresult.append({key: data for key, data in
                            zip(headers[:len(headers) - 2], coin)})
            f2.write(json.dumps(jresult, indent=2))

    print(json.dumps(jresult, indent=2))


check_currency("https://coinmarketcap.com/")
