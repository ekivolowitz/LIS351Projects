import sqlite3
import json

def getDataForPriceVis():
    con = sqlite3.connect("./app.db")
    cursor = con.cursor()
    data = {}
    for row in cursor.execute("SELECT timestamp, AVG(price) as price FROM ETH_PRICE GROUP BY timestamp"):
        data[str(row[0])] = row[1]
    return json.dumps(data)