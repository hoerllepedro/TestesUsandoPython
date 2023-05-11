import pytest
from main import Task, TaskManager

class TestTaskManager:
    def test_add_task(self):
        task_manager = TaskManager()
        task = Task(1, "Nova tarefa")
        task_manager.add_task(task)
        assert task_manager.list_tasks() == [task]

    def test_list_tasks(self):
        task_manager = TaskManager()
        task1 = Task(1, "Tarefa 1")
        task2 = Task(2, "Tarefa 2")
        task_manager.add_task(task1)
        task_manager.add_task(task2)
        assert task_manager.list_tasks() == [task1, task2]

    def test_mark_task_done(self):
        task_manager = TaskManager()
        task = Task(1, "Tarefa")
        task_manager.add_task(task)
        task_manager.mark_task_done(1)
        assert task.done is True

    def test_remove_task(self):
        task_manager = TaskManager()
        task1 = Task(1, "Tarefa 1")
        task2 = Task(2, "Tarefa 2")
        task_manager.add_task(task1)
        task_manager.add_task(task2)
        task_manager.remove_task(1)
        assert task_manager.list_tasks() == [task2]
