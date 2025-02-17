from Student import Student
from Person import Person
class FilesHandelers(Student, Person):
    def __int__(self, file_name):
        self.file_name = file_name

    def choose_file(self,file_name):
        if file_name == "Students.jason":
            file_name = "Students"
        elif file_name == "Professors.jason":
            file_name = "Professors"
        elif file_name == "courses.jason":
            file_name = "courses"
        else:
            print("File Not found")
        return file_name


        def add_to_file(self, file_name):
            records = self.read_records(file_name)
            file_name = self.choose_file(self, file_name)
            if file_name == "Students":
                for record in records:
                    if record["ID"] == self.__student_id:
                        print ("This student already exist")
                        return
                records.append({
                    "StudentID" : self.__student_id,
                    "name" : self.__name,
                    "DOB" :self.__dob,
                    "Address" : self.get_address(),
                    "Number_of_courses": self.__number_of_course,
                    "Regestered_Courses": self.registerd_courses(),
                    "Account_balance" : self.__account_balance

                })




        # To update the Accounts after running the intended function then send the updated file to the write_accounts_file
        def _update_account_in_file(self):
            accounts = self._read_accounts_file()
            for account in accounts:
                if account["account_number"] == self.__account_number:
                    account["name"] = self.__account_holder
                    account["balance"] = self.__balance
                    break
            self._write_accounts_file(accounts)

        # To retrieve the Account information then load it into a set
        def _read_files(self):
            if not os.path.isfile("balance.json"):
                return []
            with open("balance.json", "r", encoding="UTF-8") as f:
                try:
                    return [json.loads(line) for line in f]
                except json.JSONDecodeError:
                    return []

        # To upload the accounts information into the json file called "balnce.json"
        def _write_accounts_file(self, accounts):
            with open("balance.json", "w", encoding="UTF-8") as f:
                for account in accounts:
                    f.write(json.dumps(account) + "\n")

        # To get the last account number uploaded to the file then add 1 to it then assign the new number to the new account
        def assign_account_number(self):
            accounts = self._read_accounts_file()
            if accounts:
                # Extract account numbers and convert to integers
                account_numbers = [int(account["account_number"]) for account in accounts]
                last_account_number = max(account_numbers)
                return str(last_account_number + 1)
            return "1025463290"  # Starting account number