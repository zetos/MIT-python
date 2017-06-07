# OOP

# Coordinate Class definition
class Coordinate(object):
    # Attributes definition
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    #used when print(Coordinate(x,y))
    def __str__(self):
        return 'Satanic <'+str(self.x)+','+str(self.y)+'>'


c = Coordinate(3,4)
zero = Coordinate(0,0)

print('c x:', c.x)
print('zero x:', zero.x)
print('c distance', c.distance(zero))
print('c distance', Coordinate.distance(c, zero))
print('c:',c)

# Fraction Class definition
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """Returns a string representation of self"""
        return str(self.num)+"/"+str(self.denom)
    def __add__(self, other):
        """Returns a new fraction representing the addition"""
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """Returns a new fraction representing the subtraction"""
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """Returns a float value of the fraction"""
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing"""
        return Fraction(self.denom, self.num)

x = Fraction(1,4)
y = Fraction(3,4)
z = x+y

print('z:',z)
print(float(z))
print(Fraction.__float__(z))
print(float(y.inverse()))
