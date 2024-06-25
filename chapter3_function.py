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