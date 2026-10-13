import os
import json
from pathlib import Path

def get_base_dir():
    return os.getcwd()

def insure_save_file():
    save_path = Path("save.json")
    save_path.write_text(f"test : {1}", encoding="utf-8")
    print("Файл создан")

get_base_dir()
insure_save_file()