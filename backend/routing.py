import pyroutelib3_file as pyr
import math
import os

class Generator(object):
    """docstring for Generator."""
    def __init__(self, osm_path = '/home/stefan/Downloads/map (2)', speed = 0.833, vehicle = 'car'):
        self.name = "Generator"
        self.osm_path = osm_path
        self.router = pyr.Router(vehicle, osm_path)
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
        pixList = list()
        start = self.router.findNode(lat, lon)
        for pixel in pixels:

            end = self.router.findNode(pixel['lat'], pixel['lon'])
            status, route = self.router.doRoute(start, end) # Find the route - a list of OSM nodes
            if status == 'success':
                routeLatLons = list(map(self.router.nodeLatLon, route))
                dist = 0
                for i in range(len(routeLatLons) - 1):
                    dist += self.distanceInKmBetweenEarthCoordinates(routeLatLons[i][0], routeLatLons[i][1], routeLatLons[i+1][0], routeLatLons[i+1][1])

                duration = dist * 1000 / self.speed

                pixList.append({
                    'lat': lat,
                    'lon': lon,
                    't': duration
                })
        return pixList
