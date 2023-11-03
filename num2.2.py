def analyze_data(data):
    if type(data) == list:
        first_zero = data.index(0)
        second_zero = data.index(0, first_zero+1)
        return sum(data[first_zero + 1:second_zero])
    elif type(data) == tuple:
        max_elem = max(data)
        min_elem = min(data)
        new_tuple = data[:data.index(max_elem)] + (min_elem,) + data[data.index(max_elem)+1:data.index(min_elem)] + (max_elem,) + data[data.index(min_elem) + 1:]
        return new_tuple
    elif type(data) == int:
        even_sum = 0
        for digit in str(data):
            if int(digit) % 2 == 0:
                even_sum += int(digit)
        return even_sum
    elif type(data) == str:
        result = ""
        for char in data:
            result += str(ord(char)) + " "
        return result
    else:
        return "Неизвестный тип данных"


data = input("Введите данные для анализа: ")
result = analyze_data(data)
print(result)
