#!/usr/bin/python3
"""gather data from an api module"""
import requests
import json
import sys


def get_data():
    """exports to csv"""
    id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id)
        ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        ).json()

    tasks = []
    for todo in todos:
        tasks.append(
            {"task": todo['title'], "completed": todo['completed'],
             "username": user['username']}
        )

    n_dict = {user['id']: tasks}

    with open("{}.json".format(id), "w") as file:
        file.write(json.dumps(n_dict))


if __name__ == '__main__':
    get_data()
