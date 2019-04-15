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
from flask import Flask, render_template, request
import json
from pprint import pprint
import os
import EthApi
import sqlite3
import datetime
import DB_Api
app = Flask(__name__)


@app.route("/price/data")
def getPriceData():
    return DB_Api.getDataForPriceVis()

@app.route("/price")
def price():
    price = EthApi.getEthPriceUSD()
     
    con = sqlite3.connect("./app.db")
    con.execute("INSERT INTO ETH_PRICE values (?, ?)", (price, datetime.date.today()))
    con.commit()
    con.close()
    return render_template("price.html", price=price)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)