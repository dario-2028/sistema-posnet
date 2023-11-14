class CardHolder:
    def __init__(self, DNI, name, lastName, phone, email):
        self.DNI = DNI
        self.name = name
        self.lastName = lastName
        self.phone = phone
        self.email = email

    def getDNI(self):
        return self.DNI

    def setDNI(self, DNI):
        self.DNI = DNI

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def __str__(self):
        return f"CardHolder [DNI: {self.DNI}, Name: {self.name}, Last Name: {self.lastName}, Phone: {self.phone}, Email: {self.email}]"

