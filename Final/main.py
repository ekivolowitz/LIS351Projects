######################################################################
# Project           : Final
#
# Program name      : main.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 04/10/2019
#
# Purpose           : Backend for my final project.
#
# Credit            :
#
# Use                                    Source
#
# Docstring template                     https://www.phusewiki.org/wiki/index.php?title=Program_Header
# Template creation                      https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal4/ 
#
# Revision History  :
#
# Date        Author              Ref    Revision 
# 04/10/2019  Evan Kivolowitz      1     Initial work.
#
######################################################################
from flask import Flask, render_template, request, redirect
import json
from pprint import pprint
import os
import EthApi
import sqlite3
import datetime
import DB_Api
import time
import struct 
app = Flask(__name__)


#### Price Methods
@app.route("/price")
def handlePrice():
    price = EthApi.getEthPriceUSD()
     
    with sqlite3.connect("./app.db") as con:
        con.execute("INSERT INTO ETH_PRICE values (?, ?)", (price, datetime.date.today()))
        con.commit()
    rows = DB_Api.getDataForPriceVis()
    volume = EthApi.getTotalSupplyOfEthereum()
    marketcap = float(price) * float(volume)
    return render_template("price.html", price=price, historical=rows, volume=volume, marketcap=marketcap)
#### End Price

#### Searching Methods
@app.route("/search/<type>")
def handleView(type):
    if type not in ["Block", "Account", "Transaction"]:
        return redirect("")
    return render_template("search.html", searchType=type)

@app.route("/address/<account>")
def handleAccount(account):
    accountData = EthApi.getEthForAccount(account)
    transactions = EthApi.getTxForAccount(account)

    txTableData = []
    for tx in transactions:
        txEntry = {}
        txEntry['TransactionHash'] = tx['hash']
        txEntry['Block'] = tx['blockNumber']
        txEntry['Timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(tx['timeStamp'])))
        txEntry['From'] = tx['from']
        txEntry['To'] = tx['to']
        txEntry['Amount'] = int(tx['value']) / EthApi.WEI_ETH_CONVERSION
        txEntry['Fee'] = int(tx['gasUsed']) / EthApi.WEI_ETH_CONVERSION
        txTableData.append(txEntry)
    return render_template("account.html", value=accountData, transactions=txTableData)

    
@app.route("/block/<int:number>")
def handleBlock(number):
    blockData = EthApi.getBlockByNumber(number)
    blockTableData = {}
    miner = blockData['miner']
    hash = blockData['hash']
    gasUsed = int(blockData['gasUsed'], 0) / EthApi.WEI_ETH_CONVERSION
    transactions = {}
    for tx in blockData['transactions']:
        transactions[tx['hash']] = float.fromhex(tx['value']) / EthApi.WEI_ETH_CONVERSION
    return render_template("block.html", miner=miner, hash=hash, gas=gasUsed,transactions=transactions)
@app.route("/transaction/<hash>")
def handleTransaction(hash):
    data = EthApi.getTransactionByHash(hash)
    receiver = data['to']
    sender = data['from']
    blockNumber = int(data['blockNumber'], 0)
    gas = int(data['gas'], 0) / EthApi.WEI_ETH_CONVERSION
    amount = int(data['value'], 0) / EthApi.WEI_ETH_CONVERSION
    return render_template("transaction.html", hash=hash, receiver=receiver, sender=sender, blockNumber=blockNumber,gas=gas, amount=amount)
#### End searching

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
