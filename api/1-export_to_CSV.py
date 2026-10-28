#!/usr/bin/python3
"""
Python script that exports an employee's TODO list progress
in CSV format using a REST API.
"""
import csv
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
    user_data = user_res.json()
    username = user_data.get("username")

    todos_res = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos = todos_res.json()

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
