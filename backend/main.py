#!/usr/bin/env python3

from flask import Flask
from flask import Response
from flask_cors import CORS, cross_origin
app = Flask(__name__)

import json

import layer
import cache


generator = layer.DummyGenerator()

c = cache.Cache()

@app.route("/distance/<lat>/<lon>")
@cross_origin()
def root(lat, lon, options=None):
    lat = float(lat)
    lon = float(lon)

    cache_result = c.get_result(lat, lon)
    if cache_result is None:
        # for now we assume to have a view port of 2x2km²
        # also we assume to have 11x11 pixels
        count = 11

        # 1m ~ 9e-6°
        offset = 9e-6 * 200

        # generate output pixels
        pixels= []
        for dlat in range(-4,5):
            for dlon in range(-4, 5):
                pixels.append({
                    "lat": lat+dlat*offset,
                    "lon": lon+dlon*offset
                })

        result = (generator.name, generator.calc(lat, lon, pixels))
        c.add_result(lat, lon, result)
    else:
        result = cache_result

    # create return value
    r = {}
    r["center"] = {"lat":lat, "lon":lon}
    r["pixlist"] = result[1]
    return Response(json.dumps(r), mimetype='application/json')

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()
