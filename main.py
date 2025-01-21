from flask import Flask, jsonify, send_file, Blueprint, request,abort
from flask_cors import CORS
import os
import lyrics

app = Flask(__name__)
CORS(app)

wsgi_app = app.wsgi_app

@app.route("/request-lyrics/<song_details>")
def request_lyrics(song_details):
    lyrics_text = lyrics.get_ytm_lyrics(song_details)
    if lyrics_text is None:
        return "no_lyrics_found"
    return lyrics_text


@app.route("/privacy")
def privacy():
    return open("privacypolicy.html")

@app.route("/assets/logo")
def logo():
    return send_file("static/128x128.png", mimetype="image/gif")


if __name__ == "__main__":
    app.run(debug=True, port=7070)

