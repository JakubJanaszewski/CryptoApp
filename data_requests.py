from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def get_key(file: str = "key.txt"):
    with open(file) as f:
        return f.read()

def request(url: str, parameters: dict[str, str]):
    key = get_key("key.txt")
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY':key
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e

def request_data(currency: str = 'USD'):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': currency,
    }
    return url, parameters