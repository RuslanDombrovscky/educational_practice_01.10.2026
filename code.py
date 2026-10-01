def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

data = [1, 2, 3, 4, 5]
result = calculate_sum(data)
print(f"Sum is: {result}")
