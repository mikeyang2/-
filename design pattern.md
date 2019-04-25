# 工厂模式

## 理解
定义一个创建对象的接口 让子类去决定去实例化哪一个类
这里我设计了一个饭店的类 包括客人 菜 和两个随便定义的子类 牛肉肘子类 和猪肉蹄子类 和饭店类
牛肉和猪肉类去实例化 菜类  饭店类来输出 客人类来总领全文

## 代码
![](https://img-blog.csdnimg.cn/20190425113439281.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019042511460527.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425113514228.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

# 建造者模式

## 理解
建造者模式是将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示
在实际的编程中我们可以通过这种方式来避免一个类过于繁杂
将一个功能分给多个类一起工作
避免功能过于冗杂

## 代码
![](https://img-blog.csdnimg.cn/20190425112542660.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)


![](https://img-blog.csdnimg.cn/20190425112810318.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425112848434.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019042511302713.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

# 组合模式

## 理解
组合模式是将对象组合成成树形结构以表示“部分-整体”的层次结构,组合模式使得用户对单个对象和组合对象的使用具有一致性.
在下面的代码中，我定义了公司类，每一个公司都有自己的组织结构，越是大型的企业，其组织结构就会越复杂。大多数情况下，
假设一个具有HR部门，财务部门和研发部门，同时在全国有分支公司的总公司，其公司结构，可以表示成如下逻辑

## 代码
![](https://img-blog.csdnimg.cn/20190425115449169.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425115515579.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019042511553825.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425115600157.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425115631194.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019042511564610.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

# 装饰者模式

## 理解
一个饮料店里面猪肉和牛肉 并且有辣椒和甜酱两种辅料可以添加。
我们可以计算出一共有中6组合产品。
装饰模式以对客户透明的方式动态地给一个对象附加上更多的责任，换言之，
客户端并不会觉得对象在装饰前和装饰后有什么不同。装饰模式可以在不需要创造更多子类的情况下，
将对象的功能加以扩展。这就是装饰模式的模式动机。
因为装饰器模式是在给对象增加责任。所以装饰器模式为对象结构型设计模式
(对象是因为其是给对象而不是类增加责任，结构型模式就是描述如何将类或者对象结合在一起形成更大的结构，
就像搭积木，可以通过简单积木的组合形成复杂的、功能更为强大的结构）

## 代码
![](https://img-blog.csdnimg.cn/20190425114945891.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425115022685.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019042511504530.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/2019042511510589.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

# 单例模式

## 理解
保证一个类只有一个实例，并且该类可以自行实例化并向整个系统提供这个实例，
这个类称为单例类，单例模式是一种对象创建型模式
是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
在下面的代码中 我们设计了一个类
在后面我们定义a,b两个对象并将它们用类定义
但在单例模式中a,b其实指的是一个对象，一个东西

## 代码
![](https://img-blog.csdnimg.cn/20190425114315857.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

# 代理模式

## 理解
代理模式是一种常用的设计模式，它主要用来通过一个对象(比如B)给一个对象(比如A) 提供’代理’的方式方式访问。
比如一个对象不方便直接引用，代理就在这个对象和访问者之间做了中介
在这个例子里面 为了向一个公司的销售主管谈话，用户首先会向销售主管办公室的接待员打个电话，随后接待员转接电话。
在这个例子中，销售主管会是用户希望交谈的目标，接待员就是一个代理，保护主体不受用户直接要求谈话中苦恼。

## 代码
![](https://img-blog.csdnimg.cn/2019042511400470.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425114029530.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

![](https://img-blog.csdnimg.cn/20190425114056942.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzOTE5Nzkw,size_16,color_FFFFFF,t_70)

