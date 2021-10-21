class Point(): 
    def __init__(self): 
        x1 = float(input('Value for x is ')) 
        y1 = float(input('Value for y is '))
        self.x = x1
        self.y = y1
        
class Shape(): 
    def per(self):
        return 0
    def area(self):
        return 0
    
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
                    #print((p[i].x - p[j].x), ' ',(p[i].y - p[j].y))
        for i in range(len(v)):
            for j in range(len(v)):
                if (v[i][0]*v[j][0] + v[i][1]*v[j][1]) == 0:
                    s1 = (v[i][0]**2 + v[i][1]**2)**0.5
                    s2 = (v[j][0]**2 + v[j][1]**2)**0.5
                    break
        
        self.side1 = s1
        self.side2 = s2
    def area(self):
        return self.side1*self.side2
    def per(self):
        return 2*(self.side1 + self.side2)
class Square(Rect):
    def area(self):
        return self.side1*self.side1
    def per(self):
        return 4*(self.side1)
a = Rect()
print(a.area())
print(a.per())
b = Square()
print(b.area())
print(b.per())
