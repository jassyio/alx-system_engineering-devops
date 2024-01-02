import requests
import json
import sys

def fetch_and_export_to_json(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data for employee ID {employee_id}")
        return

    todos = response.json()
    employee_name = user_info['username']
    tasks_list = []

    for todo in todos:
        task_completed = todo['completed']
        task_title = todo['title']
        tasks_list.append({"task": task_title, "completed": task_completed, "username": employee_name})

    data = {str(employee_id): tasks_list}
    filename = f"{employee_id}.json"

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_and_export_to_json(employee_id)
