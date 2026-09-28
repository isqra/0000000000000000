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