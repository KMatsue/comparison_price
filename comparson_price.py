import requests
from bs4 import BeautifulSoup


def get_rakuten(keyword):
    url = f'https://search.rakuten.co.jp/search/mall/{keyword}?f=2&s=2'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.searchresultitem')

    item_number = 1  #
    price_list = []

    for item in items:
        title = item.select_one('.title').text
        price = item.select_one('.important').text
        price_list.append(price)
        print(item_number)
        print(title)
        print(price + '\n')
        item_number += 1

    selected_item_number = int(input('楽天：商品番号を入力してください\n'))
    selected_price = price_list[selected_item_number - 1]
    # print(selected_price)
    return selected_price

def main():
    keyword = input('検索ワードをよろしく：\n')
    # print(get_rakuten(keyword))
    rakuten_price = get_rakuten(keyword)
    print(rakuten_price)


if __name__ == '__main__':
    main()
# pythonチュートリアル
