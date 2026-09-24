import os
import time
import multiprocess as mp

def main():
    pid = os.getpid()
    ppid = os.getppid()
    print("Начало")
    print(f"PID: {pid}")
    print(f"Родительский PID: {ppid}")
    process = mp.Process(target=welcome)
    process.start()
    process.join()

def welcome():
    pid = os.getpid()
    ppid = os.getppid()
    print("Привет")
    print(f"PID: {pid}")
    print(f"Родительский PID: {ppid}")
    time.sleep(3)
    process = mp.Process(target=work)
    process.start()
    process.join()

def work():
    pid = os.getpid()
    ppid = os.getppid()
    print("Работаем...")
    print(f"PID: {pid}")
    print(f"Родительский PID: {ppid}")
    time.sleep(3)
    process = mp.Process(target=finish)
    process.start()
    process.join()

def finish():
    pid = os.getpid()
    ppid = os.getppid()
    print(f"PID: {pid}")
    print(f"Родительский PID: {ppid}")
    time.sleep(3)
    print("Завершение работы...")

if __name__ == "__main__":
    process_main = mp.Process(target=main)
    process_main.start()
    process_main.join()
