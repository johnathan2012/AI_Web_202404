#自訂異常處理型別

class MyError(Exception):
   def __init__(self, radius):        
      self.radius = radius

   def __str__(self):
      return repr(self.radius)
