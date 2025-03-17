numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(a)
def prod(val) : 
    res = 1
    for ele in val: 
        res *= ele 
    return res 
res = prod(map(lambda i : i * i, a))
print ("производное: " + str(res)) 



a = [10, 15, 7, 3, 29, 12]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def find_primes(array):
    return list(filter(is_prime, array))
print(find_primes(a))
number=max(a)
print(number)
 


def filter_odd_numbers(input_list): 
    return [number for number in input_list if number % 2 != 0] 
numbers = [10, 15, 7, 3, 29, 12] 
number = filter_odd_numbers(numbers) 
print(number)
kub = sum(x**3 for x in number)  
print(kub)
