import helpers
import database as db


def start():
    while True:
        helpers.clear_screen()

        print("=========================")
        print("Welcome to MyTasks App")
        print("=========================")
        print("[1] List tasks")
        print("[2] List detailed task")
        print("[3] Search task")
        print("[4] Create task")
        print("[5] Update task")
        print("[6] Delete task")
        print("[7] Save changes")
        print("[8] Close application")

        option = input("> ")
        helpers.clear_screen()

        if option == "1":
            print("List of tasks...\n") if len(
                db.DaoTasks.list_of_tasks
            ) > 0 else print("No tasks found")
            for task in db.DaoTasks.list_of_tasks:
                print(
                    f"Id:{task.id} - Name:{task.name} - Description:{task.description}"
                )

        elif option == "2":
            print("Detail of task...\n")
            while True:
                id = capture_int(
                    "Enter the id of the task (positive integer only)", min=1
                )
                if id is not None:
                    break
            task = db.DaoTasks.search(id)
            print(task) if task else print("Task not found")

        elif option == "3":
            print("Searching task...\n")
            while True:
                id = capture_int(
                    "Enter the id of the task (positive integer only)", min=1
                )
                if id is not None:
                    break
            task = db.DaoTasks.search(id)
            print(task) if task else print("Task not found")

        elif option == "4":
            name = ""
            description = ""
            start_date = ""
            end_date = ""
            category = ""
            percentage = ""
            owner = ""
            print("Creating task...\n")
            while True:
                name = capture_text(
                    "Enter the name of the task (3-30 characters)", 3, 30
                )
                if name is not None:
                    break
            while True:
                description = capture_text(
                    "Enter the description of the task (0-100 characters)", 0, 100
                )
                if description is not None:
                    break
                else:
                    print("Invalid format. Try again")
            while True:
                while True:
                    start_date = capture_date("Enter the start date (dd-mm-yyyy)")
                    if start_date is not None:
                        break
                while True:
                    end_date = capture_date("Enter the end date (dd-mm-yyyy)")
                    if end_date is not None:
                        break
                if helpers.validate_correct_range_date(start_date, end_date):
                    break
                else:
                    print(
                        "The end date of the task should be after or equal start date"
                    )  # Exit input dates (start and end) loop
            while True:
                option = select_category("Select the category of the task...")
                if 1 <= option <= len(db.DaoTasks.list_of_categories):
                    category = db.DaoTasks.list_of_categories[option - 1]
                    break
                else:
                    category = add_category("Adding a new category...")
                    break
            while True:
                percentage = capture_int("Enter the percentaje (0-100)", 0, 100)
                if percentage is not None:
                    break
            while True:
                owner = capture_text("Enter the owner (3-30 characters)", 3, 30)
                if owner is not None:
                    break
            new_task = db.DaoTasks.add(
                name, description, start_date, end_date, category, percentage, owner
            )
            db.DaoTasks.changes_on_state = True
            print("Added task..")
            print(new_task)

        elif option == "5":
            print("Updating task...\n")
            while True:
                id = capture_int(
                    "Enter the id of the test (positive integer only)", min=1
                )
                if id is not None:
                    break
            task = db.DaoTasks.search(id)
            if task is not None:
                while True:
                    option = task_update_menu(task)
                    if option == 1:
                        while True:
                            name = capture_text(
                                "Enter the new name (3-30 characters)", 3, 30
                            )
                            if name is not None:
                                task.name = name
                                break
                    elif option == 2:
                        while True:
                            description = capture_text(
                                "Enter the new description (0-100 characters)", 0, 100
                            )
                            if description is not None:
                                task.description = description
                                break
                    elif option == 3:
                        start_date = capture_date(
                            "Enter the new start date (dd-mm-yyyy)"
                        )
                        if start_date is not None:
                            task.start_date = start_date
                    elif option == 4:
                        end_date = capture_date("Enter the new end date (dd-mm-yyyy)")
                        if end_date is not None:
                            task.end_date = end_date
                    elif option == 5:
                        answer = select_category("Select the new category...")
                        if 1 <= answer <= len(db.DaoTasks.list_of_categories):
                            task.category = db.DaoTasks.list_of_categories[answer - 1]
                        else:
                            category = add_category()
                    elif option == 6:
                        percentage = capture_int(
                            "Enter the percentage of completion (0-100)", min=0, max=100
                        )
                        if percentage is not None:
                            task.percentage = percentage
                    elif option == 7:
                        owner = capture_text(
                            "Enter the new owner (3-30 characters)", 3, 30
                        )
                        if owner is not None:
                            task.owner = owner
                    elif option == 8:
                        break
                    db.DaoTasks.changes_on_state = True
                    print("Task updated...")
                    print(task)
                    while True:
                        answer = capture_int(
                            "Do you want to update another field of the task? [1]Yes [2]No",
                            1,
                            2,
                        )
                        if answer is not None:
                            break
                    if answer != 1:
                        break
            else:
                print("Task not found")

        elif option == "6":
            print("Deleting task...\n")
            while True:
                id = capture_int(
                    "Enter the id of the test to delete (positive integer only)", min=1
                )
                if id is not None:
                    break
            task = db.DaoTasks.search(id)
            if task is not None:
                task = db.DaoTasks.delete(id)
                print("The task has been deleted")
                print(task)
                db.DaoTasks.changes_on_state = True

        elif option == "7":
            print("Saving changes...\n")
            while True:
                answer = capture_int(
                    "Please confirm if you want to save changes [1]Yes [2]No", 1, 2
                )
                if answer is not None:
                    break
            if answer == 1:
                helpers.save_state()
                print("All changes have been saved...")
                db.DaoTasks.changes_on_state = False

        elif option == "8":
            if db.DaoTasks.changes_on_state:
                while True:
                    answer = capture_int(
                        "Do you want to save changes before exiting? [1]Yes [2]No", 1, 2
                    )
                    if answer is not None:
                        break
                if answer == 1:
                    helpers.save_state()
            print("Closing app...\n")
            break

        input("\nPress ENTER to continue...")


def capture_int(message=None, min=None, max=None):
    try:
        print(message)
        value = int(input("> "))
        is_correct_int = helpers.validate_int(value, min, max)
        if is_correct_int:
            return value
        else:
            print("Invalid format. Try again")
            return None
    except ValueError:
        print("Invalid format. Try again")
        return None


def capture_text(message=None, min=None, max=None):
    try:
        print(message)
        text = input("> ")
        is_correct_text = helpers.validate_text_length(text, min, max)
        if is_correct_text:
            return text
        else:
            print("Invalid format. Try again")
            return None
    except ValueError:
        print("Invalid format. Try again")
        return None


def capture_date(message):
    try:
        print(message)
        date = input("> ")
        is_correct_date = helpers.validate_date_format(date)
        if is_correct_date:
            return date
        else:
            print("Invalid date format. Try again")
            return None
    except ValueError:
        print("Invalid date format. Try again")
        return None


def select_category(message=None):
    try:
        print(message)
        for index, category in enumerate(db.DaoTasks.list_of_categories):
            print(f"[{index + 1}] {category}")
        num_categories = len(db.DaoTasks.list_of_categories)
        print(f"[{num_categories + 1}] Create a new category")
        option = int(input("> "))
        is_correct_option = helpers.validate_int(option, 1, num_categories + 1)
        if is_correct_option:
            return option
        else:
            print("Invalid option. Try again")
            return None
    except ValueError:
        print("Invalid format. Try again")
        return None


def add_category(message):
    print(message)
    while True:
        category = capture_text(
            "Enter the name of the category (3-30 characters)", 3, 30
        )
        if category is not None:
            break
        else:
            print("Invalid format. Try again")
    db.DaoTasks.list_of_categories.append(category)
    db.DaoTasks.changes_on_state = True
    print("Category created...\n")
    return category


def task_update_menu(task):
    print("[1] Name=" + task.name)
    print("[2] Description=" + task.description)
    print("[3] Start date=" + task.start_date)
    print("[4] End date=" + task.end_date)
    print("[5] Category=" + task.category)
    print("[6] Percentage=" + str(task.percentage))
    print("[7] Owner=" + task.owner)
    print("[8] Return to main menu")
    print("Select field to update...")
    try:
        option = int(input("> "))
        is_correct_option = helpers.validate_int(option, minimum=1, maximum=8)
        if is_correct_option:
            return option
        else:
            print("Invalid option. Try again")
            return False
    except ValueError:
        print("Invalid option. Try again")
        return False
