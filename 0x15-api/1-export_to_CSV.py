#!/usr/bin/python3
"""gather data from an api module"""
import requests
import sys
import os


def get_data():
    id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id)
        ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        ).json()

    text = ""
    for todo in todos:
        text += '"{}","{}","{}","{}"\n'.format(
            user['id'], user['username'], todo['completed'], todo['title']
        )

    with open("{}.csv".format(id), "w") as file:
        file.write(text)


if __name__ == '__main__':
    get_data()
