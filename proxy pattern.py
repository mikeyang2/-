"""
代理模式
代理模式是一种常用的设计模式，它主要用来通过一个对象(比如B)给一个对象(比如A) 提供’代理’的方式方式访问。
比如一个对象不方便直接引用，代理就在这个对象和访问者之间做了中介
在这个例子里面 为了向一个公司的销售主管谈话，用户首先会向销售主管办公室的接待员打个电话，随后接待员转接电话。
在这个例子中，销售主管会是用户希望交谈的目标，接待员就是一个代理，保护主体不受用户直接要求谈话中苦恼。
"""
#吾能任务
import time
class Manager(object):
    def work(self):
        pass

    def talk(self):
        pass

class SalesManager(Manager):
    def work(self):
        print("销售经理正在工作")

    def talk(self):
        print("销售经理可以和您进行通话")

class Proxy(Manager):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print("正在询问销售经理")
        if self.busy == 'Yes':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("销售经理很忙")


if __name__ == '__main__':
    p = Proxy()
    p.work()

