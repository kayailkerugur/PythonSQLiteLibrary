import sqlite3

class Main:
    
    def connect(veri_tabani) -> sqlite3.Connection:
        vt = sqlite3.connect(veri_tabani)
        return vt
    
    def cursor() -> sqlite3.Cursor:
        vt = Main.connect()
        cursor = vt.cursor()
        return cursor
    
    def create_table(table_name):
        content_name = []
        full_sentence = ""
        while True:
            kullanici = input("Enter the content titles. (q to exit)")
            if kullanici == "q":
                break
            else:
                content_name.append(str(kullanici))
        
        cursor = Main.cursor()
        cursor.execute("CREATE TABLE " + table_name + " (" + full_sentence + ") ")



Main.create_table(table_name="ilker")
    



vt = sqlite3.connect("veri_tabani")

cursor = vt.cursor()
print(type(cursor))