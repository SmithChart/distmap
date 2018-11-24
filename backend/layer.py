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

    def calc(self, lat, lon, count, pixlength, options):
        import math

        pixlist = []
        edge = int((count-1)/2)
        for x in range(-1*edge, edge+1):
            for y in range(-1*edge, edge+1):
                print("x: {}, y: {}".format(x,y))
                dist = math.sqrt((x*pixlength)**2+(y*pixlength)**2)
                dist *= self.multiplier
                duration = dist/self.speed
                pixlist.append((
                    x * pixlength,
                    y * pixlength,
                    duration
                ))

        return pixlist

