# echo 모듈을 import하여 실행하는 방법(PYTHONPATH 설정이 선행되어야 함)
#1
import game.sound.echo
game.sound.echo_echo_test()

#2
from game.sound import echo
echo.echo_test()

#3
from game.sound.echo import echo_test
echo_test()

#도트 연산자(.)를 사용하면 가장 마지막 항목은 반드시 모듈 또는 패키지

'''
__init__.py의 용도 : 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 함
__init__.py 파일이 없다면 패키지로 인식되지 않는다.(3.3 버전부터는 파일이 없어도 인식함)
해당 파일에 패키지를 처음 불러올 때 실행되어야 하는 코드를 작성할 수 있음
예를 들어 db 연결이나 설정파일로드와 같은 작업.
'''
