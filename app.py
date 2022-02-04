#!/usr/bin/env python3
import json
import os

from flask import Flask
import requests

app = Flask(__name__)

APIKEY = 'C227WD9W3LUVKVV9'

BASEURL = 'https://www.alphavantage.co/query'
APISTR = 'apikey=' + APIKEY
FUNCSTR = 'function=TIME_SERIES_DAILY'


# handle the incoming GET on the bare URL
@app.route("/", methods=['GET'])
def stock_splat():
    """ Handle the default / URL for GET

    Build response from the stock quote service based on the example URL:
    https://www.alphavantage.co/query?apikey=C227WD9W3LUVKVV9&function=TIME_SERIES_DAILY&symbol=MSFT

    :return: JSON response converted from processed dict
    """

    # get incoming params, set some defaults
    symbol = os.getenv("SYMBOL", 'ABC')
    symstr = 'symbol=' + symbol
    days = os.getenv("NDAYS", 3)

    # call the external API to get the info, capture for returning
    req_url = BASEURL + '?' + APISTR + '&' + FUNCSTR + '&' + symstr
    resp = requests.get(req_url)

    # convert the JSON response to a dict for processing
    resp_dict = json.loads(resp.text)

    # make an iterator for the data items
    itr = iter(resp_dict['Time Series (Daily)'].items())

    # pull the latest x days off the dict into a list
    lst = [next(itr) for i in range(int(days))]

    # make a dict of the selected days results and pull the close prices into
    # list for summing
    avg = 0
    closelst = []
    newd = dict(lst)
    for k, v in newd.items():
        # print(k, v['4. close'])
        closelst.append(v['4. close'])

    # sum the close prices and get the average
    for price in closelst:
        avg += float(price)
    avg = avg/float(days)
    # print("{:.4}".format(avg))

    # Add the close average to the data
    newd['Average Closing Price: '] = avg

    # returning a dict will send JSON with flask's jsonify by default
    return newd


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)

