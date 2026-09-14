# Задача 6: Каталог материалов

# Создание списка из 5 материалов (новые)
materials = ["Газобетон", "Бетон", "ЦПС", "Гипс", "Песок"]

# НОВОЕ — вывод всего списка
print("\n=== СПИСОК МАТЕРИАЛОВ ===")
for material in materials:
    print("-", material)

# Вывод элементов
print("\nПервый материал:", materials[0])
print("Последний материал:", materials[-1])
print("Средние материалы:", materials[1:-1])

# Добавление новых материалов
materials.append("Щебень")
materials.append("Битум")

print("\nПосле добавления:", materials)

# Удаление второго элемента
materials.pop(1)

# Итог
print("\nИтоговый список:", materials)
print("Количество материалов:", len(materials))