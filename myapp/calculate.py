def regulate(var_a, var_b, index_mode):
  if type(var_a) is not int:
    var_a = 0
  if type(var_b) is not int:
    var_b = 0
  
  if index_mode == 0:
    ans = plus(var_a, var_b)
    equa = "a + b = "
  elif index_mode == 1:
    ans = minus(var_a, var_b)
    equa = "a - b = "
  elif index_mode == 2:
    ans = mlt_by(var_a, var_b)
    equa = "a * b = "
  elif index_mode == 3:
    ans = div_by(var_a, var_b)
    equa = "a / b = "
  else:
    ans = 0
  
  return equa + str(ans)


def plus(a, b):
  return a + b

def mlt_by(a, b):
  return a * b

def minus(a, b):
  return a - b

def div_by(a, b):
  return round(a / b, 2)