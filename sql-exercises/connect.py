import sqlite3



        

if __name__ == '__main__':

    try:
        with sqlite3.connect("my.db") as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
            
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)