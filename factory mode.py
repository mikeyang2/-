"""
工厂模式
定义一个创建对象的接口 让子类去决定去实例化哪一个类
这里我设计了一个饭店的类 包括客人 菜 和两个随便定义的子类 牛肉肘子类 和猪肉蹄子类 和饭店类
牛肉和猪肉类去实例化 菜类  饭店类来输出 客人类来总领全文
"""
#吾能任务
class Person(object):#客人的类
    def __init__(self,name):
        self.name=name
    def order(self,menu):
        print(self.name+"欢迎光临寒舍")
        dishs=Restaurant.stir_fry(menu)
        dishs.order_dishs()

class Dishs(object):#菜的类
    def __init__(self,name):
        name=input("客官需要什么菜:")
        self.name=name
    def order_dishs(self):
        print("好的,客官需要%s,小的马上给大爷准备"%self.name)

class Beef(Dishs):#牛肉子类 继承菜类
    def order_dishs(self):
        print("好的,客官需要%s,小的马上给大爷准备" % self.name)

class Pork(Dishs):#猪肉子类 继承菜类
    def order_dishs(self):
        print("好的,客官需要%s,小的马上给大爷准备" % self.name)

class Restaurant(object):#饭店(工厂)类
    def stir_fry(type):
        if type=="牛肉肘子":
            return Beef("牛肉肘子")
        elif type=="猪肉蹄子":
            return Pork("猪肉蹄子")
        else:
            return("客官 没有您要点的菜")

if __name__=='__main__':
    NAME=input("请问客官尊姓大名:")
    p=Person(NAME)
    p.order("牛肉肘子")




