def merge_sort(nums):
  if len(nums) <= 1:
    return nums
    
  mid = len(nums) // 2
  l = merge_sort(nums[:mid])
  r = merge_sort(nums[mid:])
  i = j = 0
  result = []
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      result.append(l[i])
      i += 1
    else:
      result.append(r[j])
      j += 1

  result.extend(l[i:])
  result.extend(r[j:])

  return result

nums = [3,7,8,5,1]
result = merge_sort(nums)
print(result)
# [1, 3, 5, 7, 8]

target = 8
left = 0
right = len(result) - 1

while left <= right:
  mid = (left + right) // 2
  if result[mid] == target:
    print(mid)
    break
  elif result[mid] < target:
    left = mid + 1
  else:
    right = mid - 1

  
