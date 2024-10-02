import sys
db, priceStore = [], []
print("Вписывайте список покупок")
ipt = '[]'
while ipt != '':
    ipt = sys.stdin.readline()
    ipt = ipt.rstrip()
    if ipt == '': break
    if ipt.count(',') > 0: db.append(ipt.split(','))
    else: db.append(ipt) 
# print(db)

for i in range(len(db)):
    product = db[i]
    print(f'Введите цены и магазины для {db[i]}')
    ipt = '[]'
    while  ipt != '':     
        ipt = sys.stdin.readline()
        ipt = ipt.rstrip()
        priceStore+=[i,ipt.split(',')]
# print(db)
# print(priceStore)
    
