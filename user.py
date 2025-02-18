class User:
    def __init__(self, id, fisrt_name, second_name, phone,email, role="client"):
        self.id= id
        self.first_name=fisrt_name
        self.last_name=second_name
        self.phone=phone
        self.email=email
        self.role=role
    


class Employee(User):
    def __init__(self):
        super().__init__()
        pass


class Client(User):
    def __init__(self):
        super().__init__()
        pass


