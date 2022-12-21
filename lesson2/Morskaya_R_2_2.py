
lst_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst= []
for i in range(len(lst_1)):
  if i == 1 or i == 3:  
    lst.extend(['"', '{:02}'.format(int(lst_1[i])), '"'])
  elif i == 8:
    lst.extend(['"', '+'+'{:02}'.format(int(lst_1[i])), '"'])
  else:
    lst.append(lst_1[i])

lst_2 = ' '.join(lst[0:2]) + ''.join(lst[2:3]) + ' '.join(lst[3:6]) + ''.join(lst[6:7]) + ' '.join(lst[7:13]) + ''.join(lst[13:14]) + ' '.join(lst[14:16])    

print(lst_2)



