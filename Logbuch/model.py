import sqlite3, time
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

con = sqlite3.connect('logbuch.db')
cursor = con.cursor()


# def create_table():
#     c.execute(
#         'CREATE TABLE IF NOT EXISTS datein ( Titel VARCHAR(32), Article VARCHAR(300), login VARCHAR(300)) ')
#
#
# def dynamic_data_entry_user(id, name, vorname, login, password):
#     c.execute("INSERT INTO user (ID, Name, Vorname, login, password) VALUES (?, ?, ?, ?, ?)",
#               (id, name, vorname, login, password))
#     con.commit()
#
#
# def read_from_db_login(login):
#     c.execute("SELECT * FROM user WHERE login = ' " + login + " ' ")
#     for row in c.fetchall():
#         print(row)
#         # if c.fetchall().count(1):
#         #     return True
#         # else :
#         #     return False
#
#
# def read_from_db_pwd(password):
#     c.execute('''SELECT login, password FROM user WHERE login = ?''', password)
#     for row in c.fetchall():
#         print(row)
#
#     password = c.fetchone()
#     return password
#
#
# def read_from_db_id(id):
#     c.execute("SELECT * FROM user WHERE ID= ' " + id + " ' ")
#     for row in c.fetchall():
#         print(row)
#
#
# def read_from_all():
#     c.execute("SELECT login, password FROM user")
#     for row in c.fetchall():
#         print(row)


# --------------------------------------------------------------------
# funktion Login
# _______________________________________________________________________

# def login():
#     while True:
#         username = raw_input("please enter your username: ")
#
#         password = raw_input("please enter your password: ")
#         with sqlite3.connect("logbuch.db") as db:
#             cursor = db.cursor()
#
#         find_user = ("SELECT * FROM user WHERE login = ? AND password = ?")
#         cursor.execute(find_user, [(username), (password)])
#         results = cursor.fetchall()
#
#         if results:
#             for i in results:
#                 print("Welcome " + i[1] + " " + i[2])
#             # return("exit")
#             break
#         else:
#             print("Username or password not recognised")
#             again = raw_input("do you want to try again? (y/n) :")
#             if again.lower() == "n":
#                 print("Goodbye")
#                 time.sleep(1)
#
#                 break


#__________________________________________________________________
#connection
# def db_offnet():
#     with sqlite3.connect("logbuch.db") as db:
#         cursor = db.cursor()
#     return cursor
#_______________________________________________________________________
#login
#________________________________________________________________________

def login(username,  password ):
        find_user = ("SELECT * FROM user WHERE login = ? AND password = ?")
        cursor.execute(find_user, [(username), (password)])
        results = cursor.fetchall()
        return results


def dynamic_data_entry_user(id, name, vorname, login, password):
    cursor.execute("INSERT INTO user (ID, Name, Vorname, login, password) VALUES (?, ?, ?, ?, ?)",
              (id, name, vorname, login, password))
    con.commit()

def select_datein():
    find_log = ("SELECT Titel, Article FROM datein")
    cursor.execute(find_log)
    # results = c.fetchall()
    m = Gtk.ListStore(str, str)

    for row in cursor.fetchall():
        # m.append([row[0], row])
        #print(row[1])
        m.append([row[0], row[1]])

    return m


def record(titel, article):
    try:
        cursor.execute("INSERT INTO datein (Titel, Article) VALUES (?, ?)",(titel, article))
        con.commit()
        results= 1
    except:
        print ("probleme")
        results = 0

    return results

# def record(titel, article):
#         cursor.execute("INSERT INTO datein (Titel, Article) VALUES (?, ?)",(titel, article))
#         con.commit()
#         con.close()
#         results= 1


def load():
    find_user = ("SELECT * FROM datein")
    cursor.execute(find_user)
    results = cursor.fetchall()
    #cursor.close()
    #con.close()
    return results


# def schliessen_db(cursor):
#     with sqlite3.connect("logbuch.db") as db:
#             cursor.close()

#create_table()
# dynamic_data_entry_user(4,"Martyn", "Landry", "user", "user" )
# read_from_db("user", "user")
# read_from_all()

# read_from_db_id('1')

# print(read_from_db_login('admin'))

#login()

#select_log()

#dynamic_data_entry_user(20,"nom", "prenom", "log", "log")
