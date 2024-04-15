city_dict = {
    "Москва": 0,
    "Санкт-Петербург": 500,
    "Магнитогорск": 1690,
    "Красноярск": 4200,
    "Анапа": 1530,
    "Нижний Новгород": 470,

}
keys_str = ", ".join(city_dict.keys())
print("Все города: " + keys_str)
print("Выберите город:")
while True:
    city = input()
    if city in city_dict:
        distance = city_dict[city]
        print(f"Расстояние от Москвы до {city}: {distance} км")
        break
    else:
        print("Такого города нет в словаре. Попробуйте снова.")
