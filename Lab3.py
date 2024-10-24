def min_breaks(n,m):
    if n == 1 and m == 1: return 0
    elif n == 1: return m - 1
    elif m == 1: return n - 1
    else: 
        horizon = 1+min_breaks(n-1,m)
        vertic = 1+min_breaks(n,m-1)
        return n*m-1
n,m = int(input()), int(input())
print(min_breaks(n,m))

print('Проверка тестов')
print(min_breaks(2, 3))  # Должно вывести 5
print(min_breaks(3, 3))  # Должно вывести 8
print(min_breaks(1, 1))  # Должно вывести 0