n = int(input("Введите натуральное число: "))
factorial = 1
summ = 0

for i in range(1, n+1):
    factorial *= i
    summ += factorial

print(f"Сумма факториалов равна: {summ}")