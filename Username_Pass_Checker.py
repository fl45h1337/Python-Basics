while True:
    usr = input("Enter Username : ")
    with open("users.txt","r") as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]

    if usr in users:
        print("Username exists!")
        continue
    else:
        print("Username not found!")
        break

while True:
    notes = []
    print("Enter Password : ")
    psw = input()
    if not any(i.isdigit() for i in psw):
        notes.append("You need atleast one number.")
    if not any(i.isupper() for i in psw):
        notes.append("You need atleast one uppercase letter.")
    if len(psw) < 5:
        notes.append("Minimum length is 5.")
    if len(notes) == 0:
        print("Password is fine!")
        break
    else:
        print("Please check the following: ")
        # print(notes)
        for note in notes:
            print(note)
