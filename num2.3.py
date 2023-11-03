matrix = []
while True:
    lines = input("Введите количество сток в матрице: ")
    try:
        lines = int(lines)
        if lines <= 0:
            print("Число должно быть положительным!")
        else:
            break
    except ValueError:
        print("Вы ввели не число!")

while True:
     columns = input("Введите количество столбцов в матрице: ")
     try:
         columns = int(columns)
         if columns <= 0:
              print("Число должно быть положительным!")
         else:
              break
     except ValueError:
         print("Вы ввели не число!")

for i in range(lines):
    line = []
    for j in range(columns):
        while True:
            try:
                element = int(input(f"Введите элемент матрицы [{i}][{j}]: "))
                line.append(element)
                break
            except ValueError:
                print("Вы ввели не число!")
    matrix.append(line)

for line in matrix:
    if line == sorted(line):
        line.reverse() # с помощью метода reverse элементы строки становятся в обратном порядке
        break

print("Изменённая матрица: ")
for line in matrix:
    print(line)
