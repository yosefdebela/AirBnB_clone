import testbasemodel
class User(testbasemodel.BaseModel):
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

yosef = User('yosefalemu@gmail.com', '123456','Yosef', 'Alemu')
print(f"{yosef.__dict__}")
print(yosef.id)
yosef.save()