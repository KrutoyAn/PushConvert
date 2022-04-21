import requests
from bs4 import BeautifulSoup
import time


class Currency():


    DOLLAR_CZK = 'https://www.google.com/search?q=доллар+к+крона&sxsrf=APq-WBs-mMLkcpeqvdKgvrfNBxhfxEgjSQ%3A1650569465583&ei=-bBhYpidI5makgXH75uYCg&ved=0ahUKEwjY_bC18qX3AhUZjaQKHcf3BqMQ4dUDCA4&uact=5&oq=доллар+к+крона&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQsAMQJzoHCAAQRxCwAzoKCAAQRxCwAxDJAzoHCAAQsAMQQzoECAAQDToHCCMQsAIQJzoHCAAQyQMQDToJCAAQyQMQFhAeOgYIABANEAo6CAgAEAgQDRAeOgkIIRAKEKABECo6BwghEAoQoAE6BQghEKABOgkIIxAnEEYQggI6CggAEIAEEIcCEBQ6CAgAEIAEEMkDOg8IABCABBCHAhAUEEYQggI6BQgAEMsBOgcIABCABBAKOgoIABCABBBGEIICSgQIQRgASgQIRhgAUNoIWK8vYPEwaAdwAXgAgAFhiAG3B5IBAjE0mAEAoAEByAEKwAEB&sclient=gws-wiz'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 Safari/537.36'}

    current_converted_price = 0
    difference = 5
    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_CZK, headers=self.headers)

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