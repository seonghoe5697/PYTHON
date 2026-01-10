'''
시간 단위 변환 (초 -> 분,초)
'''
totalsecond = int(input('초를 입력하세요: '))
minute = totalsecond // 60
second = totalsecond % 60
print(f'{totalsecond}초는 {minute}분 {second}초 입니다.')

# output
'''
초를 입력하세요: 150
150초는 2분 30초 입니다.
'''