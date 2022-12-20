import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

match sistem_operasi:
    case "posix":os.system("clear")
    case "nt":os.system("cls")

print("WELCOME TO THE PROGRAM")
print("   LIBRARY DATABASE")
print("======================\n")

CRUD.init_console()

while True:
    match sistem_operasi:
        case "posix":os.system("clear")
        case "nt":os.system("cls")

    print("WELCOME TO THE PROGRAM")
    print("   LIBRARY DATABASE")
    print("======================\n")

    print("1. Read Data")
    print("2. Create Data")
    print("3. Update Data")
    print("4. Delete Data\n")

    user_option = input("Input Your Option : ")

    match user_option:
        case "1" : CRUD.read_console()
        case "2" : CRUD.create_console()
        case "3" : CRUD.update_console()
        case "4" : CRUD.delete_console()

    is_done = input("End the program  (y/n) : ")

    if is_done == "y" or is_done == "Y":
        break

print("END OF PROGRAM, THANKYOU FOR USE IT")
