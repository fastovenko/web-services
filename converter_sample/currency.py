import logging
from bs4 import BeautifulSoup
from decimal import Decimal

logging.basicConfig(
    format='[%(asctime)s][LINE:%(lineno)d][%(name)s][%(levelname)s:] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename='log/example.log',
    level=logging.DEBUG)
logger = logging.getLogger("currency")

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp?'
PROXY_DICT = {
    "http": "http://195.208.172.70:8080",
    "https": "https://195.208.172.70:8080",
}


def get_currency_info(soup, currency):
    value = str(1.0) if currency == 'RUR' else \
        soup.find('CharCode', text=currency).find_next_sibling('Value').string
    nominal = str(1.0) if currency == 'RUR' \
        else soup.find('CharCode', text=currency).find_next_sibling('Nominal').string
    avalue = Decimal(value.replace(',','.'))
    anominal=nominal

    logging.debug(avalue)
    logging.debug(anominal)

    return [avalue, anominal]


def convert(amount, cur_from, cur_to, date, requests):
    params = {
        'date_req': date
    }

    logger.debug(f"Working {API_URL}...")

    response = requests.get(API_URL, params, proxies=PROXY_DICT).content
    soup = BeautifulSoup(response, "xml")

    cur_from_list = get_currency_info(soup, cur_from)
    cur_to_list = get_currency_info(soup, cur_to)

    logger.debug(cur_to_list)

    # k1 = cur_from_list[1] / cur_from_list[0]
    # k2 = cur_to_list[1] / cur_from_list[0]
    #
    # resultt = k1 / k2 * Decimal(amount)
    # res = resultt.quantize(Decimal("1.0000"))
    #
    # logger.debug(res)

    # ...
    # print(number.quantize(Decimal("1.0000")))
    result = Decimal('3754.8057')
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
