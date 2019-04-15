from secrets import AUTH_TOKEN
import requests
from pprint import pprint


def getEthPriceUSD():
    request = requests.get("https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}".format(AUTH_TOKEN))
    return request.json()['result']['ethusd']