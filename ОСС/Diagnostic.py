import os
import sys
import platform
import datetime

os_name = platform.system()
os_release = platform.release()

current_dir = os.getcwd()
cpu_count = os.cpu_count()

python_path = sys.executable
python_version = sys.version.split()[0]

current_time = datetime.datetime.now()

print("Диагностика системы")
print(f"Время запуска : {current_time:%d.%m.%Y %H:%M:%S}")
print(f"ОС            : {os_name} {os_release}")
print(f"Процессоры    : {cpu_count}")
print(f"Текущая папка : {current_dir}")
print(f"Python        : {python_version} ({python_path})")
