class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.done = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.done = True
                break

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                break


# Exemplo de uso do programa

task_manager = TaskManager()

# Adicionar tarefas
task1 = Task(1, "Fazer compras")
task2 = Task(2, "Estudar para a prova")
task_manager.add_task(task1)
task_manager.add_task(task2)

# Listar tarefas existentes
tasks = task_manager.list_tasks()
for task in tasks:
    print(f"Tarefa {task.task_id}: {task.description} (Concluída: {task.done})")

# Marcar uma tarefa como concluída
task_manager.mark_task_done(1)

# Remover uma tarefa
task_manager.remove_task(2)

# Listar tarefas novamente para verificar as modificações
tasks = task_manager.list_tasks()
for task in tasks:
    print(f"Tarefa {task.task_id}: {task.description} (Concluída: {task.done})")
