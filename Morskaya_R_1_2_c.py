

lst=[]
amount = 0
for number in range(1,1000):
  if number%2 != 0:
    str_1=str(number**3+17)
    s = 0
    for count in range(len(str_1)):
      s += int(str_1[count])
    if s%7 == 0:
      amount += number**3+17
print(amount)
   
