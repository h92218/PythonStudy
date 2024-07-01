# 키워드 매개변수
'''
매개변수 앞에 **를 붙이면 매개변수 kwargs는 딕셔너리가 되고 key=value 형태의 입력값이 저장됨
'''
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo' , age=3)

# return값이 두개인 경우 하나의 튜플로 리턴됨.
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
# 분리하여 받고 싶은 경우
result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)

# lambda 예약어
add = lambda a, b: a+b
result = add(3,4)
print(result)

# 파일 읽고 쓰기
f = open("새파일.txt",'w')
for i in range(1,11):
    f.write("%d번째 줄입니다.\n" % i)
f.close()

# 파일 읽기 - readline
f = open("새파일.txt",'r')
while True:
    line = f.readline().strip()
    if not line:
        break
    print(line)
f.close()

# 파일 읽기 - readlines
# strip() : 개행문자 제거 
f = open("새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()

# 파일 읽기 - read
f = open("새파일.txt",'r')
data = f.read()
print(data)
f.close()

# 파일 읽기 - for문 사용
f = open("새파일.txt",'r')
for line in f:
    print(line.strip())
f.close()

#with 사용하기 - close 안 써도 됨 
with open("새파일.txt","w") as f:
    f.write("Life is too short, you")

#Q1.홀수 짝수 판별하는 함수 is_odd 작성하기
def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_odd(4))

#Q2. 모든 입력의 평균값 구하는 함수 작성
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)
print(avg_numbers(3,4,5))
print(avg_numbers(1,2,3,4,5))
    
#Q3. 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")
total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)

#Q4.출력 결과가 다른 것은?
print("you" "need" "python")
print("you" + "need" + "python")
print("you","need","python")
print("".join(["you","need","python"]))

#Q5.문자열 저장 후 다시 읽어 출력
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())
f2.close()

with open("test.txt","r") as f3:
    f3.read()

#Q6. 파일에 내용 추가
user_input = input("저장할 내용을 입력하세요 : ")
f = open('test2.txt',"a")
f.write(user_input+"\n")
f.close()

#Q7. 파일내의 "java" 를 "python" 으로 바꾸기
f = open("새파일.txt","r")
body = f.read()
f.close()
body = body.replace("java","python")
f = open("새파일.txt","w")
f.write(body)
f.close()



