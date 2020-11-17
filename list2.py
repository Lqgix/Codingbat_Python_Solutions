def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  nums.sort()
  numss = nums[1:-1]
  return sum(numss)/len(numss)

def sum13(nums):
  res = 0
  skip = 0

  for i in range(len(nums)):
    if (nums[i] == 13 or (i!=0 and nums[i-1] == 13)):
      skip += nums[i]
    else:
      res += nums[i]
  return res

def sum67(nums):
  res = 0
  canadd = True
  for i in nums:
    if i == 6:
      canadd = False
    if canadd:
      res += i
    if i == 7:
      canadd = True
  return res

def has22(nums):
  string = ""
  for i in nums:
    string += str(i)
  return True if "22" in string else False
