FILE_NAME = "tasks.json"

import json
from models import Task

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            task_data = json.load(file)

        tasks = []

        for data in task_data:
            task = Task(data["title"])
            task.done = data["done"]
            tasks.append(task)

        return tasks

    except FileNotFoundError:
        return []

def save_tasks(tasks):
    task_data = []

    for task in tasks:
        task_data.append(task.to_dic())

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(task_data, file, ensure_ascii=False, indent=4)