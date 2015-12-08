class Renderable():
    def __init__(self,x,y,src,i):
        self._x = x
        self._y = y
        self.source = src
        self.id = i
        self.updated = True

    def getData(self):
        return [self.id, self.x, self.y, self.source]

    @property
    def x(self):
        return self._x

    @x.setter
    def _x(self, value):
        self._x = value
        self.updated = True

    @property
    def y(self):
        return self._y

    @x.setter
    def _y(self, value):
        self._y = value
        self.updated = True
