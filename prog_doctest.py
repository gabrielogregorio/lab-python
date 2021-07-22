import doctest

class Fib:
  def calculo_fib(self, n):
    """
    método para calular o fibonacci

    >>> Fib().calculo_fib(10)
    55
    >>> Fib().calculo_fib(1)
    1
    >>> f.calculo_fib(-1)
    Traceback (most recent call last):
    ...
    ValueError: n tem que ser maior que 1
    """

    if n < 1:
      raise ValueError('n tem que ser maior que 1')

    a, b = 0, 1
    for i in range(n):
      a, b = b, a + b
    
    return a

if __name__ == '__main__':
  #doctest.testmod() 
  doctest.testmod(extraglobs={'f':Fib()})