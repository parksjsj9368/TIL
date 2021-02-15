a = '123'
print(a)
print(a.replace('1','*').replace('2','1').replace('*','2'))

table = str.maketrans('12','21')
print(a.translate(table))