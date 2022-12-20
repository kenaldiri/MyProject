from time import time
from . import Database
from .utility import random_string
import time
import os

def delete(choose):
    try:
        with open(Database.DB_NAME, 'r') as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == choose - 1:
                    pass
                else:
                    with open('data_temp.txt', 'a', encoding='utf-8') as temp:
                        temp.write(content)
                counter += 1
    except:
        print("Database Error")

    os.rename('data_temp.txt', Database.DB_NAME)


def update(choose,pk,date_add,year,writer,title):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["writer"] = writer + Database.TEMPLATE["writer"] [len(writer):]
    data["title"] = title + Database.TEMPLATE["title"] [len(title):]
    data["year"] = str(year)

    data_input = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'

    length_data = len(data_input)

    try:
        with open(Database.DB_NAME, 'r+', encoding="utf-8") as file:
            file.seek(length_data * (choose-1))
            file.write(data_input)
    except:
        print("Cannot to add data")

def create_data(writer,title,year):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["writer"] = writer + Database.TEMPLATE["writer"] [len(writer):]
    data["title"] = title + Database.TEMPLATE["title"] [len(title):]
    data["year"] = str(year)

    data_input = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'

    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_input)
    except:
        print("Cannot to add data")

def create_first_data():

    writer = input("Writer : ")
    title = input("Title : ")

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
    
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["writer"] = writer + Database.TEMPLATE["writer"] [len(writer):]
    data["title"] = title + Database.TEMPLATE["title"] [len(title):]
    data["year"] = str(year)

    data_input = f'{data["pk"]},{data["date_add"]},{data["writer"]},{data["title"]},{data["year"]}\n'

    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_input)
    except:
        print("Cannot to add data")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            amount_book = len(content)
            if "index" in kwargs:
                books_index = kwargs["index"]-1
                if books_index < 0 or books_index > amount_book:
                    return False
                else:
                    return content[books_index]
            else:
                return content
    except:
        print("Failed to Read Database")
        return False
