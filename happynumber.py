n=input()
original =n

while len(n)>1:
  lst =list(n)
  m=0
  for i in lst:
    m += (int(i))**2
  n = str(m)

if n == '1':
  print(original + "is a happy number")
else:
  print(original + "is not a happy number")
