def calculate_average(numbers):
    if len(numbers) == 0:
        return None  # защита от деления на ноль
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)  # исправлено: используем numbers вместо number
    return avg

data = [10, 20, 30]
result = calculate_average(data)
if result is not None:
    print(f"Среднее значение: {result}")  # исправлено: f-строка вместо конкатенации
else:
    print("Список пуст, среднее значение не определено.")
