# defining a super class called line
class line:
    # init method to initialise the length
    def __init__(self,length):
        self._length = length
    
    # setter to set the length
    def set_length(self, value):
        self._length = value

    # getter to get the length
    def get_length(self):
        return self._length

    # method to calculate the perimeter 
    def perimeter(self):
        return self._length
    
# triangle is a derived class of line class
class triangle(line):
    # overriding the init method
    def __init__(self, a , b , c):
        self._side_a = line(a)
        self._side_b = line(b)
        self._side_c = line(c)

    # overriding perimeter method
    def perimeter(self):
        return sum([self._side_a.get_length() + self._side_b.get_length() , self._side_c.get_length()])
    
# rectangle is a derived class of line class
class rectangle(line):
    def __init__(self , w , h):
        self._side_w = line(w)
        self._side_h = line(h)

    # overriding perimeter method
    def perimeter(self):
        return 2 * sum([self._side_w.get_length() + self._side_h.get_length()])
    
    # defining new area method
    def area(self):
        return self._side_w.get_length() * self._side_w.get_length()

# creation of triangle object and call the respective methods 
triangle_obj = triangle(3, 4, 5)
print("Triangle perimeter:", triangle_obj.perimeter())

# creation of rectange object and call the respective methods
rectangle_obj = rectangle(2, 4)
print("Rectangle perimeter:", rectangle_obj.perimeter())
print("Rectangle area:", rectangle_obj.area())

rectangle_obj._side_w.set_length(3)
rectangle_obj._side_h.set_length(4)

print("Modified rectangle perimeter:", rectangle_obj.perimeter())
print("Modified rectangle area:", rectangle_obj.area())