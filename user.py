class User:
    def __init__(self, id, first_name, last_name, phone,email, role):
        self.id= id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.role=role
    def user_info(self):
        return self.first_name, self.last_name, self.email ,self.phone,self.role
    def user_role(self):
        return self.role

class Client(User):
    def __init__(self, id, first_name, last_name, phone,email):
        super().__init__(id, first_name, last_name, phone,email,role="Client")
        self.history=[]

class Employee(User):
    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Employee")

class Admin(User):
    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Admin")






