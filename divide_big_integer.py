a = "1234456432457532"
b = 43

def div(a, b):
  temp = 0
  idx = 0
  ans = []
  for i in range(len(a)):
    temp = temp * 10 + int(a[i])
    print(temp)
    if temp < b:
      ans.append(0)
      continue
    else:
      ans.append(temp // b)
      temp = temp % b
  res = "".join([str(x) for x in ans]).lstrip("0")
  
  return res
  
c = div(a, b)
