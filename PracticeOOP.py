class Student():
    def __init__ (self, name, age,address, gwa):
        self.name= name
        self.age=age
        self.address= address
        self.gwa=gwa
    def Show(self):
        print("Hi I am",self.name,self.age,"years old","I live in",self.address,"my grade is",self.gwa)

raizen= Student("Raizen Sangalang", 13,"Anunas",96)
raizen.Show()