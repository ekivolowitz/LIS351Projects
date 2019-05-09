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
from flask import Flask, render_template, request, redirect, jsonify
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


# I surrounded every method lazily in a try / except block
# so that if an error occurs (a 500 error), it is handled by
# returning an error page. Simple, not very helpful, but gets 
# the job done. 

# The only thing I needed to consult the flask documentation on
# was handling 404 errors which I found here: http://flask.pocoo.org/docs/1.0/patterns/errorpages/

# I learned everything I needed to know about SQLITE and python here: https://docs.python.org/3/library/sqlite3.html
# and got some helpful SQL help when I had questions from here https://www.w3schools.com/sql/

#### Price Methods
@app.route("/price")
def handlePrice():
    try:
        price = EthApi.getEthPriceUSD()
        with sqlite3.connect("./app.db") as con:
            con.execute("INSERT INTO ETH_PRICE values (?, ?)", (price, datetime.date.today()))
            con.commit()
        rows = DB_Api.getDataForPriceVis()
        volume = EthApi.getTotalSupplyOfEthereum()
        marketcap = float(price) * float(volume)
        return render_template("price.html", price=price, historical=rows, volume=volume, marketcap=marketcap)
    except:
        return render_template("error.html"), 500

#### End Price

#### Searching Methods
@app.route("/search/<type>")
def handleView(type):
    try:
        if type not in ["Block", "Account", "Transaction"]:
            # returns the user to the homepage without erroring out. 
            return redirect("")
        return render_template("search.html", searchType=type)
    except:
        return render_template("error.html"), 500


@app.route("/address/<account>")
def handleAccount(account):
    try:
        accountData = EthApi.getEthForAccount(account)
        txTableData = []
        cachedFrom = []
        cachedTo = []

        # First, check if the acocunt has been entered into the database.
        # This is done to reduce redundancy. If there is an entry in the database
        # for it, it's smart to check that it's up to date, so I have a comparison
        # in there and will update if need be. 
        with sqlite3.connect("./app.db") as con:
            curr = con.cursor()
            curr.execute("SELECT Address,Balance FROM ACCOUNTS WHERE Address = (?)", (account,))
            result = curr.fetchall()
            if len(result) == 0:
                curr.execute("INSERT INTO ACCOUNTS VALUES (?, ?)", (account, accountData))
            elif len(result) == 1:
                if accountData != result[0][1]:
                    curr.execute("UPDATE ACCOUNTS SET Balance = (?) WHERE Address = (?)", (result[1], result[0]))
                    con.commit()
            else:
                print("You should not have more than one entry per account. Here is the account {}".format(account))
        
        with sqlite3.connect("./app.db") as con:
            transactions = EthApi.getTxForAccount(account)
            # iterate through the transactions per account and insert them into the database.
            for tx in transactions:
                curr = con.cursor()
                # Check the count to make sure we haven't inserted this into our db already.
                curr.execute("SELECT count(*) FROM TRANSACTIONS WHERE Hash = (?)", (tx['hash'], ))
                result = curr.fetchone()
                insert = False

                # Once a transaction is posted on the blockchain, it will never change ie it
                # is immutable. There should be no updates. 
                if result[0] == 0:
                    insert = True
                # local dictionary used to store the data that I want and add it to a list
                # that list (txTableData) is then sent to the frontend. 
                txEntry = {}
                txEntry['TransactionHash'] = tx['hash']
                txEntry['Block'] = tx['blockNumber']
                txEntry['Timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(tx['timeStamp'])))
                txEntry['From'] = tx['from']
                txEntry['To'] = tx['to']
                txEntry['Amount'] = int(tx['value']) / EthApi.WEI_ETH_CONVERSION
                txEntry['Fee'] = int(tx['gasUsed']) / EthApi.WEI_ETH_CONVERSION
                txTableData.append(txEntry)
                if insert:
                    con.execute("INSERT INTO TRANSACTIONS (Hash, Block, ts, FromAccount, ToAccount, Amount, Fee) values \
                        (?, ?, ?, ?, ?, ?, ?)", (txEntry['TransactionHash'], txEntry['Block'], txEntry['Timestamp'], txEntry['From'], txEntry['To'], txEntry['Amount'], txEntry['Fee']))
                    con.commit()
        # This searches all the transactions where the Sender matches this address, then
        # where all the transactions where the receiver matches this address.
        with sqlite3.connect("./app.db") as con:
                curr = con.cursor()
                curr.execute("SELECT * FROM TRANSACTIONS WHERE FromAccount = (?)", (account,))
                result = curr.fetchall()
                print("From account")
                if len(result) > 0:
                    for elem in result:
                        txEntry = {}
                        txEntry['TransactionHash'] = elem[0]
                        txEntry['Block'] = elem[1]
                        txEntry['Timestamp'] = elem[2]
                        txEntry['From'] = elem[3]
                        txEntry['To'] = elem[4]
                        txEntry['Amount'] = elem[5] 
                        txEntry['Fee'] = elem[6]
                        cachedFrom.append(txEntry)
                curr.execute("SELECT * FROM TRANSACTIONS WHERE ToAccount = (?)", (account,))
                result = curr.fetchall()
                if len(result) > 0:
                    for elem in result:
                        txEntry = {}
                        txEntry['TransactionHash'] = elem[0]
                        txEntry['Block'] = elem[1]
                        txEntry['Timestamp'] = elem[2]
                        txEntry['From'] = elem[3]
                        txEntry['To'] = elem[4]
                        txEntry['Amount'] = elem[5] 
                        txEntry['Fee'] = elem[6]
                        cachedTo.append(txEntry)    
        return render_template("account.html", value=accountData, transactions=txTableData, cachedFrom=cachedFrom, cachedTo=cachedTo)
    except:
        return render_template("error.html"), 500

# Simple method taking the information from a front end request for data in the Blocks page, allowing
# users to make dynamic queries. 
@app.route("/getData", methods=['POST'])
def queryStuff():
    try:
        pprint(request.form)
        f1 = "BlockNo"
        f2 = "BlockNo"
        con = request.form['con']
        op1 = request.form['op1']
        op2 = request.form['op2']
        v1 = request.form['v1']
        v2 = request.form['v2']
        with sqlite3.connect("./app.db") as conn:
            if request.form['f1'] == "Index in Block":
                f1 = "TransactionIndex"
            elif request.form['f1'] == "Amount":
                f1 = "TransactionValue"
            if request.form['f2'] == "Index in Block":
                f2 = "TransactionIndex"
            elif request.form['f2'] == "Amount":
                f2 = "TransactionValue"
            curr = conn.cursor()
            curr.execute("SELECT * FROM BLOCKS WHERE {} {} ? {} {} {} ?".format(f1, op1, con, f2, op2), (v1,v2))
            result = curr.fetchall()
            return jsonify(result)
        return "Error"
    except:
        return render_template("error.html"), 500


# This method gets information about a block by blocknumber from the api and then
# writes it into the database. 
@app.route("/block/<int:number>")
def handleBlock(number):
    try:
        blockData = EthApi.getBlockByNumber(number)
        blockTableData = {}
        miner = blockData['miner']
        hash = blockData['hash']
        gasUsed = int(blockData['gasUsed'], 0) / EthApi.WEI_ETH_CONVERSION
        transactions = {}
        for tx in blockData['transactions']:
            transactions[tx['hash']] = float.fromhex(tx['value']) / EthApi.WEI_ETH_CONVERSION

        with sqlite3.connect("./app.db") as con:
            curr = con.cursor()
            curr.execute("SELECT count(*) FROM BLOCKS WHERE BlockNo = (?)", (number, ))
            result = curr.fetchall()
            if int(result[0][0]) == 0:
                for elem in blockData['transactions']:
                    con.execute("INSERT INTO BLOCKS (BlockNo, TransactionHash, TransactionIndex, TransactionValue) values \
                        (?, ?, ?, ?)", (number, elem['hash'], float.fromhex(elem['transactionIndex']), float.fromhex(elem['value']) / EthApi.WEI_ETH_CONVERSION))
                con.commit()
            else:
                pprint(result)
        return render_template("block.html", miner=miner, hash=hash, gas=gasUsed,transactions=transactions)
    except:
        return render_template("error.html"), 500

# This function just gets transactions and sends the data to the front end.
@app.route("/transaction/<hash>")
def handleTransaction(hash):
    try:
        data = EthApi.getTransactionByHash(hash)
        receiver = data['to']
        sender = data['from']
        blockNumber = int(data['blockNumber'], 0)
        gas = int(data['gas'], 0) / EthApi.WEI_ETH_CONVERSION
        amount = int(data['value'], 0) / EthApi.WEI_ETH_CONVERSION
        return render_template("transaction.html", hash=hash, receiver=receiver, sender=sender, blockNumber=blockNumber,gas=gas, amount=amount)
    except:
        return render_template("error.html"), 500

#### End searching

@app.route("/peer")
def peer():
    return render_template('peer_review.html')

# This handles all 404 erros.
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("error.html"), 404

# This is the root path handler. 
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
