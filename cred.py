class User():
    def __init__(self, email, phone, fname, lname, addr, city, zipCode, state, cardNum):
        self.email = email
        self.phone = phone
        self.fname = fname
        self.lname = lname
        self.addr = addr
        self.city = city
        self.zip = zipCode
        self.state = state
        self.cardNum = cardNum


email = input("Email address for updates: ")
phone = input("Phone number, no dashes, no spaces: ")
fname = input("First name: ")
lname = input("Last name: ")
address = input("Address, ex 3070 Nvidia Drive: ")
city = input("City: ")
zipcode = input("Zip code: ")
state = input("State(2 letter code): ")
cardnumber = input("Credit card number: ")

User = User(email, phone, fname, lname, address, city, zipcode, state, cardnumber)


#User = User("human@gmail.com", "1234567890", "Ban", "Ironic", "1601  Tenmile Road", "Reading", "01867", "MA", "123456789")