
lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(lst)+6):
  if i in(1,3,5,7,12,14):
    lst.insert(i, '"')
lst[2] = '0'+lst[2]
lst[13] = '+05'
  
lst_2 = ' '.join(lst[0:2]) + ''.join(lst[2:3]) + ' '.join(lst[3:6]) + ''.join(lst[6:7]) + ' '.join(lst[7:13]) + ''.join(lst[13:14]) + ' '.join(lst[14:16])    

print(lst_2);








#['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']