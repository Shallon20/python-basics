class Criminal:
    def __init__(self, name, id_number, crime, gender):
        self.name = name
        self.id_number = id_number
        self.crime = crime
        self.gender = gender

    def show_details(self):
        print(f"Name : {self.name} \n ID : {self.id_number} \n Issue : {self.crime} \n Gender : {self.gender}")


c1 = Criminal("John Dukes", "2444555", "Stealing power cables", "Male")
c1.show_details()
