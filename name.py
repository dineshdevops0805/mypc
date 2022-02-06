class Name:
    name=None
    age=None
    def get_name(self):
        print("enter ur name: ")
        self.name=input()

    def get_age(self):
        print("enter ur age: ")
        self.age=input()

    def put_name(self):
        print("Your name is : ",self.name)

    def put_age(self):
        print("Your age is : ",self.age)
        
name1 = Name()
name1.get_name()
name1.get_age()
name1.put_name()
name1.put_age()
