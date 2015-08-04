"""
To invoke the hive-mind representing chaos.
Invoking the feeling of chaos.
With out order.
The Nezperdian hive-mind of chaos. Zalgo.
He who Waits Behind The Wall.
ZALGO!
"""

import os
import random
import requests
from flask import Flask, request, abort
from zalgo import zalgo

URL = "https://slack.com/api"
CHAT_POST = "chat.postMessage"
INTENSITY = { "up": 5, "mid": 5, "down": 5}
IN_TOKEN = os.getenv("IN_TOKEN", "")
OUT_TOKEN = os.getenv("OUT_TOKEN", "")

app = Flask(__name__)

@app.route("/zalgify", methods=["POST"])
def zalgify():
    try:
        in_token = request.form["token"]
        channel = request.form["channel_id"]
        text = request.form["text"]
    except:
        abort(400)
    if in_token != IN_TOKEN:
        abort(401)
    zalgd = zalgo(text, INTENSITY)
    params = {
        "token": OUT_TOKEN,
        "channel": channel,
        "text": zalgd,
        "username": "zalgo",
    }
    r = requests.post("{}/{}".format(URL, CHAT_POST), data=params)
    if r.status_code != 200:
        abort(500)

    z = __doc__.split("\n")
    random.shuffle(z)
    return z[0]

if __name__ == "__main__":
    app.run()