import random
import time
import math

EXPECTED_ROUTE = [
    (22.5726, 88.3639),
    (22.5730, 88.3645),
    (22.5735, 88.3650),
    (22.5740, 88.3660),
    (22.5745, 88.3670),
    (22.5749, 88.3678),
    (22.5753, 88.3685),
    (22.5758, 88.3691),
    (22.5764, 88.3696),
    (22.5770, 88.3700)
   
]

def meters_to_lat(m):
    return m / 111000


def meters_to_lon(m, lat):
    return m / (111000 * math.cos(math.radians(lat)))


def read_gps_data(port):

    # choose random route segment
    i = random.randint(0, len(EXPECTED_ROUTE) - 2)

    lat1, lon1 = EXPECTED_ROUTE[i]
    lat2, lon2 = EXPECTED_ROUTE[i + 1]

    # pick random point along the segment
    t = random.random()

    base_lat = lat1 + t * (lat2 - lat1)
    base_lon = lon1 + t * (lon2 - lon1)

    # direction of road
    dx = lon2 - lon1
    dy = lat2 - lat1

    # perpendicular direction
    perp_x = -dy
    perp_y = dx

    length = math.sqrt(perp_x**2 + perp_y**2)

    perp_x /= length
    perp_y /= length

    # choose distance 30–100 meters
    offset = random.uniform(30, 100)

    lat_offset = meters_to_lat(offset * perp_y)
    lon_offset = meters_to_lon(offset * perp_x, base_lat)

    lat = base_lat + lat_offset
    lon = base_lon + lon_offset

    speed = random.choice([0, 2, 5, 20, 25])
    timestamp = time.time()

    return lat, lon, speed, timestamp