import converters, parsers

feet_inches = input("Feet and Inches: ")


parsed = parsers.parse(feet_inches)
result = converters.convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")
if result < 1:
    print("Kid is too small!!!")
else:
    print("Play and enjoy the slide:)")
