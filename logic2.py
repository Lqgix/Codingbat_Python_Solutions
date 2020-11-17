def make_bricks(small, big, goal):
  smallw = 1
  bigw = 5

  req_bigs = goal // 5
  if req_bigs >= big:
    req_bigs = big

  goal = goal - req_bigs * 5
  if goal == 0:
    return True


  req_small = goal
  if req_small >= small:
    req_small = small

  goal = goal - req_small
  if goal == 0:
    return True

  return False

def lone_sum(a, b, c):
  if a == b == c:
    sum = 0
  elif a == b:
    sum = c
  elif a == c:
    sum = b
  elif b == c:
    sum = a

  else:
    sum = a + b + c
  return sum

def lucky_sum(a, b, c):
  if a == 13:
    sum = 0
  elif b == 13:
    sum = a
  elif c == 13:
    sum = a+b
  else:
    sum = a + b + c
  return sum

def no_teen_sum(a, b, c):
  a,b,c = fix_teen(a),fix_teen(b),fix_teen(c)
  return a+b+c

def fix_teen(num):
  if num >= 13 and num <= 19:
    if num != 15 and num != 16:
      num = 0
    else:
      pass
  return num

def round_sum(a, b, c):
  return( round10(a) + round10(b) + round10(c) )

def round10(num):
  quotient,remainder = divmod(num,10)
  if remainder >= 5:
    quotient += 1
  return quotient*10

def close_far(a, b, c):
  if abs(b-a) <= 1 and abs(c-b) > 1 and abs(c - a) > 1:
    return True
  elif abs(c-a) <= 1 and abs(b-c) > 1 and abs(b - a) > 1:
    return True
  else:
    return False

def make_chocolate(small, big, goal):
  smallw = 1
  bigw = 5
  req_bigs = goal // 5
  if req_bigs >= big:
    req_bigs = big
    goal = goal - req_bigs * 5
  if goal == 0:
    return 0
    req_small = goal
  if req_small >= small:
    req_small = small
    goal = goal - req_small
  if goal == 0:
    return req_small
    return -1
    
