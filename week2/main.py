print('Hello Mars')

import os
import errno

file_path = "/42Hoseo/week2/mission_computer_main.log"
error_file_path = "/42Hoseo/week2/error_log.txt"

try:
    # 경로가 디렉터리인지 확인
    if os.path.isdir(file_path):
        raise IsADirectoryError(errno.EISDIR, "지정된 경로가 디렉터리입니다.", file_path)
    
    # 파일 열기
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
    
    f.close()
except FileNotFoundError:
    print("Error: 파일을 찾을 수 없습니다.")
except IsADirectoryError:
    print("Error: 지정된 경로가 디렉터리입니다.")
except PermissionError:
    print("Error: 파일을 열 권한이 없습니다.")
except OSError as e:
    if e.errno == errno.ETIMEDOUT:
        print("Error: 파일을 여는 동안 시간 초과가 발생했습니다.")
    else:
        print(f"Error: {e}")
