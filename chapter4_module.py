import mod1

print(mod1.add(2,3))
print(mod1.sub(6,3))

# 함수를 직접 import 하면 모듈 이름을 붙이지 않고 함수 바로 사용 가능
from mod1 import *
add(3,4)
sub(7,6)

import mod2
print(mod2.PI)
a = mod2.Math()
a.solv(2)

# 다른 경로에서 모듈 불러오기
import sys
sys.path   
# 파이썬 라이브러리가 설치되어 있는 디렉터리 목록 조회
# 이 디렉터리에 저장된 파이썬 모듈은 해당 디렉터리로 이동하지 않아도 바로 import 가능함
sys.path.append("D:\\study")

#PYTHONPATH 환경변수를 사용하면 별도의 모듈 추가 작업 없이 불러오기 가능