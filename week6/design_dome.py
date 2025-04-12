# numpy 임포트
import numpy as np

try:
    # CSV 파일을 numpy로 가져오기
    arr1 = np.loadtxt(fname='./week6/csv/mars_base_main_parts-001.csv', delimiter=',', skiprows=1, dtype=str)
    arr2 = np.loadtxt(fname='./week6/csv/mars_base_main_parts-002.csv', delimiter=',', skiprows=1, dtype=str)
    arr3 = np.loadtxt(fname='./week6/csv/mars_base_main_parts-003.csv', delimiter=',', skiprows=1, dtype=str)

    # 셋을 하나로 합치기
    parts = np.vstack((arr1, arr2, arr3))

    # 각 항목의 평균값 구하기
    means = parts[:, 1].astype(float)

    # 평균값이 50보다 작은 항목만 추출
    filtered_parts = parts[means < 50]

    # 필터링된 데이터를 CSV파일로 저장
    file_path = 'parts_to_work_on.csv'
    with open(file_path, 'wt') as f:
        for row in filtered_parts:
            line = ','.join(row)
            f.write(line + '\n')

except FileNotFoundError as e:
    print('Error: 파일을 찾을 수 없습니다.')
except IsADirectoryError as e:
    print('Error: 지정된 경로가 디렉터리입니다.')
except PermissionError as e:
    print('Error: 파일을 열 권한이 없습니다.')
except Exception as e:
    print(f'Error: {e}')
