password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digits = False
for i in password:
    if i.isdigit():
        digits = True
result["digits"] = digits

upperCase = False
for i in password:
    if i.isupper():
        upperCase = True
result["upperCase"] = upperCase

print(result)

if all(result.values()):
    print("Strong Password...")
else:
    print()