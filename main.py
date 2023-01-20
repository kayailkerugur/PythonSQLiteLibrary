import sqlite3

class Main:
    database = ""
    def __init__(self,database):
        self.database = database

    def connect(self) -> sqlite3.Connection:
        vt = sqlite3.connect(self.database)
        return vt
    
    def cursor(self) -> sqlite3.Cursor:
        vt = self.connect()
        cursor = vt.cursor()
        return cursor
    
    def create_table(self,table_name):
        content_name = []
        while True:
            kullanici = input("Enter the content titles. (q to exit)")
            if kullanici == "q":
                break
            else:
                content_name.append(str(kullanici))
        
        strings = list(filter(lambda x: isinstance(x, str), content_name))
        full_sentence = ",".join(strings)
        cursor = self.cursor()
        cursor.execute("CREATE TABLE " + table_name + " (" + full_sentence + ") ")


main = Main(database="databasee.sqlite")

main.create_table(table_name="titles")