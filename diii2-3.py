a = input("Введите пароль")
b = input("Введите пароль ещё раз")

if a == b:
    print ("Пароль принят")
else:
    print("Пароль не принят")


# 2.2
def determine_seat_type(seat_number):
    seat_type = "верхнее" if seat_number % 2 == 0 else "нижнее"
    side = "боковое" if seat_number % 4 in [0, 1] else "вкупе"

    return f"Место {seat_number} - {seat_type}, {side}"


seat_number = int(input("Введите номер места: "))
result = determine_seat_type(seat_number)
print(result)


#2.3
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"Год {year} - високосный")
    else:
        print("Этот год не високосный")

user_year = int(input("Введите год: "))
check_leap_year(user_year)


#2.4
def mix_colors(color1, color2):
    if (color1 == 'красный' and color2 == 'синий') or (color1 == 'синий' and color2 == 'красный'):
        return 'фиолетовый'
    elif (color1 == 'красный' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'красный'):
        return 'оранжевый'
    elif (color1 == 'синий' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'синий'):
        return 'зеленый'
    else:
        return 'Ошибка! Введите корректные названия основных цветов.'

color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

result = mix_colors(color1, color2)


#3.1
n = int(input("Введите количество слов: "))

result = ""

for i in range(n):
    word = input("Введите слово: ")
    result += word + " "

print("Результат:", result.strip())

# 3.2
result = ""

while True:
    word = input("Введите слово,либо 'stop' для завершения: ")

    if word.lower() == "stop":
        break

    result += word + " "

print("Результат:", result.strip())


#3.3
word = input("Введите слово: ")

if 'ф' in word.lower():
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово…")

# 3.4
import random

correct_answers = 0
wrong_answers = 0

while wrong_answers < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = input(f"{num1} + {num2} = ")

    if int(answer) == num1 + num2:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        wrong_answers += 1

print(f"Игра кончена. Правильных ответов: {correct_answers}")