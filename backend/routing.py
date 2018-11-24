import pyroutelib3_file as pyr
import math
import numpy as np
import os

class Generator(object):
    """docstring for Generator."""
    def __init__(self, osm_path = '/home/stefan/Downloads/map (2)', speed = 0.833, vehicle = 'car'):
        self.name = "Generator"
        self.osm_path = osm_path
        self.router = pyr.Router(vehicle)#, osm_path)
        self.speed = speed

    def distanceInKmBetweenEarthCoordinates(self, lat1, lon1, lat2, lon2):
        def degreesToRadians(degrees):
          return degrees * math.pi / 180

        earthRadiusKm = 6371

        dLat = degreesToRadians(lat2-lat1)
        dLon = degreesToRadians(lon2-lon1)

        lat1 = degreesToRadians(lat1)
        lat2 = degreesToRadians(lat2)

        a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return earthRadiusKm * c

    def calc(self,lat, lon, pixels):
        skipped = 0
        pixList = list()
        start = self.router.findNode(lat, lon)
        for pixel in pixels:
            print('')
            print("{}, {}".format(lat, lon))
            print("{}, {}".format(pixel['lat'], pixel['lon']))

            end = self.router.findNode(pixel['lat'], pixel['lon'])
            status, route = self.router.doRoute(start, end) # Find the route - a list of OSM nodes
            if status == 'success':
                routeLatLons = list(map(self.router.nodeLatLon, route))
                dist = 0
                for i in range(len(routeLatLons) - 1):
                    dist += self.distanceInKmBetweenEarthCoordinates(routeLatLons[i][0], routeLatLons[i][1], routeLatLons[i+1][0], routeLatLons[i+1][1])

                duration = dist * 1000 / self.speed

                pixList.append({
                    'lat': pixel['lat'],
                    'lon': pixel['lon'],
                    't': duration
                })
            else:
                skipped += 1
        if skipped > 0:
            print("Skipped {} points while routing.".format(skipped))


        # sort by angle
        list_to_sort = list()
        for pix in pixList:
            dot_product = pix['lat'] * lat + pix['lon'] * lon
            len_p1 = math.sqrt(pix['lat']**2 + pix['lon']**2)
            len_p2 = math.sqrt(lat**2 + lon**2)
            list_to_sort.append((pix['lat'], pix['lon'], pix['t'],math.acos(dot_product / (len_p1 * len_p2))))

        dtype = [('lat', float), ('lon', float), ('t', float), ('angle', float)]
        array_to_sort = np.array(list_to_sort, dtype)
        array_to_sort.sort(order=['lat', 'lon'])

        print(array_to_sort)

        list_to_return = list()
        for tuple in array_to_sort:
            list_to_return.append({tuple[0], tuple[1], tuple[2]})


        return list_to_return
        #return pixList

#
gen = Generator()
print(gen.calc(52.268725, 10.510546, [{'lat': 52.267041, 'lon': 10.514387}, {'lat':52, 'lon': 10}]))
