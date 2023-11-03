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
        finally:
            print("end")
