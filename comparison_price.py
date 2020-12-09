import requests
from bs4 import BeautifulSoup


def get_rakuten(keyword):
    url = f'https://search.rakuten.co.jp/search/mall/{keyword}?f=2&s=2'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.searchresultitem')

    item_number = 1
    price_list = []

    for item in items:
        title = item.select_one('.title').text
        price = item.select_one('.important').text.replace('円', '').replace(',', '')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price + '\n')
        item_number += 1

    selected_item_number = int(input('楽天：商品番号を入力してください\n'))
    selected_price = int(price_list[selected_item_number - 1])
    return selected_price


def get_yahoo(keyword):
    url = f'https://shopping.yahoo.co.jp/search?p={keyword}&X=2&ship=on'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('._2W0PXaK-syIW')

    item_number = 1
    price_list = []

    for item in items:
        title = item.select_one('._2EW-04-9Eayr').text
        price = item.select_one('._2jgEMnhQANtx').text.replace('円', '').replace(',', '')
        price_list.append(price)
        # print(item.text)
        print(item_number)
        print(title)
        print(price + '\n')
        item_number += 1

    select_item_number = int(input('Yahoo:商品番号を入力してください\n'))
    select_item = int(price_list[select_item_number - 1])
    return select_item


def comparison_price(rakuten_price, yahoo_price):
    if rakuten_price > yahoo_price:
        return f'Yahooの方が安い'
    if yahoo_price > rakuten_price:
        return f'楽天の方が安い'
    else:
        return f'同じ値段'


def main():
    keyword = input('検索ワードをよろしく：\n')

    rakuten_price = get_rakuten(keyword)
    yahoo_price = get_yahoo(keyword)
    print(f'楽天：{rakuten_price}円')
    print(f'Yahoo：{yahoo_price}円')
    print()
    print(comparison_price(rakuten_price, yahoo_price))


if __name__ == '__main__':
    main()
