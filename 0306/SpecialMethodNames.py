'''
类内部方法
'''

# __slots__： 限制类的属性,但不限制方法,
# __init__： 构造函数
# __del__：  析构函数 清除对象的顺序是字典顺序
# __str__: 对象和打印都会自动转为__str__定义的形式
#__repr__:对象会输出是内存位置，打印是__repr__定义的形式

# 用处：好像没什么用
'''
class Student():
    def __init__(self):
        self.name='turing'
        self.job ='Programmer' #error
    def salary(self):
        return 8000
    __slots__ = ('name','age')
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

stu = Student()
stu
print(stu)
stu.name='Turing'
stu.age=24

stu.weight=50   #error Student has no attribute 'weight'
print(stu.job)  #error Student has no attribute 'job'
print(stu.age)
print(stu.weight)  #error
print(stu.salary()) #正确
'''
#__getattr__:若属性不存在会在这里定义去找，主要用于链式调用  具体应用场景。。。
#__iter__:使得对象可枚举 需要实现__next__来使用
#__getitem__:使得对象可通过下表访问
#__call__:使得类可以被当做函数使用，定义了此函数就可以stu()调用
#sep 用于分割，end用于结尾
#help(print)
class Student():
    def __init__(self,name='Turing'):
        self.name=name
        self.age=24
    def __iter__(self):
        return self
    def __getitem__(self, item):
        if item==0:
            return self.name
        elif item==1:
            return self.age
    def __getattr__(self, item):
        if item=='salary':
            return 10000
        else :
            return Student('%s.%s' % (self.name,item))  #链式调用
    def __call__(self, *args, **kwargs):
        print(self.name,self.age,sep='#',end='!')

    def __next__(self):
        if self.age<20:
            raise StopIteration # 退出循环的条件
        self.age-=1
        return self.age
    def __str__(self):
        return self.name

s = Student()
for adultAge in s:
    print(adultAge)

print(s.name)
print(s[1])
print(s.salary)
print(s.middleName.FamilyName)
s()
help(print)