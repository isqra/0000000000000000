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