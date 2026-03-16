
import math
from config.route_config import EXPECTED_ROUTE, ROUTE_CORRIDOR_WIDTH


EARTH_RADIUS = 6371000  # meters


def latlon_to_xy(lat, lon, ref_lat):
    """
    Convert lat/lon to local Cartesian coordinates (meters)
    using equirectangular approximation
    """

    x = math.radians(lon) * EARTH_RADIUS * math.cos(math.radians(ref_lat))
    y = math.radians(lat) * EARTH_RADIUS

    return x, y #These are meter-scale coordinates.


def distance_point_to_segment(px, py, ax, ay, bx, by):
    """
    Compute minimum distance between point P and segment AB
    """

    ABx = bx - ax
    ABy = by - ay

    APx = px - ax
    APy = py - ay

    AB_length_squared = ABx**2 + ABy**2

    if AB_length_squared == 0:
        return math.sqrt(APx**2 + APy**2)

    t = (APx * ABx + APy * ABy) / AB_length_squared

    if t < 0:
        closest_x, closest_y = ax, ay
    elif t > 1:
        closest_x, closest_y = bx, by
    else:
        closest_x = ax + t * ABx
        closest_y = ay + t * ABy

    dx = px - closest_x
    dy = py - closest_y

    return math.sqrt(dx**2 + dy**2)


def check_route_deviation(truck_lat, truck_lon):

    ref_lat = EXPECTED_ROUTE[0][0]

    px, py = latlon_to_xy(truck_lat, truck_lon, ref_lat)

    min_distance = float("inf")

    for i in range(len(EXPECTED_ROUTE) - 1):

        lat1, lon1 = EXPECTED_ROUTE[i]
        lat2, lon2 = EXPECTED_ROUTE[i + 1]

        ax, ay = latlon_to_xy(lat1, lon1, ref_lat)
        bx, by = latlon_to_xy(lat2, lon2, ref_lat)

        distance = distance_point_to_segment(px, py, ax, ay, bx, by)

        if distance < min_distance:
            min_distance = distance

    if min_distance > ROUTE_CORRIDOR_WIDTH:
        print("Distance from route:", min_distance)
        return True

    else:
        return False