# 파일 경로 설정
file_path = "./week2/logs/mission_computer_main.log"
json_output_path = "./week3/logs/mission_computer_main.json"

try:
    # 파일 열기 및 읽기
    with open(file_path, "rt", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Error: 비어 있는 파일입니다.")
        exit()

    # 첫 줄 헤더로 저장 / 로그 파일 형식 확인
    header = lines[0].strip().split(",")
    if header != ["timestamp", "event", "message"]:
        print("Error: 로그 파일 형식이 알려진 형식과 다릅니다.")
        exit()

    # 저장할 리스트 생성
    log_list = []

    # 로그 데이터 처리
    for line in lines[1:]:  # 헤더 제외하고 두 번째 줄부터 처리
        parts = line.strip().split(",", 2) 
        if len(parts) == 3: # 3개의 항목으로 분리되었는지 확인
            timestamp, event, message = parts # 분리된 3개의 항목을 각각에 할당
            log_list.append((timestamp.strip(), event.strip(), message.strip())) # strip으로 공백 제거 후 리스트화

    # 리스트 출력
    print("\n=== 기존 순서 ===")
    for log in log_list:
        print(log)

    # 시간의 역순으로 정렬
    log_list.sort(reverse=True, key=lambda x: x[0])

    print("\n=== 시간 역순 정렬 ===")
    for log in log_list:
        print(log)

    # 리스트를 사전 객체로 변환
    log_dict = {}
    for i, log in enumerate(log_list):
        log_dict[str(i)] = {"timestamp": log[0], "event": log[1], "message": log[2]}

    # JSON 형식으로 직접 파일 저장
    with open(json_output_path, "wt", encoding="utf-8") as json_file:
        json_file.write("{\n")
        for i, (key, value) in enumerate(log_dict.items()):
            json_file.write(f'  "{key}": {{"timestamp": "{value["timestamp"]}", "event": "{value["event"]}", "message": "{value["message"]}"}}')
            if i < len(log_dict) - 1:
                json_file.write(",\n")
            else:
                json_file.write("\n")
        json_file.write("}\n")

    print(f"\nJSON 파일 저장 완료 | 경로 : {json_output_path}")

    # 보너스 과제: 특정 문자열 검색 기능
    search_term = input("\n검색할 문자열을 입력하세요: ").strip()
    search_results = {}
    for k, v in log_dict.items():
        if search_term in v["message"]:
            search_results[k] = v

    if search_results:
        print(f"\n=== '{search_term}' 검색 결과 ===")
        for k, v in search_results.items():
            print(f"[{v['timestamp']}] | [{v['event']}] | {v['message']}")
    else:
        print(f"\n'{search_term}'에 대한 검색 결과가 없습니다.")

except FileNotFoundError:
    print(f"Error: 파일을 찾을 수 없습니다. ({file_path})")
except IsADirectoryError:
    print(f"Error: 지정된 경로가 디렉터리입니다. ({file_path})")
except PermissionError:
    print(f"Error: 파일을 열 권한이 없습니다. ({file_path})")
except Exception as e:
    print(f"Error: {e}")
