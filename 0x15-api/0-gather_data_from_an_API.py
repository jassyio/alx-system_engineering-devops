#!/usr/bin/python3
import requests
import sys

def fetch_todo_list_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for employee ID {employee_id}")
        return

    todos = response.json()
    employee_name = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()['name']
    total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
