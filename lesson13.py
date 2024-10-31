class Cylinder:
    def __init__(self, radius, height, color):
        self.r = radius
        self.h = height
        self.c = color

    def calc_area(self, is_closed=True):
        if is_closed:
            area = 2 * 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            area = round(area, 2)
            print(f"Area of closed cylinder is : {area}")
        else:
            area = 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            area = round(area, 2)
            print(f"Area of open cylinder is : {area}")

    def calc_volume(self):
        v = 22 / 7 * self.r ** 2 * self.h
        v = round(v, 2)
        print(f"Volume of cylinder is : {v}")


c1 = Cylinder(10, 11, "Red")
c2 = Cylinder(7.8, 22.6, "Blue")
c1.calc_volume()
c1.calc_area()
c1.calc_area(is_closed=False)
c2.calc_volume()
c2.calc_area()
