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
    
