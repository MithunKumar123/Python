date = input("Enter today's date: ")
mood = input("Rate your mood today from 1 to 10: ")
thoughts = input("Write the thoughts of the day:\n")

with open(f"../files/{date}.txt", "w") as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)
