import week7.mars_mission_computer
import time

# DummySensor 인스턴스 생성
ds = week7.mars_mission_computer.DummySensor()

# MissionComputer 클래스 정의
class MissionComputer:
    env_values = {
        "mars_base_internal_temperature": None,
        "mars_base_external_temperature": None,
        "mars_base_internal_humidity": None,
        "mars_base_external_illuminance": None,
        "mars_base_internal_co2": None,
        "mars_base_internal_oxygen": None
    }

    def get_sensor_data():
        while True:
            # 센서의 값 전체 가져오기
            envs = ds.get_env()

            # 각각 MissionComputer.env_values에 담기
            MissionComputer.env_values["mars_base_internal_temperature"] = envs["mars_base_internal_temperature"]
            MissionComputer.env_values["mars_base_external_temperature"] = envs["mars_base_external_temperature"]
            MissionComputer.env_values["mars_base_internal_humidity"] = envs["mars_base_internal_humidity"]
            MissionComputer.env_values["mars_base_external_illuminance"] = envs["mars_base_external_illuminance"]
            MissionComputer.env_values["mars_base_internal_co2"] = envs["mars_base_internal_co2"]
            MissionComputer.env_values["mars_base_internal_oxygen"] = envs["mars_base_internal_oxygen"]

            # JSON 형태로 출력
            print("{")
            keys = list(MissionComputer.env_values.keys())
            for i, key in enumerate(keys):
                value = MissionComputer.env_values[key]
                if i == len(keys) - 1:
                    print(f'  "{key}": {value}')
                else:
                    print(f'  "{key}": {value},')
            print("}")

            # 5초에 한 번씩
            time.sleep(5)

# 함수 호출
MissionComputer.get_sensor_data()
