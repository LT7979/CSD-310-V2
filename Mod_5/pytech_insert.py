from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.egtm4lx.mongodb.net/"

client = MongoClient(url)

db = client.pytech

Jessie = {
    "student_id": "1007",
    "first_name": "Jessie",
    "last_name": "Pinkman",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "2.5",
            "start_date": "June 11, 2022",
            "end_date": "July 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "C-"
                }
            ]
        }
    ]

}

bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "3.52",
            "start_date": "June 11, 2022",
            "end_date": "July 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A-"
                }
            ]
        }
    ]
}

frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "1.5",
            "start_date": "June 11, 2022",
            "end_date": "July 14, 2022",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
Jessie_student_id = students.insert_one(Jessie).inserted_id
print("  Inserted student record Jessie Pinkman into the students collection with document_id " + str(Jessie_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")