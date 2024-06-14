import traci
import sumolib
import numpy as np


def intelligent_traffic_light(tls_id):
    current_phase = traci.trafficlight.getPhase(tls_id)
    current_phase_duration = traci.trafficlight.getPhaseDuration(tls_id)

    # Получаем данные о пробках
    lane_ids = traci.trafficlight.getControlledLanes(tls_id)
    vehicle_counts = [traci.lane.getLastStepVehicleNumber(lane) for lane in lane_ids]

    # Получаем данные о задержке на полосах
    lane_delays = [traci.lane.getWaitingTime(lane) for lane in lane_ids]

    # Прогнозирование на основе исторических данных и текущих условий (улучшенная модель)
    avg_vehicle_count = np.mean(vehicle_counts)
    max_vehicle_count = np.max(vehicle_counts)
    avg_delay = np.mean(lane_delays)
    max_delay = np.max(lane_delays)

    # Определяем логику управления фазами
    if max_vehicle_count > 20 or max_delay > 30:  # Если на какой-то полосе много машин или высокая задержка
        traci.trafficlight.setPhaseDuration(tls_id, current_phase_duration + 15)
    elif avg_vehicle_count < 5 and avg_delay < 10:  # Если машин мало и задержка низкая
        traci.trafficlight.setPhaseDuration(tls_id, max(10, current_phase_duration - 5))
    else:
        traci.trafficlight.setPhaseDuration(tls_id, current_phase_duration)


def run_simulation(steps):
    traci.start(["sumo", "-c", "C:\\Users\\vanek\\Sumo\\2024-06-12-22-59-52\\osm.sumocfg"])
    step = 0
    while step < steps:
        traci.simulationStep()
        intelligent_traffic_light("419064379")
        step += 1
    traci.close()


if __name__ == "__main__":
    # Задаем количество шагов для симуляции
    steps = 3000
    run_simulation(steps)
