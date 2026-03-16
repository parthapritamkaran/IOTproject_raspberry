
from config.route_config import IDLE_SPEED_THRESHOLD
from config.route_config import IDLE_TIME_THRESHOLD

idle_start = {}


def detect_idle(truck_id, speed, timestamp):

    current_time = timestamp

    if speed < IDLE_SPEED_THRESHOLD:

        if truck_id not in idle_start:
            idle_start[truck_id] = current_time

        idle_duration = current_time - idle_start[truck_id]

        if idle_duration >= IDLE_TIME_THRESHOLD:
            return True

    else:
        idle_start.pop(truck_id, None)

    return False