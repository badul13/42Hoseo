import week7.mars_mission_computer
import time
import platform
import os
import psutil
import threading
import multiprocessing


# DummySensor 인스턴스 생성
ds = week7.mars_mission_computer.DummySensor()

class MissionComputer:
    env_values = {
        'mars_base_internal_temperature': None,
        'mars_base_external_temperature': None,
        'mars_base_internal_humidity': None,
        'mars_base_external_illuminance': None,
        'mars_base_internal_co2': None,
        'mars_base_internal_oxygen': None
    }

    def get_sensor_data(self):
        while True:
            envs = ds.get_env()

            MissionComputer.env_values['mars_base_internal_temperature'] = envs['mars_base_internal_temperature']
            MissionComputer.env_values['mars_base_external_temperature'] = envs['mars_base_external_temperature']
            MissionComputer.env_values['mars_base_internal_humidity'] = envs['mars_base_internal_humidity']
            MissionComputer.env_values['mars_base_external_illuminance'] = envs['mars_base_external_illuminance']
            MissionComputer.env_values['mars_base_internal_co2'] = envs['mars_base_internal_co2']
            MissionComputer.env_values['mars_base_internal_oxygen'] = envs['mars_base_internal_oxygen']

            print('{')
            keys = list(MissionComputer.env_values.keys())
            for i, key in enumerate(keys):
                value = MissionComputer.env_values[key]
                if i == len(keys) - 1:
                    print(f'  "{key}": {value}')
                else:
                    print(f'  "{key}": {value},')
            print('}')

            time.sleep(5)

    def get_mission_computer_info(self):
        while True:
            try:
                os_name = platform.system()
                os_version = platform.version()
                cpu_type = platform.processor()
                cpu_cores = os.cpu_count()
                mem_bytes = psutil.virtual_memory().total
                mem_gb = round(mem_bytes / (1024 ** 3), 2)

                print('{')
                print(f'  "OS": "{os_name}",')
                print(f'  "OS Version": "{os_version}",')
                print(f'  "CPU Type": "{cpu_type}",')
                print(f'  "CPU Cores": {cpu_cores},')
                print(f'  "Memory Size (GB)": {mem_gb}')
                print('}')

            except Exception as e:
                print(f'시스템 정보를 가져오는 중 오류 발생: {e}')

            # 20초로 수정
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                mem_usage = psutil.virtual_memory().percent

                print('{')
                print(f'  "CPU Usage (%)": {cpu_usage},')
                print(f'  "Memory Usage (%)": {mem_usage}')
                print('}')

            except Exception as e:
                print(f'시스템 부하 정보를 가져오는 중 오류 발생: {e}')

            # 20초로 수정
            time.sleep(20)


# 멀티스레드로 실행하게 설정
def run_threads(computer):
    t1 = threading.Thread(target=computer.get_mission_computer_info)
    t2 = threading.Thread(target=computer.get_mission_computer_load)
    t3 = threading.Thread(target=computer.get_sensor_data)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


# 멀티프로세스로 실행하게 설정
def run_process(computer):
    p1 = multiprocessing.Process(target=computer.get_mission_computer_info)
    p2 = multiprocessing.Process(target=computer.get_mission_computer_load)
    p3 = multiprocessing.Process(target=computer.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    # runComputer 인스턴스 멀티 스레드 실행
    run_computer = MissionComputer()
    thread_runner = threading.Thread(target=run_threads, args=(run_computer,))
    thread_runner.start()

    # Step 2: runComputer1, 2, 3 인스턴스 생성
    run_computer1 = MissionComputer()
    run_computer2 = MissionComputer()
    run_computer3 = MissionComputer()

    # 멀티프로세스 실행
    p1 = multiprocessing.Process(target=run_process, args=(run_computer1,))
    p2 = multiprocessing.Process(target=run_process, args=(run_computer2,))
    p3 = multiprocessing.Process(target=run_process, args=(run_computer3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
