
x = input('Введите слово ')
if x[0] == 'а' or x[0] == 'э' or x[0] == 'е' or x[0] == 'я':
  for i in range(0,len(x)):
    print(x[i])
else:
  for i in range(len(x),0):
    print(x[i])
