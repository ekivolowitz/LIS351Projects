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
#### Begin account

#  'result': [{'blockHash': '0x4570a2e290c3d9d4f18ec64b1f3a7323c4b9d787acbfe63568ba62540999f320',
#              'blockNumber': '3868472',
#              'confirmations': '3712917',
#              'contractAddress': '',
#              'cumulativeGasUsed': '1352016',
#              'from': '0x79b47ec077b468ba1110c588b9d324c0e34d97b7',
#              'gas': '90000',
#              'gasPrice': '21000000010',
#              'gasUsed': '21000',
#              'hash': '0x647084493986c27d2bd89ff325801aa9bc64a76beedcbcae73fab71fcfbfb146',
#              'input': '0x',
#              'isError': '0',
#              'nonce': '0',
#              'timeStamp': '1497394664',
#              'to': '0x8f215bf78d61d45b0d2055dcd60e7c37651ce0ab',
#              'transactionIndex': '15',
#              'txreceipt_status': '',
#              'value': '25953280000000000'}

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
        txEntry['Fee'] = int(tx['gasUsed'])
        txTableData.append(txEntry)




    return render_template("account.html", value=accountData, transactions=txTableData)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)