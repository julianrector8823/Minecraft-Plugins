class Test(int):

  def __new__(cls, n):
    return int.__new__(cls, n)
    
  def cube(self):
    return pow(self, 3)
