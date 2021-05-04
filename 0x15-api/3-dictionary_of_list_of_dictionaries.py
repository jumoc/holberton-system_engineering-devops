#!/usr/bin/python3
"""gather data from an api module"""
import json
import requests


def get_data():
    """exports to csv"""

    with open("todo_all_employees.json", "w") as f:
        pass

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/"
        ).json()
    n_dict = {}
    for i in range(len(users)):
        user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                users[i]['id']
                )
            ).json()

        todos = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                users[i]['id']
                )
            ).json()

        tasks = []
        for todo in todos:
            tasks.append(
                {
                    "username": user['username'], "task": todo['title'],
                    "completed": todo['completed'],
                }
            )

        n_dict[user['id']] = tasks

    with open("todo_all_employees.json", "a") as f:
        f.write(json.dumps(n_dict))


if __name__ == '__main__':
    get_data()
