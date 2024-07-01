import sys
#입력값을 모두 더해 출력하는 스크립트
args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)
