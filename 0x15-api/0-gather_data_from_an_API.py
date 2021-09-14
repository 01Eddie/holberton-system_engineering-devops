#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress."""
import requests
from sys import argv


def get_employee(sizeofReq):
    """ Use API from jsonplaceholder """

    # Variables
    taskList = []
    count = 0

    link = "https://jsonplaceholder.typicode.com"

    # get requests
    usersRes = requests.get(
        "{}/users/{}".format(link, sizeofReq))
    todosRes = requests.get(
        "{}/users/{}/todos".
        format(link, sizeofReq))

    # Get the json from responses
    name = usersRes.json().get('name')
    todosJson = todosRes.json()

    # Save the employee Name -- Loop the tasks
    for task in todosJson:
        if task.get('completed') is True:
            count += 1
            # save the task title to taskList
            taskList.append(task.get('title'))

    # Print the first line
    print('Employee {} is done with tasks({}/{}):'.format(
        name, count, len(todosJson)))
    # Loop the taskList and print tasks
    for title in taskList:
        print('\t {}'.format(title))

    return 0


if __name__ == '__main__':
    get_employee(argv[1])
