from secrets import AUTH_TOKEN
import requests
from pprint import pprint

# Found http://ethdocs.org/en/latest/ether.html
WEI_ETH_CONVERSION = 1000000000000000000

# Found how to use the requests library from the requests documentation
# https://2.python-requests.org/en/master/
# Documentation on the API is available here: https://etherscan.io/apis
def getEthPriceUSD():
    request = requests.get("https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}".format(AUTH_TOKEN))
    print(request.json()['result'])
    return request.json()['result']['ethusd']
def getTotalSupplyOfEthereum():
    request = requests.get("https://api.etherscan.io/api?module=stats&action=ethsupply&apikey={}".format(AUTH_TOKEN))
    return int(request.json()['result']) / WEI_ETH_CONVERSION
def getEthForAccount(address):
    request = requests.get("https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}".format(address, AUTH_TOKEN))
    return int(request.json()['result']) / WEI_ETH_CONVERSION
def getTxForAccount(address):
    request = requests.get("http://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}".format(address, AUTH_TOKEN))
    pprint(request.json())
    return request.json()['result']
def getBlockByNumber(number):
    request = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={}&boolean=true&apikey={}".format(hex(number), AUTH_TOKEN))
    pprint(request.json())
    return request.json()['result']
def getTransactionByHash(hash):
    request = requests.get("https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={}&apikey={}".format(hash, AUTH_TOKEN))
    pprint(request.json())
    return request.json()['result']