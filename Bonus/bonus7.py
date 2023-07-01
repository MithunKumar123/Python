def get_average():
    with open("../files/temperature.txt", "r") as local_file:
        data = local_file.readlines()
    value_local = data[1:]
    value_local = [float(x) for x in value_local]

    average_local = sum(value_local)/len(value_local)
    return average_local

average = get_average()
print(average)