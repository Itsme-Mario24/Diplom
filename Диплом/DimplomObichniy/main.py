import traci
import sumolib
import numpy as np

#Светофор
def collect_traffic_light_data(tls_id):
    current_phase = traci.trafficlight.getPhase(tls_id)
    current_phase_duration = traci.trafficlight.getPhaseDuration(tls_id)

    lane_ids = traci.trafficlight.getControlledLanes(tls_id)
    vehicle_counts = [traci.lane.getLastStepVehicleNumber(lane) for lane in lane_ids]



def run_simulation(max_steps):
    traci.start(["sumo", "-c", "C:\\Users\\vanek\\Sumo\\2024-06-12-22-59-52\\osm.sumocfg"])

    step = 0
    while traci.simulation.getMinExpectedNumber() > 0 and step < max_steps:
        traci.simulationStep()
        data = collect_traffic_light_data("419064379")
        step += 1

    traci.close()


if __name__ == "__main__":
    # Кол-во шагов
    max_steps = 3000
    run_simulation(max_steps)
