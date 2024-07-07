#패키지 내의 다른 모듈을 미리 import가능
from .graphic.render import render_test

#패키지 수준에서 변수와 함수 정의
VERSION=3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

#여기에 패키지 초기화 코드를 작성. 패키지를 처음 import할 때 초기화 코드가 실행된다.
#한 번 실행된 후에는 다시 import를 수행하더라도 실행되지 않는다.
print("Initializing game")