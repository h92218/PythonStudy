# 클래스의 생성
class FourCal:
    #객체 생성 시점에 자동으로 호출되는 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
a = FourCal(4,3)
a.first
a.second
a.add()

# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
a.pow()

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4,0)
a.div()

# 클래스 변수
# 객체변수와 달리 클래스로 만든 모든 객체에 공유된다.
class Family:
    lastname = "김"