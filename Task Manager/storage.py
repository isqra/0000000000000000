def load_file(task_list, NAME_FILE_SAVES):
    with open(NAME_FILE_SAVES, 'r') as file:
        for line in file:
            task_list.append(line.strip())
    return task_list

def save_file(task_list, NAME_FILE_SAVES):
    with open(NAME_FILE_SAVES, "w", encoding="utf-8") as file:
        for task in task_list:
            file.write(task + "\n")