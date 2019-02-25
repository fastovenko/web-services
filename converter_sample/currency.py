# import logging
from decimal import Decimal

from bs4 import BeautifulSoup

# logging.basicConfig(
#     format='[%(asctime)s][LINE:%(lineno)d][%(name)s][%(levelname)s:] %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     # filename='log/example.log',
#     level=logging.DEBUG)
# logger = logging.getLogger("currency")

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp?'
PROXY_DICT = {
    "http": "http://195.208.172.70:8080",
    "https": "https://195.208.172.70:8080",
}


def get_currency_info(soup, currency):
    svalue = str(1.0) if currency == 'RUR' else \
        soup.find('CharCode', text=currency).find_next_sibling('Value').string
    snominal = str(1.0) if currency == 'RUR' \
        else soup.find('CharCode', text=currency).find_next_sibling('Nominal').string
    value = Decimal(svalue.replace(',', '.'))
    nominal = Decimal(snominal)

    return [value, nominal]


def convert(amount, cur_from, cur_to, date, requests):
    params = {
        'date_req': date
    }

    response = requests.get(API_URL, params, proxies=PROXY_DICT).content
    soup = BeautifulSoup(response, "xml")

    cur_from_list = get_currency_info(soup, cur_from)
    cur_to_list = get_currency_info(soup, cur_to)

    k1_1 = cur_from_list[1]
    k1_2 = cur_from_list[0]

    k2_1 = cur_to_list[1]
    k2_2 = cur_to_list[0]

    k1 = k1_1 / k1_2
    k2 = k2_1 / k2_2

    result = k2 / k1 * Decimal(amount)
    result = result.quantize(Decimal("1.0000"))

    # ...
    # result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой

# import requests
# http_proxy = "http://195.208.172.70:8080"
# https_proxy = "https://195.208.172.70:8080"
# response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', proxies={"http": http_proxy,"https": https_proxy,}).content
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response, 'xml')
#
# soup.find('CharCode', text='EUR').find_next_sibling('Value')
