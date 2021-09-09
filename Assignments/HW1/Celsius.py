# Prompting user for celsius value -> float
celsius = float(input("Enter temperature in celsius: "))

# Conversion from celsius to fahrenheit
fahrenheit = (9/5)*celsius+32

# Showing conversion from original celsius value to calculated fahrenheit
# \xb0 adds the degree symbol as a character
print(f"{celsius}\xb0C -> {fahrenheit}\xb0F")
