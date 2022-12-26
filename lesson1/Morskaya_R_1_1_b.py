
lst_duration = [53, 153, 4153]
for num in lst_duration:
  if num<60:
    print(num,'сек')
  elif num<3600:
    print(num//60,'мин', num%60,'сек')
  elif num<86400:
    print(num//3600, 'час', num%3600//60, 'мин', num%3600%60, 'сек')
  else:
    print(num//86400, 'дн', num%86400//3600, 'час', num%86400%3600//60, 'мин', num%86400%3600%60, 'сек')