import Task

class TaskList:
# A list object that manages multiple, related, tasks in a list  

    def __init__(self):
        # Initializes an empty task list and set the id tracker count to 0
        self.tasks = []
        self.id_tracker = 0
        self.add_task("Done - Display owner in task print", "Lindsay", "0.5")
        self.add_task("Done - Output consistant field size", "Lindsay", "1")
        self.add_task("Implement saved task lists", "Sadie", "3")
        self.add_task("Meh - Output view list headers", "Sadie", "1")
        self.add_task("Make searches case insensitive", "Sadie", "1")
        self.add_task("Verify input format, at least for duration", "Sadie", "1")


    def gen_id_number(self):
        # This neeed to check that the ID is unique to the list and loop
        # until it finds a unique ID it then returns  
        self.id_tracker += 1
        return self.id_tracker    

    def get_tasks(self):
        return self.tasks

    def add_task(self, desc, owner, dur):
        new_task = Task.Task()
        new_task.id_number   = self.gen_id_number()
        new_task.description = desc
        new_task.owner       = owner 
        new_task.duration    = dur
        self.tasks.append(new_task)

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task_id == str(task.id_number):
                 return task

    def delete_task(self, task_to_delete): # untested
        index = 0
        for task in self.tasks:
            if task_to_delete == task:
                self.tasks.pop(index)
            else:
                index += 1

    def update_task(self, task, desc, owner, dur):
         task.update_task(desc, owner, dur)

    def find_tasks_by_desc(self, string):
        matches = []
        for task in self.tasks:
            if task.description.find(string) > -1:
                matches.append(task)
        return matches

    def find_tasks_by_owner(self, string):
        matches = []
        for task in self.tasks:
             if task.owner.find(string) > -1:
                matches.append(task)
        return matches

