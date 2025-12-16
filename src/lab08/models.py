from dataclasses import dataclass
from datetime import *


@dataclass # generates class methods automatically
class Student:
    fullname: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try: 
            dt_obj = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError as exception:
            raise ValueError(f"Date format error: {self.birthdate}: must be 'YYYY-MM-DD'") from exception
            
        if not (0 <= self.gpa <= 5):
            raise ValueError("Grade point average must be between 0 and 5.")
    
    def age(self) -> int: 
        birthday = datetime.strptime(self.birthdate, "%Y-%m-%d").date() 
        today = date.today()
        return today.year - birthday.year - int((today.month, today.day) < (birthday.month, birthday.day)) 

    def to_dict(self) -> dict:
        return {
            "fullname": self.fullname,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fullname=data["fullname"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )

    def __str__(self):
        return f"{self.fullname}, group {self.group}, GPA {self.gpa:.2f}, age {self.age()} years."