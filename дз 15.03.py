numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [i * i for i in filter(lambda x: x % 2 != 0, numbers)]
print(a)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(" ".join(list(map(str, numbers))))
