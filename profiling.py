class Profiling:
    '''This class represents a person's profile'''
    def __init__(self, pName):
        self.name = pName
        self.address = ''
        self.phone = ''
        self.gender = ''
        self.height = ''
        self.weight = ''

    def addAddress(self, addr):
        #add address
        self.address += str(addr)

    def addPhone(self, num):
        #add phone number
        self.phone += str(num)

    def addGender(self, gen):
        #add gender
        self.gender += str(gen)

    def addHeight(self, height):
        #add height
        self.height += str(height)

    def addWeight(self, weight):
        #add weight
        self.weight += str(weight)

    def profile(self):
        '''
        self.d = {}
        self.d[self.name] = ("Address: " + self.address + "\n" + "Phone: " + self.phone + "\n" + "Gender: " + self.gender + "\n" + "Height: " + self.height + "\n" + "Weight: " + self.weight + "\n")
        return self.d
        '''
        print("Name: " + self.name)
        print("Address: " + self.address)
        print("Phone: " + self.phone)
        print("Gender: " + self.gender)
        print("Height: " + self.height)
        print("Weight: " + self.weight)
        
