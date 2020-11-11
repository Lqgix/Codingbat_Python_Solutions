def cigar_party(cigars, is_weekend):
  if(is_weekend == True):
    if(cigars >= 40):
      return True
    else:
      return False
  elif(is_weekend == False):
    if(cigars >= 40) and (cigars <= 60):
      return True
    else:
      return False

def date_fashion(you, date):
  if(you <= 2) or (date<= 2):
    return 0
  elif(you >= 8) or (date >= 8):
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  if(is_summer == True):
    if(temp <= 100) and (temp >= 60):
      return True
    else:
      return False
  else:
    if(temp <= 90) and (temp >= 60):
      return True
    else:
      return False

def caught_speeding(speed, is_birthday):
  r = 0
  if(is_birthday == True):
    if(speed <= 60):
      r = 0
    elif(speed <= 65) and (speed >= 61):
      r = 0
    elif(speed <= 85) and (speed >= 81):
      r = 1
    else:
      if(speed > 65) and (speed < 81):
        r = 1
      else:
        r = 2
  else:
    if(speed <= 60):
      r = 0
    elif(speed >= 61) and (speed <= 80):
      r = 1
    elif(speed >= 81):
      r = 2
    else:
      return 2
  return r

def sorta_sum(a, b):
  if(a + b >= 10) and (a + b <= 19):
    return 20
  else:
    return a + b

def alarm_clock(day, vacation):
  if(vacation == True):
    if(day >= 1) and (day <= 5):
      return '10:00'
    elif(day == 0) or (day == 6):
      return 'off'
  else:
    if(day >= 1) and (day <= 5):
      return '7:00'
    elif(day == 0) or (day == 6):
      return '10:00'

def love6(a, b):
  if(a == 6) or (b == 6) or (abs(a - b) == 6) or (a + b == 6):
    return True
  else:
    return False

def in1to10(n, outside_mode):
  if outside_mode == False:
    if n > 0 and n < 11:
      return True
    return False
  else:
    if n < 2 or n > 9:
      return True
    return False

def near_ten(num):
  if str(num)[-1] in "12890":
    return True
  return False

  
