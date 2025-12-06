def say_goodbye(name):
    print("Goodbye,", name)


def area_of_circle(radius):
    area = 3.14 * radius * radius
    print(area)


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def min_max_temps(temperatures):
    minimum = min(temperatures)
    maximum = max(temperatures)
    return (minimum, maximum)


def is_weekend_number(day):
    return day == 6 or day == 7


def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used


def secret_code(n):
    s = str(n)
    if len(s) <= 1:
        return n
    shifted = s[-1] + s[:-1]
    return int(shifted)


def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result


def min_for(values):
    current_min = values[0]
    for v in values[1:]:
        if v < current_min:
            current_min = v
    return current_min


def max_for(values):
    current_max = values[0]
    for v in values[1:]:
        if v > current_max:
            current_max = v
    return current_max


def min_while(values):
    index = 0
    current_min = values[0]
    while index < len(values):
        if values[index] < current_min:
            current_min = values[index]
        index += 1
    return current_min


def max_while(values):
    index = 0
    current_max = values[0]
    while index < len(values):
        if values[index] > current_max:
            current_max = values[index]
        index += 1
    return current_max


def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


x = 2
y = 3
result = power(x, y)

print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")
