import json

stds = {
    1:{

    }
}

with open(r"D:\Data_Analytics\Python\Foundations\file_handling\std_data.json","r") as j_file:
    # student = json.load(j_file)

    # print(student["attendance"])
    # print(student["marks"]["Python"])

    student = json.dumps(stds)
    print(student)