# два квадрата задаются с помощью координат верхнего левого и нижнего правого углов
def collide(x0, y0, x1, y1, x2, y2, x3, y3):
    if x1 < x2 or x0 > x3 or y1 < y2 or y0 > y3:
        return False
    return True
