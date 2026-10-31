#!/usr/bin/python3
"""
Python script that exports an employee's TODO list progress
in JSON format using a REST API.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get(
        "{}/users/{}".format(base_url, employee_id)
    )
    username = user_res.json().get("username")

    todos_res = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos = todos_res.json()

    task_list = []
    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {str(employee_id): task_list}

    filename = "{}.json".format(employee_id)
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(json_data, f)
