from typing import Optional
from data_requests import *

class Cryptocurrency:
    def __init__(self, name: Optional[str] = None, symbol: Optional[str] = None, currency: Optional[str] = None,
                  price: Optional[float] = None, volume_24h: Optional[float] = None,
                  percent_change_1h: Optional[float] = None, percent_change_24h: Optional[float] = None,
                  percent_change_7d: Optional[float] = None, percent_change_30d: Optional[float] = None):
         self.name = name
         self.symbol = symbol
         self.currency = currency
         self.price = price
         self.volume_24h = volume_24h
         self.percent_change_1h = percent_change_1h
         self.percent_change_24h = percent_change_24h
         self.percent_change_7d = percent_change_7d
         self.percent_change_30d = percent_change_30d

    def __str__(self) -> str:
         return f"[{self.name}] {self.symbol} {self.currency} {self.price}"

def build_cryptocurrencies() -> list[Cryptocurrency]:
     currencies = ["USD", "EUR", "PLN"]
     crypto_list = list()
     for currency in currencies:
         url, parameters = request_data(currency)
         response = request(url, parameters)
         for crypto in response["data"]:
             crypto_list.append(Cryptocurrency(crypto["name"], crypto["symbol"], currency,
                                                float(crypto["quote"][currency]["price"]), float(crypto["quote"][currency]["volume_24h"]),
                                                float(crypto["quote"][currency]["percent_change_1h"]), float(crypto["quote"][currency]["percent_change_24h"]),
                                                float(crypto["quote"][currency]["percent_change_7d"]), float(crypto["quote"][currency]["percent_change_30d"])))
     return crypto_list

def get_cryptocurrency_name_list(cryptocurrencies: list = None) -> list[str]:
    crypto_names = list()
    for cryptocurrency in cryptocurrencies:
        if cryptocurrency.name not in crypto_names:
            crypto_names.append(cryptocurrency.name)
    return crypto_names

def get_cryptocurrency(cryptocurrencies: list = None, cryptocurrency: str = None, currency: str = "PLN") -> Cryptocurrency:
    for crypto in cryptocurrencies:
        if crypto.name == cryptocurrency and crypto.currency == currency:
            return crypto
    return Cryptocurrency()