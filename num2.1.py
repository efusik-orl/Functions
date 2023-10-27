def find_divisors():
    while True:
        number = input("Введите положительное число: ")
        try:
            number = int(number)
            if number <= 0:
                print("Число должно быть положительным!")
            else:
                break
        except ValueError:
            print("Вы ввели не число!")

    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    print("Числа на которые без остатка делится", number, ":", divisors)

find_divisors()
