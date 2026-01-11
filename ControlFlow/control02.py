'''
평균에 의한 합격/불합격
'''
sub1 = int(input("첫 번째 점수: "))
sub2 = int(input("두 번째 점수: "))
avg = (sub1+sub2)/2
if sub1<50 or sub2 < 50:
  print("결과: 과락으로 인한 불합격")
elif avg>70:
  if avg>90:
    grade = 'A'
  elif avg >80:
    grade = 'B'
  else:
    grade = "C"
  print(f'결과: 합격 (평균: {avg} 등급: {grade})')
else:
  print(f'결과: 평균 점수 미달로 인한 불합격 (평균: {avg})')

''' OUTPUT
첫 번째 점수: 70
두 번째 점수: 80
결과: 합격 (평균: 75.0 등급: C)
'''
