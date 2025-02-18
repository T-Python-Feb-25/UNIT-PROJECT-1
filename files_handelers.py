from Person import Person
import json
import os


class FilesHandlers(Person):

    def __int__(self, file_name):
        self.__file_name = file_name

    def add_to_file(self, file_name: str):
        records = self.read_records(file_name)
        if file_name == "Students.jason":
            for record in records:
                if record["ID"] == self.__student_id:
                    print("This student already exist")
                    return

            records.append({
                    "StudentID": self.__per_id,
                    "name": self.__name,
                    "DOB": self.__dob,
                    "Address": self.get_address(),
                    "Number_of_courses": self.__number_of_course,
                    "Registered_Courses": self.registerd_courses(),
                    "Account_balance": self.__account_balance

            })
            self._write_records_file(records, file_name)
        elif file_name == "Professors.jason":
            for record in records:
                if record["ID"] == self.__prof_id:
                    print("This professor already exist")
                    return
            records.append({
                        "Professor_ID": self.__prof_id,
                        "name": self.__name,
                        "DOB": self.__dob,
                        "Address": self.get_address(),
                        "Number_of_courses": self.__number_of_teaching_course,
                        "Salary": self.get_salary()
            })
            self._write_records_file(records, file_name)
        elif file_name == "courses.jason":
            for record in records:
                if record["CRN"] == self.__crn:
                    print("This course already exist")
                    return
            records.append({
                        "CRN": self.__crn,
                        "course_name": self.__course_name,
                        "Starting_date": self.__start_date,
                        "End_date": self.__end_date,
                        "Starting_time": self.__start_time,
                        "End_time": self.__end_time,
                        "Price_per_class": self.__price_per_class,
                        "Number_of_students": self.__number_of_students

                })
            self._write_records_file(records, file_name)

        # To update the Accounts after running the intended function then send the
        # updated file to the write_accounts_file
        def _update_records_in_file(file_name: str):
            self.file_name = file_name
            records = self._read_record_files(file_name)
            for record in records:
                if record["Professor_ID"] == self.__crn:
                    record["course_name"] = self.__course_name
                    record["Starting_date"] = self.__start_date
                    record["End_date"] = self.__end_date
                    record["Starting_time"] = self.__start_time
                    record["Price_per_class"] = self.__price_per_class
                    record["Number_of_students"] = self.__number_of_students
                    break
                if record["StudentID"] == self.__per_id:
                    record["name"] = self.__name
                    record["DOB"] = self.__dob
                    record["Address"] = self.get_address()
                    record["Number_of_courses"] = self.__number_of_course
                    record["Registered_Courses"] = self.registerd_courses()
                    record["Account_balance"] = self.__account_balance
                    break
                if record["Professor_ID"] == self.__per_id:
                    record["name"] = self.__name
                    record["DOB"] = self.__dob
                    record["Address"] = self.get_address()
                    record["Number_of_courses"] = self.__number_of_teaching_course
                    record["Salary"] = self.get_salary()
                    break
                self._write_records_file(records)

        # To retrieve the Account information then load it into a set
        def _read_record_files(file_name):
            if not os.path.isfile(f"{file_name}"):
                return []
            with open("balance.json", "r", encoding="UTF-8") as f:
                try:
                    return [json.loads(line) for line in f]
                except json.JSONDecodeError:
                    return []

        # To upload the accounts information into the json file called "balnce.json"
        def _write_records_file(self, records, file_name):
            with open(f"{file_name}", "w", encoding="UTF-8") as f:
                for record in records:
                    f.write(json.dumps(record) + "\n")

        # To get the last account number uploaded to the file then add 1 to it then assign the new number to the new account
        def assign_id_number(file_name):
            records = self.__read_record_files(file_name)
            if file_name == "Students.json":
                if records:
                    student_records = [int(self.per_id["StudentID"]) for student_record in records]
                    last_student_id_number = max(self.__per_id)
                    return str(last_student_id_number + 1)
                return "3025463290"  # Starting account number
            records = self.__read_record_files(file_name)
            if file_name == "Professors.json":
                if records:
                    professor_records = [int(self.per_id["Professor_ID"]) for professor_records in records]
                    last_professor_id_number = max(self.__per_id)
                    return str(last_professor_id_number + 1)
                return "1025463290"  # Starting account number

            if file_name == "courses.jason":
                if records:
                    course_records = [int(self.per_id["CRN"]) for course_records in records]
                    last_crn = max(self.__per_id)
                    return str(last_crn + 1)
                return "2025463290"  # Starting account number
