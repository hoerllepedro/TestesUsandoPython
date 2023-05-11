import pytest
from main import Task, TaskManager


class TestTaskManager:
    @pytest.fixture
    def task(self):
        return Task(1, "Fazer compras")

    def test_task_creation(self, task):
        assert task.task_id == 1
        assert task.description == "Fazer compras"
        assert not task.done

    def test_add_task(self, task):
        task_manager = TaskManager()
        task_manager.add_task(task)
        assert len(task_manager.list_tasks()) == 1
        assert task_manager.list_tasks()[0] == task

    def test_list_tasks(self):
        task_manager = TaskManager()
        task1 = Task(1, "Fazer compras")
        task2 = Task(2, "Estudar para a prova")
        task_manager.add_task(task1)
        task_manager.add_task(task2)
        tasks = task_manager.list_tasks()
        assert len(tasks) == 2
        assert tasks[0].task_id == 1
        assert tasks[0].description == "Fazer compras"
        assert not tasks[0].done
        assert tasks[1].task_id == 2
        assert tasks[1].description == "Estudar para a prova"
        assert not tasks[1].done

    def test_mark_task_done(self):
        task_manager = TaskManager()
        task = Task(1, "Fazer compras")
        task_manager.add_task(task)
        task_manager.mark_task_done(1)
        assert task.done

    def test_remove_task(self):
        task_manager = TaskManager()
        task1 = Task(1, "Fazer compras")
        task2 = Task(2, "Estudar para a prova")
        task_manager.add_task(task1)
        task_manager.add_task(task2)
        task_manager.remove_task(1)
        tasks = task_manager.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].task_id == 2
        assert tasks[0].description == "Estudar para a prova"
        assert not tasks[0].done
