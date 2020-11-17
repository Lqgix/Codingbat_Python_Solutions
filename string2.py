def double_char(string):
  s = ''
  for char in string:
    s = s + char + char
  return s

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
  return True if str.count("cat") == str.count("dog") else False

def count_code(str):
  temp = ""
  sum = 0
  for i in range(len(str)-3):
    temp = str[i]+str[i+1]+str[i+3]
    if temp == "coe":
      sum += 1
  return sum

def end_other(a, b):
  a,b = a.lower(),b.lower()
  return True if a.endswith(b) or b.endswith(a) else False

def xyz_there(str):
  if len(str) < 3:
    return False
  else:
    if ".xyz" in str:
      str = str.replace(".xyz", "    ")
      if "xyz" in str:
        return True
      return False
    elif "xyz" in str:
      return True
    return False
