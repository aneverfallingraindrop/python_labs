import json
from typing import List
from models import Student


def students_to_json(students: List[Student], path: str):
    with open(path, "w", encoding="utf-8") as file: 
        data = [] 
        for student in students:
            data.append(student.to_dict())
        json.dump(data, file, ensure_ascii=False, indent=2) 


def students_from_json(path: str) -> List[Student]:
    with open(path, "r", encoding="utf-8") as file: 
        data = json.load(file)
        student_list = []
        for i in data:
            student_list.append(Student.from_dict(i))
        return student_list

if __name__ == "__main__":
    students_list = [
        Student(fullname="Карчов И.И.", birthdate="2007-03-19", group="РВ-11", gpa=4.5),
        Student(fullname="Алтун А.А.", birthdate="2004-05-10", group="РПК-12", gpa=3.2),
        Student(fullname="Смирнов К.К.", birthdate="1995-11-18", group="КК-ТР-13", gpa=5.0)
    ]

    students_to_json(students_list, "./data/lab08/students_input.json")

    loaded_students = students_from_json("./data/lab08/students_output.json")

    for students in loaded_students: 
        print(students)