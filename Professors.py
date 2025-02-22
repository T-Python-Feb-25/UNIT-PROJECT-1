from Person import Person
from Courses import Course
from datetime import datetime
from typing import List, Dict, Any


class Employee(Person):
    """Represents an employee with additional details like department and salary."""

    BASE_SALARY = 30000  # Base salary for all employees
    PER_COURSE_BONUS = 5000  # Bonus per course assigned

    def __init__(self, name: str, mem_id: str, dob: datetime, address: Dict[str, str], department: str) -> None:
        super().__init__(name, mem_id, dob, address)
        self.__department = department
        self.__courses: List[Course] = []
        self.__salary = self.BASE_SALARY

    def assign_course(self, course: Course) -> None:
        """Assign a course to the employee and update their salary."""
        self.__courses.append(course)
        self.__salary = self.BASE_SALARY + (len(self.__courses) * self.PER_COURSE_BONUS)

    def remove_course(self, course: Course) -> None:
        """Remove a course from the employee and update their salary."""
        if course in self.__courses:
            self.__courses.remove(course)
            self.__salary = self.BASE_SALARY + (len(self.__courses) * self.PER_COURSE_BONUS)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the employee object to a dictionary."""
        person_dict = super().to_dict()
        person_dict.update({
            "Department": self.__department,
            "Courses": [course.to_dict() for course in self.__courses],
            "Salary": self.__salary
        })
        return person_dict

    @property
    def department(self) -> str:
        return self.__department

    @property
    def courses(self) -> List[Course]:
        return self.__courses

    @property
    def salary(self) -> float:
        return self.__salary

