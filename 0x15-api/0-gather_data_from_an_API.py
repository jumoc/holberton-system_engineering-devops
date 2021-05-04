#!/usr/bin/python3
"""gather data from an api module"""
import requests
import sys


def get_data():
    try:
        id = int(sys.argv[1])
    except:
        return

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            id
            )
        )
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            id
            )
        )

    comp = 0
    for todo in todos.json():
        if todo['completed'] is True:
            comp += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.json()['name'], comp, len(todos.json())
    ))

    for todo in todos.json():
        print("\t {}".format(todo['title']))


if __name__ == '__main__':
    get_data()
