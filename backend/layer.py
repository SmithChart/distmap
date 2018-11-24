#!/usr/bin/env python3


class DummyGenerator(object):
    """
    This generator takes the distance between the center and every pixel
    multiplies this length with a factor and
    adds a speed.
    """

    # name of this generator for output
    name = "DummyCircularGenerator"

    # length multiplier
    multiplier = 1.3

    # speed in m/s
    speed = 0.833

    # deg to len factor: [°/m]
    dtlf = 9e-6

    def calc(self, lat, lon, pixels):
        """
        Arguments:
        * lat, lon: Startpunkt
        * pixels: Liste von Endpunkten
        """
        import math

        result = []

        for p in pixels:
            dlat = lat-p["lat"]/self.dtlf
            dlon = lon-p["lon"]/self.dtlf
            d = math.sqrt(dlat**2 + dlon**2)*self.multiplier
            duration = d / self.speed

            result.append({
                "lat": p["lat"],
                "lon": p["lon"],
                "t": duration
            })

        return result

