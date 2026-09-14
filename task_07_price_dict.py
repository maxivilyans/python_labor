# Задача 7: Прайс-лист материалов

# Создание словаря
materials = {
    "Газобетон": 1200,
    "Бетон": 2000,
    "ЦПС": 800,
    "Гипс": 320,
    "Песок": 450
}

# Вывод
print("Исходный список материалов:")
for name, price in materials.items():
    print(name, "-", price, "руб")

    # Добавление новых материалов
materials["Щебень"] = 400
materials["Битум"] = 200

# Изменение цены (+10%)
materials["Газобетон"] = materials["Газобетон"] * 1.1

print("\nПосле изменений:")
for name, price in materials.items():
    print(name, "-", round(price, 2), "руб")

    # Удаление одного материала
materials.pop("Гипс")

# Расчет средней цены
average_price = sum(materials.values()) / len(materials)

print("\nПосле удаления:")
for name, price in materials.items():
    print(name, "-", round(price, 2), "руб")

print("\nСредняя цена:", round(average_price, 2), "руб")