import csv

with open(r"D:\Data_Analytics\Python\Foundations\file_handling\data.csv", "a", newline="") as file:
    # reader = csv.reader(file)
    # for row in file:
    #     print(row)
    # print(file)

    # reader = csv.DictReader(file)
    # for row in reader:
    #     print(row["Dept"])


    # writer = csv.writer(file)
    # writer.writerow(["Ram","CDF"])
    # print()


    data = [
    {"name": "John", "age": 25, "city": "Chennai"},
    {"name": "David", "age": 30, "city": "Coimbatore"},
    {"name": "Ravi", "age": 28, "city": "Erode"}
    ]


    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age", "city"]
    )

    writer.writeheader()
    writer.writerows(data)
    