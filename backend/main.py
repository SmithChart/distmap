#!/usr/bin/env python3

from flask import Flask
from flask import Response
from flask_cors import CORS, cross_origin
app = Flask(__name__)

import json

import layer


generators = []
generators.append(layer.DummyGenerator())

@app.route("/distance/<lat>/<lon>")
@cross_origin()
def root(lat, lon, options=None):
    lat = float(lat)
    lon = float(lon)

    # for now we assume to have a view port of 2x2km²
    # also we assume to have 11x11 pixels
    count = 11
    # this creates a pixel-size of:
    pixlength = 2000/10
    # run all generators and get travel times
    results = []

    for g in generators:
        results.append((g.name, g.calc(lat, lon, count, pixlength, options)))

    # create return value
    r = {}
    r["center"] = {"lat":lat, "lon":lon}
    r["options"] = options
    r["pixlength"] = pixlength
    r["pixlist"] = results[0][1]
    return Response(json.dumps(r), mimetype='application/json')

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()
