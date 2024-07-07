#패키지 내의 다른 모듈을 미리 import가능
from .graphic.render import render_test

#패키지 수준에서 변수와 함수 정의
VERSION=3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

#여기에 패키지 초기화 코드를 작성
print("Initializing game")