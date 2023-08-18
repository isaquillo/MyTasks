class Task:
    def __init__(
        self, id, name, description, start_date, end_date, category, percentage, owner
    ):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.category = category
        self.percentage = percentage
        self.owner = owner

    def __str__(self):
        info = (
            "Id: "
            + str(self.id)
            + " \nName: "
            + self.name
            + "\nDescription: "
            + self.description
            + "\nStart Date: "
            + self.start_date
            + "\nEnd Date: "
            + self.end_date
            + "\nCategory: "
            + self.category
            + "\nPercentage: "
            + str(self.percentage)
            + "\nOwner: "
            + self.owner
        )
        return info


class DaoTasks:
    list_of_tasks = []
    list_of_categories = []
    counter = 0
    changes_on_state = False
    current_gui_skin = None

    @staticmethod
    def add(name, description, start_date, end_date, category, percentage, owner):
        DaoTasks.counter += 1
        new_task = Task(
            DaoTasks.counter,
            name,
            description,
            start_date,
            end_date,
            category,
            percentage,
            owner,
        )
        DaoTasks.list_of_tasks.append(new_task)
        return new_task

    @staticmethod
    def search(id):
        for task in DaoTasks.list_of_tasks:
            if task.id == id:
                return task

    @staticmethod
    def update(
        id, name, description, start_date, end_date, category, percentage, owner
    ):
        for index, task in enumerate(DaoTasks.list_of_tasks):
            if task.id == id:
                DaoTasks.list_of_tasks[index].name = name
                DaoTasks.list_of_tasks[index].description = description
                DaoTasks.list_of_tasks[index].start_date = start_date
                DaoTasks.list_of_tasks[index].end_date = end_date
                DaoTasks.list_of_tasks[index].category = category
                DaoTasks.list_of_tasks[index].percentage = percentage
                DaoTasks.list_of_tasks[index].owner = owner
                return DaoTasks.list_of_tasks[index]

    @staticmethod
    def delete(id):
        for index, task in enumerate(DaoTasks.list_of_tasks):
            if task.id == id:
                return DaoTasks.list_of_tasks.pop(index)
