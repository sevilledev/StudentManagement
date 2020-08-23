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
        while True:
            name = input("Adınızı daxil edin: ")
            if name.isalpha():
                break
            else:
                print("Adınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")

        while True:
            surname = input("Soyadınızı daxil edin: ")
            if surname.isalpha():
                break
            else:
                print("Soyadınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")

        while True:
            email = input("Email adresinizi daxil edin: ")
            if "@" in email:
                break
            else:
                print("Düzgün email adresi daxil edin!")

        while True:
            telNumber = input("Əlaqə nömrənizi daxil edin: +994")
            if telNumber.isdigit() and len(telNumber) == 9:
                break
            else:
                print("Əlaqə nömrəniz 9 rəqəmli olmalıdır!(nümunə:501234567)")

        while True:
            password = input("Şifrənizi yazın: ")
            if password.isdigit() and 100 <= int(password) <= 999:
                print("Qeydiyyatınız uğurla başa çatdı!")
                break
            else:
                print("Şifrə 3 rəqəmli ədəd olmalıdır!")
                
        print("Tələbələrin datalarının sistemə yerləşdirilmə prosesi sona çatdı!")
        s = createStudent(name, surname, email, telNumber, password)
else:
    print("Tələbə sayı rəqəm vəya ədəd olmalıdır!")
    
print("Tələbələrin datalarının sistemə yerləşdirilmə prosesi sona çatdı!")

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
            while True:
                new_name = input("Yeni adınızı daxil edin: ")
                if new_name.isalpha():
                    student[5*i] = new_name
                    break
                else:
                    print("Yeni adınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")

            while True:
                new_surname = input("Yeni soyadınızı daxil edin: ")
                if new_surname.isalpha():
                    student[5*i+1] = new_surname
                    break
                else:
                    print("Yeni soyadınızda ancaq əlifbanın hərflərindən istifadə edə bilərsiz!")

            while True:
                new_email = input("Yeni email adresinizi daxil edin: ")
                if "@" in new_email:
                    student[5*i+2] = new_email
                    break
                else:
                    print("Yeni emailiniz standartlara uyğun deyil!")

            while True:
                new_telNumber = input("Yeni əlaqə nömrənizi daxil edin: +994")
                if new_telNumber.isdigit() and len(new_telNumber) == 9:
                    student[5*i+3] = new_telNumber
                    break
                else:
                    print("Yeni Əlaqə nömrəniz 9 rəqəmli olmalıdır!(nümunə:501234567)")

            while True:
                new_password = input("Şifrənizi yazın: ")
                if new_password.isdigit() and 100 <= int(new_password) <= 999:
                    student[5*i+4] = new_password
                    print("Qeydiyyatınız uğurla başa çatdı!")
                    break
                else:
                    print("Şifrə 3 rəqəmli ədəd olmalıdır!")

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
            n=n-5
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
        elif data == "2":
        secret_psw=int(input("4-rəqəmli gizli şifrəni daxil edin: "))
        while True:
            if secret_psw==2005:
                allData()
                break
            else:
                print("Yalnış şifrə!") 
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
