print('Hello Mars')

# 파일 경로 설정
file_path = "./week2/logs/mission_computer_main.log"
error_file_path = "./week2/logs/error_log.txt"

try:
    # 파일 열기 (디렉터리인지 확인 - open())
    with open(file_path, "rt", encoding="utf-8") as f:
        lines = f.readlines()
        
        # 기존 순서대로 출력
        print("\n=== 기존 순서 ===")
        for line in lines:
            print(line, end='')
        
        # 시간의 역순으로 정렬하여 출력
        print("\n=== 시간 역순 ===")
        for line in reversed(lines):
            print(line, end='')
        
        # 오류 로그 저장 - explosion 검출
        error_lines = [line for line in lines if "explosion" in line]
        if error_lines:
            with open(error_file_path, "wt", encoding="utf-8") as error_file:
                error_file.writelines(error_lines)

except FileNotFoundError:
    print(f"Error: 파일을 찾을 수 없습니다. ({file_path})")
except IsADirectoryError:
    print(f"Error: 지정된 경로가 디렉터리입니다. ({file_path})")
except PermissionError:
    print(f"Error: 파일을 열 권한이 없습니다. ({file_path})")
except Exception as e:
    print(f"Error: {e}")
