

import serial
from datetime import datetime

KNOT_TO_MPS = 0.514444


def convert_to_degrees(raw_value, direction):
    """
    Convert NMEA lat/long format (DDMM.MMMM) to decimal degrees
    """

    if raw_value == "":
        return None

    value = float(raw_value)

    degrees = int(value / 100)
    minutes = value - (degrees * 100)

    decimal = degrees + minutes / 60

    if direction in ['S', 'W']:
        decimal = -decimal

    return decimal


def parse_gprmc(sentence):
    """
    Parse GPRMC sentence
    """

    parts = sentence.split(",")

    if parts[2] != "A":
        return None

    timestamp_raw = parts[1]
    lat_raw = parts[3]
    lat_dir = parts[4]

    lon_raw = parts[5]
    lon_dir = parts[6]

    speed_knots = parts[7]

    latitude = convert_to_degrees(lat_raw, lat_dir)
    longitude = convert_to_degrees(lon_raw, lon_dir)

    speed_mps = float(speed_knots) * KNOT_TO_MPS if speed_knots != "" else 0

    timestamp = datetime.utcnow().isoformat()

    return latitude, longitude, speed_mps, timestamp


def read_gps_data(port):

    ser = serial.Serial(port, 9600, timeout=1)

    while True:

        line = ser.readline().decode("utf-8", errors="ignore")

        if line.startswith("$GPRMC"):

            result = parse_gprmc(line)

            if result:
                return result