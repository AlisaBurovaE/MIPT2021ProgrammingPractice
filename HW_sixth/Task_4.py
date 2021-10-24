import math

class Point():
    def __init__(self):
        x1 = float(input('Value for x is '))
        y1 = float(input('Value for y is '))
        self.x = x1
        self.y = y1


from abc import ABC, abstractmethod


class Shape(ABC):
    def per(self):
        return 0

    def area(self):
        return 0

    def __str__(self):
        output = [self.__class__.__name__, str(self.area()), str(self.per())]
        return '  '.join(output)


class Rect(Shape):
    def __init__(self):
        p = []
        for i in range(4):
            temp = Point()
            p.append(temp)
        self.sidess(p)

    def sidess(self, p):
        i = 0
        j = 0
        v = []
        s1 = 0
        s2 = 0
        for i in range(4):
            for j in range(4):
                if i != j:
                    v.append([(p[i].x - p[j].x), (p[i].y - p[j].y)])
                    # print((p[i].x - p[j].x), ' ',(p[i].y - p[j].y))
        for i in range(len(v)):
            for j in range(len(v)):
                if (v[i][0] * v[j][0] + v[i][1] * v[j][1]) == 0:
                    s1 = (v[i][0] ** 2 + v[i][1] ** 2) ** 0.5
                    s2 = (v[j][0] ** 2 + v[j][1] ** 2) ** 0.5
                    break

        self.side1 = s1
        self.side2 = s2

    def area(self):
        return self.side1 * self.side2

    def per(self):
        return 2 * (self.side1 + self.side2)


class Square(Rect):
    def area(self):
        return self.side1 * self.side1

    def per(self):
        return 4 * (self.side1)


class Triangle(Shape):
    def __init__(self):
        self.p = [];
        self.r = 0
        self.s = 0
        for i in range(3):
            temp = Point()
            self.p.append(temp)
        self.sidess()
        self.radius()
        self.area_triangle()

    def radius(self):
        if (self.__class__.__name__ != 'Triangle'):
            cos_angle = (-(self.side3 ** 2) + (self.side1 ** 2) + (self.side2 ** 2))/(2 * self.side1 * self.side2)
            cos_2angle = 2 * (cos_angle ** 2) - 1
            r = (((self.side3 ** 2)/(2 + 2*cos_2angle))) ** (0.5)
            self.r = r

    def sidess(self):
        i = 0
        j = 0
        v = []
        s1 = 0
        s2 = 0
        s3 = 0

        for i in range(3):
            for j in range(3):
                if i < j:
                    v.append([(self.p[i].x - self.p[j].x), (self.p[i].y - self.p[j].y)])


        s1 = ((v[0][0]) ** 2 + (v[0][1]) ** 2) ** (0.5)
        s2 = ((v[1][0]) ** 2 + (v[1][1]) ** 2) ** (0.5)
        s3 = ((v[2][0]) ** 2 + (v[2][1]) ** 2) ** (0.5)

        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def area_triangle(self):
        v = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    v.append([(self.p[i].x - self.p[j].x), (self.p[i].y - self.p[j].y)])
        cos_angle = ((v[0][0])*(v[1][0]) + (v[0][1])*(v[1][1]) )/(self.side1 * self.side2)
        
        sin_angle = (1 - cos_angle ** 2) ** (0.5) 
        self.s = 0.5 * (self.side1 * self.side2 * sin_angle)
    def area(self):
        return self.s

    def per(self):
        return (self.side1 + self.side2 + self.side3)

class Circle(Triangle):

    def area(self):
        return (math.pi * (self.r ** 2))
    def per(self):
        return (2 * math.pi * self.r)

class Rhomb(Triangle):

    def area(self):
        return (2 * self.s)
    def per(self):
        if ((self.side1 != self.side2) and (self.side1 != self.side3)):
            return (4 * self.side2)
        else:
            return (4 * self.side1)


a = Rect()
print(a)
b = Square()
print(b)
c = Triangle()
print(c)
d = Circle()
print(d)
e = Rhomb()
print(e)
