n = int(input("Введите максимальный номер карты: "))
lst = []
missing_card = 0

for _ in range(n - 5):
    a = int(input("Введите число: "))
    if a >= 5 and a not in lst:
        lst.append(a)
    else:
        print("Ошибка")
        break
lst = sorted(lst)

for i in range(len(lst) - 1):
    if lst[i] + 1 != lst[i + 1]:
        missing_card = lst[i] + 1
        break

print(f"Номер пропавшей карты: {missing_card}")


        
