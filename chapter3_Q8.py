import sys
'''
import 는 현재 디렉터리에 있는 파일이나
파이썬 라이브러리가 저장된 디렉터에 있는 모듈만 불러올 수 있음 
'''
#입력값을 모두 더해 출력하는 스크립트
args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)
