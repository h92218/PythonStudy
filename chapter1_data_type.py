#Q1. 평균 구하기
a = (85+80+73)/3
print(a)


#Q2. 13이 홀수인지 짝수인지 판별하기
if(13%2 == 0):
    print("짝수")
else:
    print("홀수")

    
#Q3. 문자열 슬라이스
pin = "881120-1068234"
yyyymmdd = "19" + pin.split('-')[0]
print(yyyymmdd)
print(pin.split('-')[1])


#Q4. 문자열 인덱싱. 성별숫자 출력
pin = "881120-1068234"
print(pin[7])


#Q5. a:b:c:d 를 a#b#c#d로 바꾸기
a= "a:b:c:d"
b = a.replace(":","#")
print(b)


#Q6. 리스트 역순 정렬하기
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)


#Q7. 리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)


#Q8. (1,2,3) 튜플을 (1,2,3,4)로 만들기
a = (1,2,3)
a = a + (4,)
print(a)

#Q9. 오류가 발생하는 경우 찾기
a = dict()
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
#a[[1]] = 'python' <- key에 리스트는 쓸 수 없음.
a[250] = 'python'
print(a)


#Q10. 딕셔너리 a에서 'B'에 해당하는 값을 제거해보기
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#Q11. a리스트에서 중복숫자 제거해보기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)
print(b)
c = list(b)
print(c)

#Q12. 파이썬 변수
a = b = [1,2,3]
a[1] = 4
print(b)
print(id(a))
print(id(b))
#a리스트와 b리스트 동일함
#깊은복
a = [2,3,4]
b = a[:]
a[1] = 4
print(a)
print(b)
