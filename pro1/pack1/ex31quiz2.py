# 다중상속 연습문제
# super
class Animal:
    def move(self):
        print('대부분의 동물들은 4발로 걸어요')

class Dog(Animal):
    # Field
    name = '개'

    # Method
    def move(self):
        print('댕댕이')


class Cat(Animal):
    # Field
    name = '고양이'

    # Method
    def move(self):
        print('냥냥이')


class Wolf(Dog, Cat):
    pass


class Fox(Cat, Dog):
    #Method
    def move(self):
        print('여우')
    
    def foxMethod(self):
        print('Fox 고유 메소드')

animal = [Dog(), Cat(), Wolf(), Fox()]
for a in animal:
    print('---'*10)
    print(a)      
    a.move()