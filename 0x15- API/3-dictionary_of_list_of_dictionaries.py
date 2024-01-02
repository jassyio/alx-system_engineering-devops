#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: ./3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    todo_dict = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)
        tasks = response.json()

        todo_dict[user_id] = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            todo_dict[user_id].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_dict, json_file)
