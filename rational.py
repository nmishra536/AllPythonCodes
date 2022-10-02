#rational.py

def _gcd(a,b): #fix this
    if(b==0):
        return a
    else:
        return _gcd(b,a%b)

  

class Rational(object):
  def __init__(self,n, d=1):
    
    if d< 0:
      self.n = (-1 * n)//_gcd(n,d)
      self.d = (-1 * d)//_gcd(n,d)
    if d == 0:
      raise ValueError
    else:
      self.n = n//_gcd(n,d)
      self.d = d//_gcd(n,d)
  


  def __add__(self, other):
    lol = ((self.n*other.d) + (self.d*other.n))
    wolo = (self.d * other.d)
    g = int(_gcd(lol, wolo))
    return Rational((lol), (wolo))
    
  
  def __eq__(self, other):
    if (self.n*other.d) == (self.d*other.n):
      return True

  def __float__(self):
    dil = self.n/self.d
    return (dil)
  
  def __ge__(self, other):
    if (self.n/self.d) >= (other.n/other.d):
      return True

  def __gt__(self, other):
    if (self.n/self.d) > (other.n/other.d):
      return True
  
  def __le__(self, other):
    if (self.n/self.d) <= (other.n/other.d):
      return True

  def __lt__(self, other):
    if (self.n/self.d) < (other.n/other.d):
      return True

  def __mul__(self, other):
    venti = ((self.n*other.n))
    bard = ((self.d*other.d))
    g = int(_gcd(venti, bard))
    return Rational((venti), (bard))
    

  def __ne__(self, other):
    if (self.n*other.d) != (self.d*other.n):
      return True

  def __repr__(self):
      if self.d == 1:
          return "rational.Rational("+str(self.n)+")"
      else:
          if abs(self.d) != self.d:
              return "rational.Rational(-"+str(self.n)+", "+str(abs(self.d))+")"
          else:
              return "rational.Rational("+str(self.n)+", "+str(self.d)+")"

  def __str__(self):
      return "{}/{}".format(self.n, self.d)

  def __sub__(self, other):
    lol = ((self.n*other.d) - (self.d*other.n))
    wolo = (self.d * other.d)
    g = int(_gcd(lol, wolo))
    return Rational((lol), (wolo))
    

  def __truediv__(self, other):
    morax = (self.n *other.d)
    rex = (self.d * other.n)
    if rex <0:
      return Rational((morax*-1), (rex*-1))
    else:
      return Rational((morax), (rex))


  def inverse(self):
    return Rational(self.d, self.n)
