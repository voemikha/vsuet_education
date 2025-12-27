def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


num = int(input("Введите число: "))

if num <= 0:
    print("Число должно быть больше 0!")
else:
    factor = factorial(num)
    print(f"{num}! = {factor}")
