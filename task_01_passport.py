# Задача 1: Паспорт объекта

# Переменные
student_name = "Сулейманов Максим Эдуардович"
group_number = "3150801/10101"
project_name = "ЖК \"Соты\""
floors = 20
height = 63.2
is_residential = True
construction_year = 2024

# Вывод
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print("Составитель:", student_name)
print("Группа:", group_number)
print()
print("Объект:", project_name)
print("Этажность:", floors, "этажей")
print("Высота:", height, "м")

if is_residential:
    print("Тип: Жилой")
else:
    print("Тип: Нежилой")

print("Год постройки:", construction_year)

# Комментарий:
# Объект находится в вымышленном районе.
# Выбран ЖК, спроектированный для курсового проекта.