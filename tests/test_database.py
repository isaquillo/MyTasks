import unittest
import copy

import database as db


class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.DaoTasks.list_of_tasks = [
            # id, description, star_date, end_date, category, percentage, owner
            db.Task(
                1,
                "Paint the wall",
                "Paint the wall of the house",
                "2023-07-01",
                "2023-07-05",
                "Home",
                "0",
                "Isaac",
            ),
            db.Task(
                2,
                "Wash the car",
                "Wash the Stratus",
                "2023-06-29",
                "2023-07-02",
                "Home",
                "0",
                "Isaac",
            ),
            db.Task(
                3,
                "U3EA Actividad de Aprendizaje",
                "Materia: Programación Web I",
                "2023-07-03",
                "2023-07-14",
                "School",
                "0",
                "Isaac",
            ),
        ]
        db.DaoTasks.counter = 3

    def test_add(self):
        db.DaoTasks.counter += 1
        new_task = db.Task(
            db.DaoTasks.counter,
            "Clean the room",
            "Clean the room",
            "2023-04-12",
            "2023-06-27",
            "Home",
            "25",
            "Isaac",
        )
        db.DaoTasks.list_of_tasks.append(new_task)
        self.assertEqual(len(db.DaoTasks.list_of_tasks), 4)
        self.assertEqual(new_task.name, "Clean the room")
        self.assertEqual(new_task.description, "Clean the room")
        self.assertEqual(new_task.star_date, "2023-04-12")
        self.assertEqual(new_task.end_date, "2023-06-27")
        self.assertEqual(new_task.category, "Home")
        self.assertEqual(new_task.percentage, "25")
        self.assertEqual(new_task.owner, "Isaac")

    def test_search(self):
        existing_task = db.DaoTasks.search(1)
        nonexistent_task = db.DaoTasks.search(4)
        self.assertIsNotNone(existing_task)
        self.assertIsNone(nonexistent_task)

    def test_update(self):
        task_to_update = copy.copy(db.DaoTasks.search(1))
        task_updated = db.DaoTasks.update(
            1,
            "Paint the wall",
            "Paint the wall of the house",
            "2023-07-01",
            "2023-07-05",
            "Home",
            "0",
            "Berenice",
        )
        self.assertEqual(task_to_update.owner, "Isaac")
        self.assertEqual(task_updated.owner, "Berenice")

    def test_delete(self):
        task_deleted = db.DaoTasks.delete(3)
        task_searched = db.DaoTasks.search(3)
        self.assertEqual(task_deleted.id, 3)
        self.assertIsNone(task_searched)
