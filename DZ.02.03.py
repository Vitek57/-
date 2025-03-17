def is_prime(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 
start = int(input("начало диапазона: ")) 
end = int(input("конец диапазона: ")) 
for i in range(start, end + 1): 
    if is_prime(i): 
        print(i)



for i in range(1, 11):
    for k in range(2, 11):  
        print(f'{i} * {k} = {i * k}\t', end='')
print('')


a = int(input('Введите начальное значение: ')) 
b = int(input('Введите конечное значение: ')) 
for i in range(a, b + 1): 
    for j in range(1, 11): 
        result = i * j 
        print(f'{i} * {j} = {result}') 
    print()
