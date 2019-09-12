class Address:
    def __init__(self,house_no = 0, street = 0, city="",country=""):
        self.house_no=house_no 
        self.street=street
        self.city=city
        self.country=country
    def get_full_address(self):
        return "H. No. "+str(self.house_no)+", Street "+str(self.street)+", "+str(self.city)+" "+str(self.country)
    def __str__(self):
        return self.get_full_address()

class Employee:
    def __init__(self, id=1,name=None):
        self.id=id
        self.name=name
        self.current_address=None
        self.permanent_address=None
    def set_current_address(self ,house_no, street, city, country):
        self.current_address=Address(house_no, street, city,country)
    def set_permanent_address(self,house_no, street, city,country):
        self.permanent_address=Address(house_no, street, city,country)
    def get_current_address(self):
        if self.current_address is None:
            return None
        return self.current_address.get_full_address()
    def get_permanent_address(self):
        if self.permanent_address is None:
            return None
        return self.permanent_address.get_full_address()
    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.get_permanent_address() 

class Lecturer(Employee): 
    def __init__(self):
        super().__init__(1 , "Mr. Bigshot")
    def __str__(self):
        return "Lecturer: "+super().__str__()
    

if __name__ == "__main__": 
    # Uncomment these to test out your code before run.py local 

    
    a = Address() 
    a.house_no = 2 
    a.street = 3 
    a.city = "Peshawar"
    a.country = "Pakistan"

    print(a.get_full_address())
    print(a)


    e = Employee() 
    e.set_current_address(1, 2, "Cape Town", "South Africa")
    print(e.get_current_address()) 

    e.set_permanent_address(4, 19, "Cape Town", "South Africa")
    print(e.get_permanent_address())

    print(e)

    l = Lecturer() 
    l.set_permanent_address(44, 24, "KL", "Malaysia")
    print(l.get_permanent_address())
    print(l)