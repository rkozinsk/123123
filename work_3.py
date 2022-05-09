from turtle import color


class Shape:
    def __int__(self,x,y,polor):
        self.x = x
        self.y = y
        self.color = color

    def descripe(self):
        print(f"Figura w punkcie {self.x},{self.y} o kolorze {self.color}")

    def distancce(self, shape):
        return ((self.x - shape.x)**2 + (self.y - shape.y)**2) ** 0.5

    def __str__(self):
        return f'figura w punkcie'