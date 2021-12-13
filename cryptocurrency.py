from typing import Optional
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class Cryptocurrency:
    def __init__(self, name: Optional[str] = None, symbol: Optional[str] = None,
                  price: Optional[float] = None, volume_24h: Optional[float] = None,
                  percent_change_1h: Optional[float] = None, percent_change_24h: Optional[float] = None,
                 percent_change_7d: Optional[float] = None, percent_change_30d: Optional[float] = None):
         self.name = name
         self.symbol= symbol
         self.price = price
         self.volume_24h = volume_24h
         self.percent_change_1h = percent_change_1h
         self.percent_change_24h = percent_change_24h
         self.percent_change_7d = percent_change_7d
         self.percent_change_30d = percent_change_30d

    def __str__(self):
         return f"[{self.name}] {self.symbol} {self.price}"

def request():
     url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
     parameters = {
          'start':'1',
          'limit':'200',
          'convert':'USD'
     }
     headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': 'c1fbd94f-1e45-4652-9524-541113224366',
     }
     session = Session()
     session.headers.update(headers)
     try:
          response = session.get(url, params=parameters)
          data = json.loads(response.text)
          return data
     except (ConnectionError, Timeout, TooManyRedirects) as e:
          return e

def build_cryptocurrency():
     respose = request()
     crypto_list = list()
     for crypto in respose:
          crypto_list.append(Cryptocurrency(crypto["name"], crypto["symbol"],
                                            float(crypto["price"]), float(crypto["volume_24h"]),
                                            float(crypto["percent_change_1h"]), float(crypto["percent_change_24h"]),
                                            float(crypto["percent_change_7d"]), float(crypto["percent_change_30d"])))
     return crypto_list

print(build_cryptocurrency())






