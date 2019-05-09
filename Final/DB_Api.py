import sqlite3
import json
# Pretty simple function. Selects the average price per day of Ethereum (of logged data points
# in my database) and returns them in pairs sorted by their timestamp in ascending order. 
def getDataForPriceVis():
    con = sqlite3.connect("./app.db")
    cursor = con.cursor()
    data = {}
    for row in cursor.execute("SELECT timestamp, AVG(price) as price FROM ETH_PRICE GROUP BY timestamp"):
        data[str(row[0])] = row[1]
    return data