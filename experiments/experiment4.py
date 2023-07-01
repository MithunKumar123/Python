import csv

with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city to find the temperature: ")

for row in data[1:]:
    if row[0] == city:
        print(int(row[1]))