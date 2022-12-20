from . import Operasi

DB_NAME = "database.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add" : "yyyy-mm-dd",
    "title" : 255 * " ",
    "writer" : 255 * " ",
    "tahun" : "yyyy"
}

def init_console():
    try : 
        with open(DB_NAME, "r") as file:
            print("Database is Availabe, init done!")
    except:
        print("Database isn't Available, Please Create New . . .\n")
        Operasi.create_first_data()