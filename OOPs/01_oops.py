class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


Harry = Programmer("Harry", "Skype")
Alka = Programmer("Alka", "Github")
Harry.getInfo()
Alka.getInfo()