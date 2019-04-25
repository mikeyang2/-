"""
装饰者模式
一个饮料店里面猪肉和牛肉 并且有辣椒和甜酱两种辅料可以添加。
我们可以计算出一共有中6组合产品。
装饰模式以对客户透明的方式动态地给一个对象附加上更多的责任，换言之，
客户端并不会觉得对象在装饰前和装饰后有什么不同。装饰模式可以在不需要创造更多子类的情况下，
将对象的功能加以扩展。这就是装饰模式的模式动机。
因为装饰器模式是在给对象增加责任。所以装饰器模式为对象结构型设计模式
(对象是因为其是给对象而不是类增加责任，结构型模式就是描述如何将类或者对象结合在一起形成更大的结构，
就像搭积木，可以通过简单积木的组合形成复杂的、功能更为强大的结构）。
"""
class Meet():
    name = ""
    price = 0.0
    type = "肉"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class Beef(Meet):#原料
    def __init__(self):
        self.name = "牛肉"
        self.price = 4.0

class Pork(Meet):#原料
    def __init__(self):
        self.name = "猪肉"
        self.price = 5.0

class MeetDecorator():
    def getName(self):
        pass
    def getPrice(self):
        pass

class PepperDecorator(MeetDecorator):#辅料
    def __init__(self, meet):
        self.meet= meet
    def getName(self):
        return self.meet.getName() + " +辣椒"
    def getPrice(self):
        return self.meet.getPrice() + 0.3

class SweetDecorator(MeetDecorator):#辅料
    def __init__(self, meet):
        self.meet = meet
    def getName(self):
        return self.meet.getName() + "+甜酱"
    def getPrice(self):
        return self.meet.getPrice() + 0.5

if  __name__=="__main__":
    beef=Beef()
    print("名称:%s"%beef.getName())
    print("价格:%s"%beef.getPrice())
    pepper_beef=PepperDecorator(beef)
    print("名称:%s" %pepper_beef.getName())
    print("价格:%s" %pepper_beef.getPrice())



