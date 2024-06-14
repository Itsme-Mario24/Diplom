import traci
import sumolib

def adapt_traffic_light(tls_id):
    # Получаем информацию о светофоре
    current_phase = traci.trafficlight.getPhase(tls_id)
    current_phase_duration = traci.trafficlight.getPhaseDuration(tls_id)

    # Получаем количество автомобилей на подъездах к перекрестку
    lane_ids = traci.trafficlight.getControlledLanes(tls_id)
    vehicle_counts = [traci.lane.getLastStepVehicleNumber(lane) for lane in lane_ids]

    # Логика изменения фаз светофора на основе количества автомобилей
    if sum(vehicle_counts) > 10:  # Простая логика: если больше 10 автомобилей, увеличиваем зеленую фазу
        traci.trafficlight.setPhaseDuration(tls_id, current_phase_duration + 5)
    else:
        traci.trafficlight.setPhaseDuration(tls_id, max(10, current_phase_duration - 1))

def run_simulation():
    # Запуск симуляции
    traci.start(["sumo", "-c", "C:\\Users\\vanek\\Sumo\\2024-06-12-22-59-52\\osm.sumocfg"])
    step = 0
    while step < 1000:
        traci.simulationStep()
        adapt_traffic_light("419064379")
        step += 1
    traci.close()

if __name__ == "__main__":
    run_simulation()