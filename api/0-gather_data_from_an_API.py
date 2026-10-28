#!/usr/bin/python3
"""
Module that gathers data from an API and displays an employee's TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get("{}/users/{}".format(base_url, employee_id))
    employee_name = user_res.json().get("name")

    todos_res = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
    todos = todos_res.json()

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
