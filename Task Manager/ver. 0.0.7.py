import os

def show_collection(task_collection):
    print("=" * 45)
    for i, j in enumerate(task_collection):
        print(i + 1, j)
    print("=" * 45)

def show_message(message):
    print(f"{message}\n")

def show_menu():
    print("1. Показать задачи \n"
          "2. Добавить задачу \n"
          "3. Редактировать задачи \n"
          "4. Удаление задачи \n"
          "5. Выход")


def check_number(select_task, task_list):
    if select_task.isdigit():
        if int(select_task) > 0 and int(select_task) <= len(task_list):
            return True
        else:
            show_message(f"Задачи с номером >{select_task}< нет в списке")
            return False
    else:
        show_message("Ошибка")
        return False


def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи: ")
    if check_number(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        show_message(f"Задача >{delete_task}< удалена")


def edit_task(task_collection):
    select_task = input("Введите номер задачи: ")
    if check_number(select_task, task_collection):
        new_task_name = input("Новое имя задачи: ")
        if not new_task_name.strip():
            show_message("Название не может быть пустым")
        else:
            task_collection[int(select_task) - 1] = new_task_name
            show_message("Задача успешно переименована")

def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ")
    if not task_name.strip():
        show_message("Название не может быть пустым")
    else:
        task_collection.append(task_name)
        show_message(f"Задача >{task_name}< успешно добавлена")

def main():
    is_running = True

    name_file = "saves.txt"
    if os.path.exists(name_file):
        with open(name_file, "r", encoding="utf-8") as file:
            task_collection = [line.strip() for line in file if line.strip()]
    else:
        task_collection = []

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ")

        match str(choice_user):
            case "1":
                show_collection(task_collection)

            case "2":
                add_task(task_collection)
                with open(name_file, "w", encoding="utf-8") as file:
                    for task in task_collection:
                        file.write(task + "\n")

            case "3":
                show_collection(task_collection)
                edit_task(task_collection)
                with open(name_file, "w", encoding="utf-8") as file:
                    for task in task_collection:
                        file.write(task + "\n")

            case "4":
                show_collection(task_collection)
                delete_tasks(task_collection)
                with open(name_file, "w", encoding="utf-8") as file:
                    for task in task_collection:
                        file.write(task + "\n")

            case "5":
                is_running = False

            case _:
                print("Такого пункта нет...")

if __name__ == "__main__":
    main()
