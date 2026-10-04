# ct = 3
# while ct >= 0:
#     std = input("Enter your name:")
#     ct -= 1

# Read the file
# file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt","r")
# print(file.read())

# with open (r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt","r") as file:
#     content =file.read()
#     print(content)

# file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt","r")
# print(file.read())

# with open (r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt","w") as file:
#     file.write("raj")
#     content = file.read
#     print(content)


# Read function
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "r")

data = file.read()
print(data)

file.close()

# How many character you want to read
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "r")

data = file.read(5)
print(data)

file.close()


# Readline Function
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "r")

line = file.readline()
print(line)

file.close()


# Readlines Function
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "r")

lines = file.readlines()
print(lines)

file.close()


# # Readline Function in list
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "r")

lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()


# Write Function
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "w+")

file.write("Fruites")
file.seek(2)
print(file.read())

file.close()


# # Writelines Function in list
file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt", "w+")

lines = ["Apple\n", "Banana\n", "Orange\n"]

file.writelines(lines)
file.seek(0)
print(file.read())

file.close()