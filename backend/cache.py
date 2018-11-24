#!/usr/bin/env python3

import json
import os
import math

class Cache(object):

    def __init__(self, file='resultcache.json'):
        try:
            with open(file) as fh:
                self._cache = json.load(fh)
        except:
            self._cache = []

    def add_result(self, lat, lon, pixels):
        self._cache.append( {
            "lat": lat,
            "lon": lon,
            "pixels": pixels
        })

    def get_result(self, lat, lon, precision=9e-6*200):
        for c in self._cache:
            dlat = lat - c["lat"]
            dlon = lon - c["lon"]
            d = math.sqrt(dlat**2 + dlon**2)

            if d < precision:
                return c

        else:
            return None
