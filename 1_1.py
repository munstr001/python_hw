temperature = float(input("Введите температуру в градусах Цельсия: "))
print(f"{temperature}°C = {round((temperature * 9/5) + 32, 2)}°F\n"
      f"{temperature}°C = {round(temperature + 273.15, 2)}K")
