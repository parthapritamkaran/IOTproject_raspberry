
previous_state = {}

ACCELERATION_THRESHOLD = 3.0   # m/s^2
HIGH_SPEED_THRESHOLD = 26.0    # m/s


def detect_fuel_anomaly(truck_id, speed, timestamp, route_deviation=False, idle=False):
    """
    Detect fuel anomaly based on:
    1. Sudden acceleration
    2. High speed
    3. Route deviation
    4. Idle status

    Returns:
        bool
    """

    fuel_alert = False

    if truck_id not in previous_state:
        previous_state[truck_id] = {
            "speed": speed,
            "timestamp": timestamp
        }

        if route_deviation or idle:
            return True
        return False

    prev_speed = previous_state[truck_id]["speed"]
    prev_time = previous_state[truck_id]["timestamp"]

    # Acceleration check
    time_diff = timestamp - prev_time
    if time_diff > 0:
        acceleration = (speed - prev_speed) / time_diff
        if acceleration > ACCELERATION_THRESHOLD:
            fuel_alert = True

    # High speed check
    if speed > HIGH_SPEED_THRESHOLD:
        fuel_alert = True

    # Route deviation check
    if route_deviation:
        fuel_alert = True

    # Idle check 
    if idle:
        fuel_alert = True

    
    previous_state[truck_id]["speed"] = speed
    previous_state[truck_id]["timestamp"] = timestamp

    return fuel_alert