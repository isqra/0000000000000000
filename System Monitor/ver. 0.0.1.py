import json
import os
import platform
import psutil

def main():
    data = search_data()
    save_data(data)

def search_data():
    name_PC = str(os.getpid())
    logic_count = psutil.cpu_count()
    used_memory = (f"{psutil.virtual_memory().used} / {(1024 * 3)} / {psutil.virtual_memory().total} {(1024 * 3)}")
    process_count = psutil.process_iter
    treads_count = psutil.Process().num_threads()
    cpu_used =psutil.cpu_percent()
    # memory = psutil.disk_usage()
    cpu_frequency = psutil.cpu_freq()

    data = { "Имя ПК" : name_PC,
             "Логические процессы" : logic_count,
             "Используется ОЗУ" : used_memory,
             "Число процессов" : process_count,
             "Число потоков" : treads_count,
             "Загрузка процессора" : cpu_used,
             # "Используется ПЗУ" : memory,
             "Скорость процессора" : cpu_frequency,

            }
    return data

def save_data(data:dict):
    name = "data.json"
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

main()
