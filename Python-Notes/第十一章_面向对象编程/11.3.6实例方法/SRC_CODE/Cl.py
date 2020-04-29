class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex = 1, weight = 0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight += 0.05
        print('eat...')

    def run(self):
        self.weight -= 0.01
        print('run...')

a1 = Animal(2, 0, 10.0)
print('a1 体重:{0:0.2f}'.format(a1.weight))
a1.eat()
print('a1 体重:{0:0.2f}'.format(a1.weight))
a1.run()
print('a1 体重:{0:0.2f}'.format(a1.weight))