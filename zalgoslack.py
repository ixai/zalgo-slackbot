from flask import Flask, request, abort
from zalgo import zalgo
from config import TOKEN, INTENSITY
import requests

URL = "https://slack.com/api"
CHAT_POST = "chat.postMessage"

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