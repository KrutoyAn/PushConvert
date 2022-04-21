import requests
from bs4 import BeautifulSoup
import time


class Currency():


    DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APq-WBtnTG_o9daJFnDruFDzbClYWZW2KQ%3A1650567909482&source=hp&ei=5aphYt6zGqiPxc8PoZ6ymA8&iflsig=AHkkrS4AAAAAYmG49Xdn3nGVeAXSaGgYajTjwLJ82koL&oq=%D0%B4%D0%BE%D0%BB%D0%BB&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoFCC4QgARQiARY7gdgtQ5oAXAAeACAATaIAckBkgEBNJgBAKABAbABBw&sclient=gws-wiz'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 Safari/537.36'}

    current_converted_price = 0
    difference = 5
    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("+ is  APP ")
        elif currency <= self.current_converted_price - self.difference:
            print("- is low")
        print("Now currency is : " + str(currency))
        time.sleep(3)
        self.check_currency()


currency = Currency()
currency.check_currency()