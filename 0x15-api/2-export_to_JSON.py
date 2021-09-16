#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export data
in the JSON format."""
import json
import requests
from sys import argv


def task_to_json(IDemployee):
    # Variables
    userDict = {}

    link = "https://jsonplaceholder.typicode.com"

    # get requests
    usersRes = requests.get("{}/users/{}".format(link, IDemployee))
    todosRes = requests.get("{}/users/{}/todos".format(link, IDemployee))

    # Get the json from responses
    username = usersRes.json().get('username')
    todosJson = todosRes.json()
    # Save the employee Name
    userDict[IDemployee] = []
    # Loop the tasks and save
    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = username
        taskDict['completed'] = task.get('completed')

        userDict[IDemployee].append(taskDict)

    with open("{}.json".format(IDemployee), "w") as jsonFile:
        json.dump(userDict, jsonFile)


if __name__ == "__main__":
    task_to_json(argv[1])
