# 전역 변수 설정
material = ''
diameter = 0
thickness = 0
area = 0.0
weight = 0.0

def sphere_area(diameter_input, material_input='유리', thickness_input=1):
    global material, diameter, thickness, area, weight

    densities = {
        '유리': 2.4,
        '알루미늄': 2.7,
        '탄소강': 7.85
    }

    # 전역 변수에 저장
    material = material_input
    diameter = diameter_input
    thickness = thickness_input

    # 면적
    radius = diameter / 2
    area = 2 * 3.14 * (radius ** 2)  # 반구 면적 2파이r^2
    area = area * 10000  # 단위 m에서 cm로 변경

    # 무게 (부피 > 질량 > 무게)
    volume = area * thickness
    mass = densities[material] * volume
    mass = mass / 1000 # 단위 g에서 kg으로 변경
    weight_on_mars = mass * 0.38  # 화성 중력 반영

    area = round(area, 3)
    weight = round(weight_on_mars, 3)

    return area, weight


def main():
    while True:
        # 재질 입력
        while True:
            material_input = input('재질을 입력하세요 [종류 : 유리, 알루미늄, 탄소강] >> ')
            if material_input in ['유리', '알루미늄', '탄소강']:
                break
            print('지정된 재질의 종류가 아닙니다. 다시 입력하세요.')

        # 지름 입력
        diameter_str = input('돔의 지름을 입력하세요 (단위: m): ')
        try:
            diameter_input = float(diameter_str)
            if diameter_input <= 0:
                print('지름은 0보다 커야 합니다.')
                continue
        except ValueError:
            print('지름은 숫자로 입력해야 합니다.')
            continue

        # 두께 입력
        thickness_str = input('두께를 입력하세요 (단위: cm) [기본: 1]: ')
        try:
            thickness_input = float(thickness_str)
        except ValueError:
            print('두께는 숫자로 입력해야 합니다.')
            continue

        sphere_area(diameter_input, material_input, thickness_input)

        print(f'재질 =⇒ {material}, 지름 =⇒ {diameter}, 두께 =⇒ {thickness}, 면적 =⇒ {area}, 무게 =⇒ {weight} kg')

        again = input('다시 계산하시겠습니까? (y/n): ')
        if again.lower() != 'y':
            print('프로그램을 종료합니다.')
            break


if __name__ == '__main__':
    main()
