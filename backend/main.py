#!/usr/bin/env python3

from flask import Flask
import json

app = Flask(__name__)

@app.route("/distance/<lat>/<lon>/<options>")
def root(lat, lon, options):
    r = {}
    r["center"] = {"lat":lat, "lon":lon}
    r["options"] = options
    r["pixlength"] = 10
    pixmap = [(x,x,x*1.3) for x in range(0, 100)]
    r["pixmap"] = pixmap
    return json.dumps(r)

app.run(host='0.0.0.0', port=8080)
