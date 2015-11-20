class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor Called")
        self.lastname=last_name
        self.eye_color = eye_color

    def showinfo(self):
        print("Last Name -"+self.lastname)
        print("Eye Color -"+self.eye_color)
class Child(Parent):
    def __init__(self,last_name,eye_color,toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.toys=toys
    def showinfo(self):
        print("Last Name -"+self.lastname)
        print("Eye Color -"+self.eye_color)
        print("Toys -"+str(self.toys))


billy = Parent("Bahadur","Blue")
billythekid = Child("Bahadur","Blue",69)
print(billy.lastname)
print(billythekid.toys)
billythekid.showinfo()
