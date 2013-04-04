import TaskList

class TaskListController:
    # Handles data provided by the user to modify and view 
    # tasks in the TaskList
    
    def __init__(self):
        # Creates a TaskList object and the ability to
        # edit the new object
        self.task_list = TaskList.TaskList()

    def get_list(self):
        return self.task_list.get_tasks()

    def add_task(self, desc, owner, dur):
        self.task_list.add_task(desc, owner, dur)
        return True

    def get_task_by_id(self, task_id):
        return self.task_list.get_task_by_id(task_id)

    def update_task(self, task, desc, owner, dur):
        self.task_list.update_task(task, desc, owner, dur)

    def delete_task(self, task):
        self.task_list.delete_task(task)

    def find_tasks_by_desc(self, string):
        return self.task_list.find_tasks_by_desc(string)

    def find_tasks_by_owner(self, string):
        return self.task_list.find_tasks_by_owner(string)

