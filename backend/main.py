#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/distance/<lat>/<lon>/<options>")
def root(lat, lon, options):
    return "{}, {}, {}".format(lat, lon, options)

app.run(host='0.0.0.0', port=8080)
