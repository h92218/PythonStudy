# 여러가지 선택지 중 하나를 선택해서 입력받는 예제
prompt="""
1. Add
2. Del
3. List
4. Quit
Enter number:
"""

number=0
while number !=4:
    print(prompt)
    number = int(input())

# for문의 사용
'''
총 5명의 학생이 시험을 보았는데 시험점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다.
합격인지, 불합격인지 결과를 보여주시오
'''
marks = [90,25,67,45,80]
i = 0
for mark in marks:
    i = i + 1
    if mark >= 60:
        print("%d번 학생 : 합격" % i)
    else:
        print("%d번 학생 : 불합격" % i)


'''
합격인 경우만 축하메세지
'''
i=0
for mark in marks:
    i=i+1
    if mark < 60:
        continue
    print("%d번 학생 축하" % i)


#range함수
a = range(1,11)
add = 0
for b in a:
    add = add + b
print(add)

#리스트 컴프리헨션
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
result = [num*3 for num in a if num%2 == 0]
print(result)

#Q1. 다음 코드의 결과값은 무엇일까?
a = "Life is too short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("python")

#Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

#Q3. while문을 사용하여 다음과 같이 표시하는 프로그램을 작성해보자.
i = 0
while True:
    i+=1
    if(i>5):
        break
    print("*"*i)

#Q4. for문을 사용하여 1부터 100까지 출력
a = range(1,101)
for i in a:
    print(i)

#Q5. 평균점수 구하기
A=[70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)

#Q6. 다음 소스코드를 리스트 컴프리헨션을 사용하여 표현하기
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)

result = [n*2 for n in numbers if n % 2 == 1]
print(result)