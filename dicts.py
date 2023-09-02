# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

city_tepperature = {"city": "Москва", "temperature": "20"}
print(city_tepperature["city"])
city_tepperature["temperature"] = int(city_tepperature["temperature"]) - 5
print(city_tepperature)

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря

print(city_tepperature.get("country"))
print(city_tepperature.get("country", "Россия"))
city_tepperature["date"] = "27.05.2019"
print(len(city_tepperature))
print(city_tepperature)