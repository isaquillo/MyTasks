import platform
import os
import csv
import pickle
from datetime import datetime
from pathlib import Path
import database as db


def load_state():
    read_counter()
    read_tasks()
    read_categories()


def save_state():
    save_counter()
    save_tasks()
    save_categories()


def clear_screen():
    os.system("cls") if platform.system == "Windows" else os.system("clear")


def validate_text_length(text, minimum_length=0, maximum_length=100):
    return len(text) >= minimum_length and len(text) <= maximum_length


def validate_int(num, minimum=None, maximum=None):
    if minimum is not None and maximum is not None:
        return str(num).isdigit() and int(num) >= minimum and int(num) <= maximum
    elif minimum is not None:
        return str(num).isdigit() and int(num) >= minimum
    elif maximum is not None:
        return str(num).isdigit() and int(num) <= maximum
    return str(num).isdigit()


def validate_date_format(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def validate_correct_range_date(start_date, end_date):
    try:
        return datetime.strptime(start_date, "%d-%m-%Y") <= datetime.strptime(
            end_date, "%d-%m-%Y"
        )
    except:
        return False


def read_counter():
    try:
        with open("storage/counter.txt", "r") as f:
            db.DaoTasks.counter = int(f.read())
    except Exception as e:
        print("On function read_counter: ")
        print(e.__str__)


def save_counter():
    try:
        with open("storage/counter.txt", "w") as f:
            f.write(str(db.DaoTasks.counter))
    except Exception as e:
        print(e.__str__)


def read_tasks():
    try:
        with open("storage/tasks.csv", "r") as f:
            reader = csv.reader(f, delimiter=";")
            for (
                id,
                name,
                description,
                start_date,
                end_date,
                category,
                percentage,
                owner,
            ) in reader:
                task = db.Task(
                    int(id),
                    name,
                    description,
                    start_date,
                    end_date,
                    category,
                    percentage,
                    owner,
                )
                db.DaoTasks.list_of_tasks.append(task)
    except Exception as e:
        print("On function read_tasks: ")
        print(e.__str__)


def save_tasks():
    try:
        with open("storage/tasks.csv", "w", newline="\n") as f:
            writer = csv.writer(f, delimiter=";")
            for task in db.DaoTasks.list_of_tasks:
                writer.writerow(
                    [
                        task.id,
                        task.name,
                        task.description,
                        task.start_date,
                        task.end_date,
                        task.category,
                        task.percentage,
                        task.owner,
                    ]
                )
    except Exception as e:
        print(e)


def read_categories():
    try:
        with open("storage/categories.pkl", "rb") as f:
            db.DaoTasks.list_of_categories = pickle.load(f)
            db.DaoTasks.list_of_categories.sort()
    except Exception as e:
        print("On function read_categories: ")
        print(e.__str__)


def save_categories():
    try:
        with open("storage/categories.pkl", "wb") as f:
            pickle.dump(db.DaoTasks.list_of_categories, f)
    except Exception as e:
        print(e.__str__)


def add_category(category):
    db.DaoTasks.list_of_categories.append(category)
    db.DaoTasks.list_of_categories.sort()


def get_substring(text, max=None):
    if len(text) <= max:
        return text
    else:
        return text[: max + 1] + "..."


def get_abs_path(file):
    return str(Path(__file__).parent.absolute() / file)


def get_qss_files(path, extension):
    files = []
    try:
        for file in os.listdir(path):
            if file.endswith(extension):
                files.append(file)
        return files
    except Exception as e:
        raise e
    
