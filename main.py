
import os
import sqlite3


def divide(a, b):
    return a / b


def get_user(username):
    connection = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = connection.execute(query).fetchall()
    connection.close()
    return result


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False


def main():
    print(divide(10, 0))
    print(calculate_average([]))
    print(get_user("admin"))
    print(read_file("data.txt"))


if __name__ == "__main__":
    main()
