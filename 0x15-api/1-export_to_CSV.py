#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the CSV format. """
import csv
import requests
from sys import argv


def export_to_CSV(sizeofReq):
    """ The task define export to the CSV format"""

    # Variables
    allTasks = []

    link = "https://jsonplaceholder.typicode.com"

    # get requests
    usersRes = requests.get("{}/users/{}".format(link, sizeofReq))
    todosRes = requests.get("{}/users/{}/todos".format(link, sizeofReq))

    # Get the json from responses
    name = usersRes.json().get('username')
    todosJson = todosRes.json()

    # Save the employee Name -- Loop the tasks and save
    for task in todosJson:
        taskRow = []
        taskRow.append(sizeofReq)
        taskRow.append(name)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))
        allTasks.append(taskRow)

    with open("{}.csv".format(sizeofReq), "w") as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(allTasks)

    return 0


if __name__ == '__main__':
    export_to_CSV(int(argv[1]))
