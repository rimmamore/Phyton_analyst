


lst=[]
amount = 0
for number in range(1,1000):
  if number%2 != 0:
    lst.append(number**3+17)
for number_2 in lst:
  s = 0
  for count in range(len(str(number_2))):
    s += int((str(number_2)[count]))
  if s%7 == 0:
    amount += number_2
print(amount)
  

   
