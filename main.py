import sqlite3

class Main:
    database = ""
    table_name = ""
    def __init__(self,database,table_name):
        self.database = database
        self.table_name = table_name

    def connect(self) -> sqlite3.Connection:
        vt = sqlite3.connect(self.database)
        return vt
    
    def cursor(self) -> sqlite3.Cursor:
        vt = self.connect()
        cursor = vt.cursor()
        return cursor
    
    def create_table(selfd,table_name):
        content_name = []
        self.table_name = table_name
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

    def add_table(self,content_name, content):
        vt = self.connect()
        cursor = self.cursor()
        cursor.execute("INSERT INTO " + "bunungibi" + content_name + " VALUES " + content)
        vt.commit()

    def select_table(self) -> str:
        cursor = self.cursor()
        result = cursor.execute("")
        return result


