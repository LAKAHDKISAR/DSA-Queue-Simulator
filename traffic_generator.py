import random
from traffic_management import lane_queues, LEFT_TURNING_LANES, LANES_CONTROLLED, INCOMING_LANES


vehicle_id = 0
def Generate_vehicle():
    global vehicle_id
    for lane in LANES_CONTROLLED:
        if len(lane_queues[lane]) < 10:
            num_vehicles = random.randint(0, 2)
            for i in range(num_vehicles):
                vehicle_id += 1
                lane_queues[lane].append({"id": vehicle_id, "intent": "straight"})

    for lane in LEFT_TURNING_LANES:
        if len(lane_queues[lane]) < 5 and random.random() < 0.2:
            vehicle_id += 1
            lane_queues[lane].append({"id": vehicle_id, "intent": "left"})