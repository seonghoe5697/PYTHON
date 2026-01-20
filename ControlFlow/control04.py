'''
도형 면적 계산기
'''
print('1:사각형 2:삼각형 3:원')
opt = int(input('면적을 계산할 도형 번호: '))
match opt:
  case 1:
    width = int(input('가로 입력: '))
    height = int(input('세로 입력: '))
    area = width * height
    print(f'사각형의 넓이는 {area} 입니다.')
  case 2:
    base = int(input('밑변 입력: '))
    height = int(input('높이 입력: '))
    area = base * height
    print(f'삼각형의 넓이는 {area} 입니다.')
  case 3:
    radius = int(input('반지름 입력: '))
    area = radius **2
    print(f'원의 넓이는 {area} 입니다.')
  case _:
    print('번호를 잘못 입력했습니다.')

# 1:사각형 2:삼각형 3:원
# 면적을 계산할 도형 번호: 2
# 밑변 입력: 50
# 높이 입력: 30
# 삼각형의 넓이는 1500 입니다.