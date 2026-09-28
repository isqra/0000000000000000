import os
from view import show_collection, show_menu
from core import add_task, edit_task, delete_tasks
from config import NAME_FILE_SAVES
from storage import save_file, load_file


def main():
    is_running = True
    NAME_FILE_SAVES
    while is_running:
        task_collection = load_file(NAME_FILE_SAVES)
        show_menu()
        choice_user = input("Введите ваш выбор: ")

        match str(choice_user):
            case "1":
                show_collection(task_collection)

            case "2":
                add_task(task_collection)
                save_file(task_collection, NAME_FILE_SAVES)

            case "3":
                show_collection(task_collection)
                edit_task(task_collection)
                save_file(task_collection, NAME_FILE_SAVES)

            case "4":
                show_collection(task_collection)
                delete_tasks(task_collection)
                save_file(task_collection, NAME_FILE_SAVES)

            case "5":
                is_running = False

            case _:
                print("Такого пункта нет...")

if __name__ == "__main__":
    main()