#!/usr/init/python3
#!/usr/bin/python3
"""
Script that returns information about an employee's TODO list progress using a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_res = requests.get("{}/users/{}".format(base_url, employee_id))
    employee_name = user_res.json().get("name")

    # Get employee todos
    todos_res = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
    todos = todos_res.json()

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    # Print summary line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Print each completed task title with a tab and a space
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
