# Tələbə class-ının yaradılması və listə yığılması:

student = []


class createStudent:
    def __init__(self, name, surname, email, telNumber, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.telNumber = telNumber
        self.password = password
        student.append(self.name)
        student.append(self.surname)
        student.append(self.email)
        student.append(self.telNumber)
        student.append(self.password)


# Tələbənin datalarının daxil edilmə prosesi:

n = input("Ümumi tələbə sayını daxil edin: ")
if n.isdigit():
    n = int(n)
    for i in range(0, n):
        name = input("Adınızı daxil edin: ")
        if name.isalpha():
            pass
        else:
            print("Adınızı düzgün daxil edin!")
            break

        surname = input("Soyadınızı daxil edin: ")
        if surname.isalpha():
            pass
        else:
            print("Soyadınızı düzgün daxil edin!")
            break

        email = input("Email adresinizi daxil edin: ")
        if "@" in email:
            pass
        else:
            print("Emailinizi düzgün daxil edin!")
            break

        telNumber = input("Əlaqə nömrənizi daxil edin: ")
        if telNumber.isdigit() and len(telNumber) == 9:
            pass
        else:
            print("Əlaqə nömrənizi düzgün daxil edin!")
            break

        password = input("Şifrənizi yazın: ")
        if password.isdigit() and 100 <= int(password) <= 999:
            print("Qeydiyyatınız uğurla başa çatdı!")
        else:
            print("Şifrə 3 rəqəmli ədəd olmalıdır!")
            break
        s = createStudent(name, surname, email, telNumber, password)
else:
    print("Tələbə sayı rəqəm vəya ədəd olmalıdır!")

# Tələbə adına görə tələbə məlumatlarının göstərilmə funksiyası:


def showData(student_name):
    for i in range(0, n):
        if student_name == student[5*i]:
            print(f"Student{i+1}")
            print(student[5*i])
            print(student[5*i+1])
            print(student[5*i+2])
            print(student[5*i+3])
            print(student[5*i+4])
            break
        else:
            pass
    else:
        print("Bu adda tələbə yoxdu!")


# Bütün tələbə məlumatlarının göstərilmə funksiyası:

def allData():
    for i in range(0, n):
        print(f"Student{i+1}")
        print(student[5*i])
        print(student[5*i+1])
        print(student[5*i+2])
        print(student[5*i+3])
        print(student[5*i+4])


# Tələbə koduna görə tələbə məlumatlarının dəyişdirilmə funksiyası:

def changeData(student_psw):
    for i in range(0, n):
        if student_psw == int(student[5*i+4]):
            new_name = input("Yeni adınızı daxil edin: ")
            if new_name.isalpha():
                student[5*i] = new_name
            else:
                print("Yeni adınız standartlara uyğun deyil!")
                break

            new_surname = input("Yeni soyadınızı daxil edin: ")
            if new_surname.isalpha():
                student[5*i+1] = new_surname
            else:
                print("Yeni soyadınız standartlara uyğun deyil!")
                break

            new_email = input("Yeni email adresinizi daxil edin: ")
            if "@" in new_email:
                student[5*i+2] = new_email
            else:
                print("Yeni emailiniz standartlara uyğun deyil!")
                break

            new_telNumber = input("Yeni əlaqə nömrənizi daxil edin: +994")
            if new_telNumber.isdigit() and len(new_telNumber) == 9:
                student[5*i+3] = new_telNumber
            else:
                print("Yeni əlaqə nömrəniz standartlara uyğun deyil!")
                break

            new_password = input("Şifrənizi yazın: ")
            if new_password.isdigit() and 100 <= int(new_password) <= 999:
                student[5*i+4] = new_password
                print("Qeydiyyatınız uğurla başa çatdı!")
            else:
                print("Şifrə 3 rəqəmli ədəd olmalıdır!")
                break
            showData(new_name)
            break
        else:
            pass
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")

# Tələbə koduna görə tələbə məlumatlarının silinmə funksiyası:


def deleteData(student_psw):
    for i in range(0, n):
        if student_psw == int(student[5*i+4]):
            student.pop(5*i)
            student.pop(5*i)
            student.pop(5*i)
            student.pop(5*i)
            student.pop(5*i)
            print(student)
            break
        else:
            pass
    else:
        print("Sistemdə bu kodlu tələbə yoxdur!")


# Outputda görmək istədiyiniz əmrlərin verilməsi:
for i in range(10):
    data = input('''Həyata keçirmək istədiyiniz funksionallığa uyğun rəqəmi daxil edin:
                    Hansısa tələbənin datasını əldə etmək istəyirsizsə-1
                    Bütün tələbələrin datasını əldə etmək istəyirsizsə-2
                    Hansısa tələbənin datasını dəyişmək istəyirsizsə-3
                    Hansısa tələbənin datasını sistemdən silmək istəyirsizsə-4 
                    ==>''')
    if data == "1":
        name_input = input(
            "Datasını görmək istədiyiniz tələbənin adını daxil edin: ")
        showData(name_input)
    elif data == "2":
        allData()
    elif data == "3":
        psw_input = int(
            input("Datasını dəyişmək istədiyiniz tələbənin kodunu daxil edin: "))
        changeData(psw_input)
    elif data == "4":
        psw_input = int(
            input("Datasını silmək istədiyiniz tələbənin kodunu daxil edin: "))
        deleteData(psw_input)
    else:
        print("Belə funksionallıq yoxdur!Əldə etmək istədiyiniz məlumatlara uyğun düzgün ədədi daxil edin!")