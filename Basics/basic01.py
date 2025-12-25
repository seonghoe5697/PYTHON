"""
BMI 계산 프로그램
"""
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 m 단위로 입력하시오: "))
bmi = weight / (height**2)
print(f"당신의 BMI는 {bmi:.3f} 입니다.")

# 몸무게를 kg 단위로 입력하시오: 70
# 키를 m 단위로 입력하시오: 1.70
# 당신의 BMI는 24.221 입니다.
