# ct = 3
# while ct >= 0:
#     std = input("Enter your name:")
#     ct -= 1

file = open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt","r")
print(file.read())

with open (r"D:\Data_Analytics\Python\Foundations\file_handling\std_detail.txt","r") as file:
    content =file.read()
    print(content)
