def first_last6(nums):
  if(nums[-1] == 6) or (nums[0] == 6):
    return True
  return False

def same_first_last(nums):
    if(len(nums) >= 1) and (nums[0] == nums[len(nums)-1]):
      return True
    return False

def make_pi():
  ls = [3,1,4]
  return ls

def common_end(a, b):
  if(a[0] == b[0]) or (a[-1] == b[-1]):
    return True
  return False

def sum3(nums):
  return sum(nums)

def rotate_left3(arr):
  n = len(arr)
  x = arr[0]
  for i in range(0, n-1):
    arr[i] = arr[i+1]

  arr[n-1] = x
  return arr

def reverse3(nums):
  nums.reverse()
  return nums

def max_end3(nums):
  nums1 = []
  nums1.append(nums[0])
  nums1.append(nums[2])
  m = max(nums1)
  nums1.append(m)
  nums1[0], nums1[1] = m,m
  return nums1

def sum2(nums):
  if(len(nums) == 0):
    return 0
  elif(len(nums) < 2):
    return sum(nums)
  else:
    return(nums[0] + nums[1])

def middle_way(a, b):
  mid = []
  mid.append(a[1])
  mid.append(b[1])
  return mid

def make_ends(nums):
  end = []
  end.append(nums[0])
  end.append(nums[-1])
  return end

def has23(nums):
  if(3 in nums) or (2 in nums):
    return True
  return False
