import sys

def Inputing(db):
    line = '[]'
    while line != '':
        line = sys.stdin.readline()
        line = line.rstrip()
        if line == '': break
        if line.count(',') > 0: db.append(line.split(','))
        else: db.append(line)
    return db

items, store = [], []
print("#Для перехода к следующему этапу отправьте пустую строку, записывайте копейки через точку#")
print("Введите список покупок")
items = Inputing(items) 
print('Введите магазины в которых вы хотите закупиться')
store = Inputing(store)
ans = []
for numStore in range(len(store)):
    print(f'Напишите цены в маназине "{store[numStore]}" для: ')
    price = 0
    for item in range(len(items)):
        price += float(input(f'{items[item]}: '))
    ans += [[price, store[numStore]]]
for i in range(len(ans)):
    print(f'{ans[i][1]}:{ans[i][0]:.2f} рублей')
ans.sort(key=lambda x: x[0])
print(f"Я вам советую закупить ваши товары в магазине {ans[0][1]}, ведь вы потратите {ans[0][0]:.2f} рублей")
    
