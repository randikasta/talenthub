suhu_celcious = 33 
# suhu_kelvin = 80 
# suhu_fahrenheit = 144 


def CelToKelvin(celcious):
  kelvin = celcious + 273.15
  return kelvin

def KelToCelcious(kelvin):
  celcious = kelvin - 273.15
  return celcious

def fahToCelcious(fahrenheit):
  celcious = (fahrenheit - 32) * 5/9
  return celcious

def CelToFahrenheit(celcious):
  fahrenheit = 9/5 * celcious + 32
  return fahrenheit

# suhu_kelvin = CelToKelvin(suhu_celcious)
# print(f"{suhu_celcious} derajat C setara dengan {suhu_kelvin} Kelvin ")

# suhu_celcious = KelToCelcious(suhu_kelvin)
# print(f"{suhu_kelvin} kelvin setara dengan {suhu_celcious} derajat C ")

# suhu_celcious = fahToCelcious(suhu_fahrenheit)
# print(f"{suhu_fahrenheit} derajat F setara dengan {suhu_celcious} derajat C ")

suhu_fahrenheit = CelToFahrenheit(suhu_celcious)
print(f"{suhu_celcious} derajat C setara dengan {suhu_fahrenheit} derajat F ")
