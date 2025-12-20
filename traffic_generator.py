import random
from traffic_management import lane_queues, LANES

def Generate_vehicle():

    for lane in LANES:
        if random.random() < 0.4:      # 40% chance of vehicle. 
            lane_queues[lane].append("V")
