#1

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return str(self.x)+","+str(self.y)

    def reflect_x(self):
        xref=-self.x

        return Point(xref,self.y)


print(Point(3,5).reflect_x())

#2

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # Put your new method here
    def move(self, dx, dy):
        self.x=self.x+dx
        self.y=self.y+dy

    def __str__(self):
        return str(self.x)+","+str(self.y)
