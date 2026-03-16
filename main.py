
import time
#from gps.gps_reader import read_gps_data
from gps.simulator import read_gps_data
from processing.route_deviation import check_route_deviation
from processing.idle_detection import detect_idle
from processing.fuel_anomaly import detect_fuel_anomaly
from communication.send_to_server import send_data


GPS_DEVICES = {
    "TRUCK_1": "/dev/ttyUSB0",
    "TRUCK_2": "/dev/ttyUSB1"
}


def process_truck(truck_id, port):

    lat, lon, speed, timestamp = read_gps_data(port)

    deviation = check_route_deviation(lat, lon)

    idle = detect_idle(truck_id, speed, timestamp)

    fuel_alert = detect_fuel_anomaly(truck_id, speed, timestamp, deviation, idle)

    payload = {
        "truck_id": truck_id,
        "latitude": lat,
        "longitude": lon,
        "speed": speed,
        "timestamp": timestamp,
        "route_deviation": deviation,
        "idle": idle,
        "fuel_alert": fuel_alert
    }

    send_data(payload)
    print(payload)


def main():

    i=0
    while i<10:

        for truck_id, port in GPS_DEVICES.items():

            process_truck(truck_id, port)

        time.sleep(5)
        i+=1


if __name__ == "__main__":
    main()