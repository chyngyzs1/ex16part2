numbers = []
result = []
print('vedite chislo cherez enter:')
for add in range(5):
  add = int(input())
  numbers.append(add)
print (numbers)
for x in numbers:
  if x % 2 == 0:  
    result.append(x)
print (result)