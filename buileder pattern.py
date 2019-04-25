"""
建造者模式
建造者模式是将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示
在实际的编程中我们可以通过这种方式来避免一个类过于繁杂
将一个功能分给多个类一起工作
避免功能过于冗杂
"""
#吾能任务
class Builder(object):#先构建一个画人的步鄹的类
    def create_foot(self):
        pass
    def create_hand(self):
        pass
    def create_head(self):
        pass
    def create_arm(self):
        pass
    def create_leg(self):
        pass

class Mike(Builder):#通过继承定义一个画Mike的类
    def create_foot(self):
        print("画脚")
    def create_hand(self):
        print("画手")
    def create_head(self):
        print("画头")
    def create_arm(self):
        print("画手臂")
    def create_leg(self):
        print("画腿")

class Tom(Builder):#通过继承定义一个画Tom的类
    def create_foot(self):
        print("画脚")
    def create_hand(self):
        print("画手")
    def create_head(self):
        print("画头")
    def create_arm(self):
        print("画手臂")
    def create_leg(self):
        print("画腿")

class Artict(object):#定义一个画家的类 来画出身体
    def __init__(self,person):
        self.person=person
    def create_person(self):
        hand=self.person.create_hand()
        foot=self.person.create_foot()
        head=self.person.create_head()
        arm=self.person.create_arm()
        leg=self.person.create_leg()

if __name__=='__main__':
    mike=Mike()
    tom=Tom()
    drawmike=Artict(mike)
    drawtom=Artict(tom)
    drawmike.create_person()
    drawtom.create_person()








