import mysql.connector as connector
from hashlib import sha1


class Connection():
    def __init__(self):
        self.con = connector.connect(
            host='localhost', user='root', password='root', database='userdata')
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()


def authenticate(username, password):
    hash = sha1(password.encode('utf-8')).hexdigest()

    db = Connection()

    db.cur.execute(
        "SELECT username FROM users WHERE username='%s' AND password='%s'" % username, password)
    result = db.cur.fetchall()

    return ' '.join(sum(result, ()))


def login():
    print("Welcome to our login page!")
    username = input("Username: ")
    password = input("Password: ")

    user = authenticate(username, password)

    if(len(user) > 0):
        print(f"Welcome {user}!")
    else:
        print("Access denied!")


if(__name__ == '__main__'):
    login()
