"""
单例模式
保证一个类只有一个实例，并且该类可以自行实例化并向整个系统提供这个实例，
这个类称为单例类，单例模式是一种对象创建型模式。
"""
#吾能任务
class hello(object):
    def __new__(cls, *args, **kwargs):
        if not '_instance_one'in vars(cls):
            cls._instance_one=object.__new__(cls)
            return cls._instance_one
        return cls._instance_one

    def __init__(self):
        print(self)

a=hello()
b=hello()#输出结果会表明都放在一个内存里面说明两个都一个对象