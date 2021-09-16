#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export data in the JSON format. """
import json
import requests

def all_json():
     # Variables
    userTask = {}

    link = "https://jsonplaceholder.typicode.com"

    # get requests
    usersJson = requests.get("{}/users".format(link)).json()
    todosJson = requests.get("{}/todos".format(link)).json()

    userInfo = {}

    # get the json from responses
    for user in usersJson:
        userInfo[user['id']] = user['username']

    for task in todosJson:
        if userTask.get(task['userId'], False) is False:
            userTask[task['userId']] = []
        taskDict = {}
        taskDict['username'] = userInfo[task['userId']]
        taskDict['task'] = task['title']
        taskDict['completed'] = task['completed']
        userTask[task['userId']].append(taskDict)

    nameFile = "todo_all_employees.json"
    with open(nameFile, "w") as jsonFile:
        json.dump(userTask, jsonFile)

if __name__ == '__main__':
    all_json()
