summ = 0
N = int(input("Введите кол-во целых чисел: "))
for _ in range(N):
    a = int(input())
    summ = summ + a
print(f"Ответ: {summ}")