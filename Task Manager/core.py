from utils import check_number
from view import show_message

def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ")
    task_content = input("Введите содержание задачи: ")

    if not task_content.strip():
        show_message("Содержание задачи не может быть пустым")
    else:

        if not task_name.strip():
            show_message("Название не может быть пустым")
        else:
            task_collection.append(f"{task_name} | {task_content}")
            show_message(f"Задача > {task_name} < успешно добавлена")

def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи: ")
    if check_number(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        show_message(f"Задача > {delete_task} < удалена")


def edit_task(task_collection):
    select_task = input("Введите номер задачи: ")
    if check_number(select_task, task_collection):
        new_task_name = input("Новое имя задачи: ")
        if not new_task_name.strip():
            show_message("Название не может быть пустым")
        else:
            new_task_content = input("Содержание новой задачи: ")
            if not new_task_content.strip():
                show_message("Содержание не может быть пустым")
            else:

                task_collection[int(select_task) - 1] = f"{new_task_name} | {new_task_content}"
                show_message("Задача успешно изменена")
