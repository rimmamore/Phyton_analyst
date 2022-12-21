

for i in range(1,101):
  if i == 1 or i%10 == 1 and i > 11:
    print(i, 'процент')
  elif i < 5 or 0 < i%10 < 5  and i > 21:
    print(i, 'процента')
  else:
    print(i,'процентов')




