# class Cookie:
#     pass

# a = Cookie()
# b = Cookie()

# print(a)
# print(id(a))
# print(type(a))

# print(b)
# print(id(b))
# print(type(b))

class FourCal:
    calname = "계산기"
    def __init__(self,first=1,second=1) -> None:
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print(result)
        return result

    def sub(self):
        result = self.first - self.second
        print(result)
        return result
    
    def div(self):
        result = self.first / self.second
        print(result)
        return result
    
a = FourCal()
a.add()
c = FourCal()
print(FourCal.calname,c.calname)
c.calname = "다기능 계산기"
FourCal.calname = "멀티 계산기"
print(FourCal.calname,a.calname,c.calname)

class MoreFourCal(FourCal):
    def div(self):
        if self.second == 0:
            print("2번째 인자값은 0을 입력하면 안됨")
            return 0
        else:
            result = self.first / self.second
            print(result)
            return result

b = MoreFourCal(4,0)
b.add()
b.div()