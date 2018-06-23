"""Class object for rational numbers"""

class Rational():
    
    
    """
    Constructor for rational number from two integers.
    Represents numerator/denominator

    Input:
    int numerator
    int denominator

    The additional logic is to ensure positive denominators.
    """
    def __init__(numerator, denominator=1):
        if b != 0:
            self.numerator = int(numerator * (denominator/abs(denominator))
            self.b = abs(b)
        else:
            raise ZeroDivisionError("The denominator must be non-zero")
    
    ####################################################

    # Defining standard operations on rational numbers #

    ####################################################
    
    """
    The following overloaded operators represent addition of Rational Numbers with Rational Numbers

    `other` may be a rational number or an integer
    """

    def __add__(self, other):
        other = Rational(other)
        return Rational((self.numerator * other.denominator) + (self.denominator * other.numerator),
                        self.denominator * other.denominator)

    def __sub__(self, other):
        other = Rational(other)
        return Rational((self.numerator * other.denominator) - (self.denominator * other.numerator),
                        self.denominator * other.denominator)

    def __mul__(self, other):
        other = Rational(other)
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        other = Rational(other)
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __neg__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    """
    Exponentiation operator
    
    n.b. Defined only for integer powers
    """
    def __pow__(self, power):
        
        #For positive powers just iteratively multiply
        if power > 0:
            q = 1
            while power > 0:
                q *= self
                power -= 1
            return q

        #If 0 return 1
        elif power == 0:
            return 1

        #Define reciprocal in the case of `self**-1`
        elif power == -1:
            return Rational(self.denominator, self.numerator)
        
        #For negative powers iteratively multiply by the reciprocal
        else:
            reciprocal = self ** -1
            q = 1
            while power < 0:
                q *= (reciprocal)
                return q


    # Make commutative operators commutative

    __radd__ = __add__
    __rmul__ = __mul__ 

    # Define assignment operators +=, -=, *=, /=, **=

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __itruediv__(self, other):
        self = self / other
        return self

    def __ipow__(self, power):
        self = self ** power
        return self


    ########################################################

    # Add additional constructors for other types of input #

    ########################################################
    

    """
    Constructor from string of the form "a/b"
    """
    @classmethod
    def from_str(string):
        vals = string.split('/')
        return Rational(int(vals[0]), int(vals[1]))

    
    
