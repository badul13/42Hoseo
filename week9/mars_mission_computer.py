import week7.mars_mission_computer
import time
import platform
import os
import psutil

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
            # 센서의 값 전체 가져오기
            envs = ds.get_env()

            # 각각 MissionComputer.env_values에 담기
            MissionComputer.env_values['mars_base_internal_temperature'] = envs['mars_base_internal_temperature']
            MissionComputer.env_values['mars_base_external_temperature'] = envs['mars_base_external_temperature']
            MissionComputer.env_values['mars_base_internal_humidity'] = envs['mars_base_internal_humidity']
            MissionComputer.env_values['mars_base_external_illuminance'] = envs['mars_base_external_illuminance']
            MissionComputer.env_values['mars_base_internal_co2'] = envs['mars_base_internal_co2']
            MissionComputer.env_values['mars_base_internal_oxygen'] = envs['mars_base_internal_oxygen']

            # JSON 형태로 출력
            print('{')
            keys = list(MissionComputer.env_values.keys())
            for i, key in enumerate(keys):
                value = MissionComputer.env_values[key]
                if i == len(keys) - 1:
                    print(f'  "{key}": {value}')
                else:
                    print(f'  "{key}": {value},')
            print('}')

            # 5초에 한 번씩
            time.sleep(5)

    def get_mission_computer_info(self):
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

    def get_mission_computer_load(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.virtual_memory().percent

            print('{')
            print(f'  "CPU Usage (%)": {cpu_usage},')
            print(f'  "Memory Usage (%)": {mem_usage}')
            print('}')

        except Exception as e:
            print(f'시스템 부하 정보를 가져오는 중 오류 발생: {e}')


# runComputer 인스턴스 생성
runComputer = MissionComputer()

# get_mission_computer_info(), get_mission_computer_load() 호출하여 시스템 정보 출력
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
