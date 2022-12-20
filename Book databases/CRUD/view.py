from . import Operasi

def delete_console():
    read_console()

    while True:
        print("Please Select number of book")
        choose = int(input("number of book : "))
        books_data = Operasi.read(index=choose)

        if books_data:
            break
        else:
            print("Invalid Number, Please try again ! ")

    data_break = books_data.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    writer = data_break[2]
    title = data_break[3]
    year = data_break[4][:-1]
        
    while True:
        print("\n"+"="*100)
        print("Your data : ")
        print(f"1. Title \t : {title:.40}")
        print(f"2. Writer \t : {writer:.40}")
        print(f"3. Year \t : {year:4}")

        is_done = input("Are you sure to delete (y/n) : ")
        if is_done == "y" or is_done == "Y":
            Operasi.delete(choose)
            print("Your data has been delete")
            break
        else:
            break

def update_console():
    read_console()
    while True:
        print("Please Select number of book")
        choose = int(input("number of book : "))
        books_data = Operasi.read(index=choose)

        if books_data:
            break
        else:
            print("Invalid Number, Please try again ! ")

    data_break = books_data.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    writer = data_break[2]
    title = data_break[3]
    year = data_break[4][:-1]

    while True:
        print("\n"+"="*100)
        print("Please select the items you want to edit")
        print(f"1. Title \t : {title:.40}")
        print(f"2. Writer \t : {writer:.40}")
        print(f"3. Year \t : {year:4}")

        user_option = input("Select Item : ")
        print("\n"+"="*100)
        match user_option : 
            case "1": title = input("Title\t: ")
            case "2": writer = input("Writer\t: ")
            case "3": 
                while True:
                    try:
                        year = int(input("Year\t: ")) 
                        if len(str(year)) == 4:
                            break
                        else:
                            print("Data of year is (yyyy)")    
                    except:
                        print("Please check your data carefully !")
                        print("data type of Year is 'Integer'")

            case _: print("Item that you select Invalid")

        print("Your new data : ")
        print(f"1. Title \t : {title:.40}")
        print(f"2. Writer \t : {writer:.40}")
        print(f"3. Year \t : {year:4}")
        
        is_done = input("Continue for update  (y/n) : ")

        if is_done == "n" or is_done == "N":
            break

    Operasi.update(choose,pk,date_add,year,writer,title)

def create_console():           
    print("\n\n"+"="*100)
    print("Please add book's data\n")
    writer = input("Writer\t: ")
    title = input("Title\t: ")
    while True:
        try:
            year = int(input("Year\t: ")) 
            if len(str(year)) == 4:
                break
            else:
                print("Data of year is (yyyy)")    
        except:
            print("Please check your data carefully !")
            print("data type of Year is 'Integer'")

    Operasi.create_data(writer,title,year)
    print("\n This is your new data")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    title = "title"
    writer = "writer"
    year = "year"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {title:40} | {writer:40} | {year:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        writer = data_break[2]
        title = data_break[3]
        year = data_break[4]
        print(f"{index+1:4} | {title:.40} | {writer:.40} | {year:4}",end="")

    # Footer
    print("="*100+"\n")