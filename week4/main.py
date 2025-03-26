# Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력한다. 
# Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환한다.  
# 배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬한다.
# 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다. 
# 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장한다. 

# 인화성 순서로 정렬된 배열의 내용을 이진 파일형태로 저장한다. 파일이름은 Mars_Base_Inventory_List.bin
# 저장된 Mars_Base_Inventory_List.bin 의 내용을 다시 읽어 들여서 화면에 내용을 출력한다.
# 텍스트 파일과 이진 파일 형태의 차이점을 설명하고 장단점을 함께 설명할 수 있게 준비한다.  

# 파일 경로 설정
file_path = "./week4/logs/Mars_Base_Inventory_List.csv"
csv_output_path = "./week4/logs/Mars_Base_Inventory_danger.csv"
binary_output_path = "./week4/logs/Mars_Base_Inventory_List.bin"    

try:
    # 파일 열기
    with open(file_path, "rt", encoding="utf-8") as f:
        lines = f.readlines()

        # 기존 순서 출력
        print("\n=== 기존 순서 ===============================================")
        for line in lines:
            print(line, end='')

        # 첫 줄 헤더 확인
        header = lines[0].strip().split(",")
        if header != ["Substance", "Weight (g/cm³)", "Specific Gravity", "Strength", "Flammability"]:
            print("Error: 로그 파일 형식이 다릅니다.")
            exit()

        # 데이터 리스트 저장
        log_list = []
        for line in lines[1:]:  # 헤더 제외
            parts = line.strip().split(",", 4)
            if len(parts) == 5:
                Substance = parts[0].strip()
                Weight = parts[1].strip()
                Specific_Gravity = parts[2].strip()
                Strength = parts[3].strip()

                try:
                    Flammability = float(parts[4].strip())  # 인화성 (숫자로 변환)
                    log_list.append((Substance, Weight, Specific_Gravity, Strength, Flammability))
                except ValueError:
                    print(f"변환 오류: {parts} - 인화성 값이 숫자가 아님 (제외됨)")

        # 인화성 기준으로 정렬 (내림차순)
        log_list.sort(key=lambda x: x[4], reverse=True)

        # 인화성 지수 0.7 이상인 경우에만 출력
        print("\n=== 인화성 지수 0.7 이상 목록 ===========================")
        danger_list = [log for log in log_list if log[4] >= 0.7]
        for log in danger_list:
            print(log)

        # 인화성 지수 0.7 이상 목록 csv 파일로 저장
        with open(csv_output_path, "wt", encoding="utf-8") as f:
            f.write(",".join(header) + "\n")  # 헤더 추가
            for log in danger_list:
                f.write(",".join(map(str, log)) + "\n")

        print(f"\n인화성 지수 0.7 이상 데이터를 csv 파일 : {csv_output_path}에 저장")

        # 이진 파일로 저장
        with open(binary_output_path, "wb") as f:
            for log in log_list:
                line = ",".join(map(str, log)) + "\n"
                f.write(line.encode("utf-8"))  # 문자열을 바이트로 변환 후 저장

        print(f"인화성 순 정렬 데이터를 이진 파일 : {binary_output_path}에 저장")

        # 이진 파일 다시 읽어 출력
        print("\n=== 이진 파일에서 읽은 데이터 ===========================")
        with open(binary_output_path, "rb") as f:
            binary_content = f.readlines()
            for line in binary_content:
                print(line.decode("utf-8").strip())  # 바이트를 문자열로 변환 후 출력

except FileNotFoundError:
    print(f"Error: 파일을 찾을 수 없습니다. ({file_path})")
except IsADirectoryError:
    print(f"Error: 지정된 경로가 디렉터리입니다. ({file_path})")
except PermissionError:
    print(f"Error: 파일을 열 권한이 없습니다. ({file_path})")
except Exception as e:
    print(f"Error: {e}")
