def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return totall  # ошибка: опечатка в имени переменной (totall вместо total)

data = [1, 2, 3, 4, 5]
result = calculate_sum(data)
print("Sum is: " + result)  # ошибка: нельзя конкатенировать строку и число
