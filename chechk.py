class Telebe:
    def __init__(self, fname, lname, email, password, p_number):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.password = password
        self.phone_number = p_number

    def full_data(self):
        print(self.first_name, self.last_name, self.email,
              self.password, self.phone_number)


user_number = input("Enter user number : ")
if user_number.isdigit():
    user_number = int(user_number)
    for Telebe in range(0, user_number):
        fname = input("Enter your name : ")
        last_name = input("Enter your surname : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        if password.isdigit() and 1000 > int(password) > 99:
            print(password)
        else:
            print("Adam balasi kimi sifre daxil et ay cahil")
    else:
        print("you have not entered a number")
