#!/usr/bin/env python3

from flask import Flask
from flask import Response
import json

app = Flask(__name__)

@app.route("/distance/<lat>/<lon>/<options>")
def root(lat, lon, options):
    r = {}
    r["center"] = {"lat":lat, "lon":lon}
    r["options"] = options
    r["pixlength"] = 10
    pixlist = []
    for x in range(-2,2):
        for y in range(-2,2):
            pixlist.append((x, y, (x+y)*1.3))
    r["pixlist"] = pixlist
    return Response(json.dumps(r), mimetype='application/json')

app.run(host='0.0.0.0', port=8080)
