def filterEven(lst):
  even = []
  for num in lst:
    if num%2 == 0:
      even.append(num)
  return even
list1 = [1,2,3,4,5,6]
ans = filterEven(list1)
print(ans)