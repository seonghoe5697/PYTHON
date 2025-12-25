'''
윤년을 판별하는 프로그램
'''
user_year = int(input("연도를 입력하세요: "))
if((user_year % 4 ==0 and user_year % 100 != 0) or (user_year % 400 ==0)):
    print(f"{user_year}년은 윤년 입니다.")
else:
    print(f"{user_year}년은 평년 입니다.")

# 출력
# 연도를 입력하세요: 2100
# 2100년은 평년 입니다.