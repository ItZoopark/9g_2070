print("Hello World!") # операция вывода на экран
name = input("Введите ваше имя: ") # команда ввода данных
# print("Привет, ", name, "!")
print(f"Привет, {name}!")
# int - целочисленный тип данных
weight = int(input("Введите ваш вес (кг): ")) # конвертация в число
height = int(input("Введите ваш рост (см): ")) / 100
bmi = weight / (height**2) # bmi = weight / (height * height)
print(f"Ваш индекс массы тела: {bmi}")
