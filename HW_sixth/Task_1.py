class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return(self.x)

    def get_y(self):
        return(self.y)

    def get(self):
        return self.x, self.y

    def set_x(self):
        x_new = float(input('New value for x is '))
        self.x = x_new

    def set_y(self):
        y_new = float(input('New value for y is '))
        self.y = y_new

    def set(self):
        x_new = float(input('New value for x is '))
        self.x = x_new
        y_new = float(input('New value for y is '))
        self.y = y_new

a = 0
b = 0

point = Point(a, b)
print(point.get_x())
print(point.get_y())
point.set_x()
print(point.get_x())
point.set_y()
print(point.get_y())
point.set()
print(point.get_x(), ' ', point.get_y())
point.set()
print(point.get())
