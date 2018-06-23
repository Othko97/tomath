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
    def __init__(self, numerator, denominator=1):
        if denominator != 0:
            self.numerator = int(numerator * (denominator/abs(denominator)))
            self.denominator = abs(denominator)
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
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational((self.numerator * other.denominator) + (self.denominator * other.numerator),
                        self.denominator * other.denominator)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational((self.numerator * other.denominator) - (self.denominator * other.numerator),
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
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
                power += 1
            return q


    # Make commutative operators commutative

    __radd__ = __add__
    __rmul__ = __mul__

    def __rsub__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return other - self

    def __rtruediv__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return other / self

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
    def from_str(cls, string):
        vals = string.split('/')
        return cls(int(vals[0]), int(vals[1]))

    
    ##############################

    # Overload Equality Relation #

    ##############################

    """
    Overload operator for equality
    """
    def __eq__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return other.numerator * self.denominator == self.numerator * other.denominator


    ###########################################

    # Set output formats of __str__, __repr__ #

    ###########################################


    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
