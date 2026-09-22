students = [
    {
        "name": "Arun Kumar",
        "dob": "15-03-2002",
        "roll_no": 101,
        "degree": "B.Sc",
        "gender": "Male",
        "course_name": "Python Programming",
        "course_code": "PY101",
        "course_duration_weeks": 12
    },
    {
        "name": "Priya Sharma",
        "dob": "22-07-2001",
        "roll_no": 102,
        "degree": "BCA",
        "gender": "Female",
        "course_name": "Data Analytics",
        "course_code": "DA201",
        "course_duration_weeks": 16
    },
    {
        "name": "Rahul Raj",
        "dob": "10-11-2002",
        "roll_no": 103,
        "degree": "B.E",
        "gender": "Male",
        "course_name": "Cloud Computing",
        "course_code": "CC301",
        "course_duration_weeks": 14
    },
    {
        "name": "Divya Priya",
        "dob": "05-01-2003",
        "roll_no": 104,
        "degree": "B.Tech",
        "gender": "Female",
        "course_name": "Machine Learning",
        "course_code": "ML401",
        "course_duration_weeks": 20
    },
    {
        "name": "Vijay Kumar",
        "dob": "18-09-2001",
        "roll_no": 105,
        "degree": "B.Sc",
        "gender": "Male",
        "course_name": "SQL and Database",
        "course_code": "SQL501",
        "course_duration_weeks": 10
    }
]

# Display student details
for student in students:
    print("Name:", student["name"])
    print("Date of Birth:", student["dob"])
    print("Roll No:", student["roll_no"])
    print("Degree:", student["degree"])
    print("Gender:", student["gender"])
    print("Course Name:", student["course_name"])
    print("Course Code:", student["course_code"])
    print("Course Duration:", student["course_duration_weeks"], "weeks")
    print("-" * 40)