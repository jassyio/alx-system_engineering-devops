import requests
import csv
import sys

def fetch_and_export_to_csv(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data for employee ID {employee_id}")
        return

    todos = response.json()
    employee_name = user_info['username']
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            task_completed = todo['completed']
            task_title = todo['title']
            csv_writer.writerow([employee_id, employee_name, str(task_completed), task_title])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_and_export_to_csv(employee_id)
