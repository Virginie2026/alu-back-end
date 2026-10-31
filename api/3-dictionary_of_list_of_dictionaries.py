#!/usr/bin/python3
"""
Python script that exports all employees' TODO list progress
in JSON format using a REST API.
"""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_res = requests.get("{}/users".format(base_url))
    users = users_res.json()

    todos_res = requests.get("{}/todos".format(base_url))
    todos = todos_res.json()

    all_data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_todos = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if str(task.get("userId")) == user_id
        ]
        all_data[user_id] = user_todos

    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(all_data, f)
