import os
import requests
from flask import Flask, request, abort
from zalgo import zalgo

URL = "https://slack.com/api"
CHAT_POST = "chat.postMessage"
INTENSITY = { "up": 5, "mid": 5, "down": 5}
TOKEN = os.getenv("TOKEN", "")

app = Flask(__name__)

@app.route("/zalgify", methods=["POST"])
def zalgify():
    try:
        channel = request.form["channel"]
        text = request.form["text"]
    except:
        abort(400)
    zalgd = zalgo(text, INTENSITY)
    params = {
        "token": TOKEN,
        "channel": channel,
        "text": zalgd,
    }
    r = requests.post("{}/{}".format(URL, CHAT_POST), data=params)
    if r.status_code != 200:
        abort(500)
    return zalgd

if __name__ == "__main__":
    app.run()