class Task:
    # Task object 

    def __init__(self):
        # Initializes the components in a new task
        self.id_number = 000
        self.description = "Super task"
        self.owner = "Mine"
        self.duration = 1

    def update_task(self, desc, owner, dur):
        self.description = desc
        self.owner = owner
        self.duration = dur

