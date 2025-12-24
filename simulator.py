import time
from traffic_management import (
    lane_queues,
    priority_lane_active,
    priority_should_end,
    select_lane,
    vehicles_to_move,
    release_vehicles,
    update_lights,
    LANES,
    traffic_lights,
    green_light_duration,
)
from traffic_generator import Generate_vehicle

priority_active = False
SIMULATION_STEPS = 30
last_active_lane = None  # To remember the last active lane when all are empty so as to avoid green light for empty lanes.

for step in range(SIMULATION_STEPS):
    print("\n-----------------------------")

    # Generating vehicles
    Generate_vehicle()

    # Checking priority condition
    if priority_lane_active():
        priority_active = True
    elif priority_should_end():
        priority_active = False

    # Selecting the lane
    active_lane = select_lane(priority_active, last_active_lane)

    if active_lane:

        vehicles_to_release = vehicles_to_move(active_lane)
        
        green_duration = green_light_duration(active_lane)
        
        release_vehicles(active_lane, vehicles_to_release)

        # Update lights
        update_lights(active_lane)

        for lane in LANES:
            print(f"{lane}: {len(lane_queues[lane])} vehicles -------> {traffic_lights[lane]}")

        time.sleep(green_duration)

        last_active_lane = active_lane
    

    
