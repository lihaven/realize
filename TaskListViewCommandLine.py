import TaskListController
import os

class TaskListViewCommandLine:
    
    def __init__(self):
        # Initiates a new TaskListController
        # Functional statements:
        self.controller = TaskListController.TaskListController()
        # Visual statements:
        self.line_break = "----------------------------------------"
        self.field_len_4 = "    "
        self.field_len_6 = "      "
        self.field_len_8 = "        "
        self.field_len_16 = "                "
        self.menu_options   = ["1. View Tasks  |", 
                               "2. Add Task  |",
                               "3. Update Task  |", 
                               "4. Delete Task  |", 
                               "5. Search Tasks  |", 
                               "0. Quit"]
        self.update_options = ["1. Update Description  |",
                               "2. Update Owner  |",
                               "3. Update Duration  |",
                               "0. Save Update"]
        self.search_options = ["1. Search by Description  |",
                               "2. Search by Owner"]

#-----------------------------------------------------------------------------
# Menu Functions
#-----------------------------------------------------------------------------
    def menu(self):
        # Outputs the menu options for the user, takes user
        # input, and sends user to the desired task in the 
        # program
        action = self.menu_output(self.menu_options)
        
        if   action == "1":
            self.print_list(self.controller.task_list.tasks)
            return True
        elif action == "2":
            self.add_task()
            return True
        elif action == "3":
            self.update_task()
            return True
        elif action == "4":
            self.delete_task()
            return True
        elif action == "5":
            self.search_list()
            return True
        elif action == "0":
            os.system("clear") 
            return False
        else:
            print "Please choose a listed option."
            return True

    def menu_output(self, action_list):  #menu(), update_task()
        # Outputs all the visual elements of the menu, and calls for user 
        # input as well
        print self.line_break
        for action in action_list:
            print action,
        print ""
        action = self.menu_get_user_input()
        print self.line_break
        return action

    def menu_get_user_input(self):
        return raw_input("Command: ")


#-----------------------------------------------------------------------------
# View List Functions
#-----------------------------------------------------------------------------

    def print_list(self, task_list):        # Prints the list of tasks in a readable format
        print ("|" + self.gen_task_field_name("ID", self.field_len_4) +
               "|" + self.gen_task_field_name("Time", self.field_len_4) +
               "|" + self.gen_task_field_name("Owner", self.field_len_4) +
               "| " + self.gen_task_field_name("Description", self.field_len_4))
        if task_list != None:
            for task in task_list:
                print self.print_task(task)
        else:
            print "There were no tasks found."
    
    def print_task(self, task): #print_list, update_task
        # this is named stupidly because it doesn't print the task
        #mmaybe it should
        return ("|" + self.gen_task_field_name(str(task.id_number), self.field_len_4) +
                "|" + self.gen_task_field_name(str(task.duration), self.field_len_4) + 
                "|" + self.gen_task_field_name(str(task.owner), self.field_len_8) + 
                "| " + str(task.description))


#-----------------------------------------------------------------------------
# Add Task Functions
#-----------------------------------------------------------------------------
    def add_task(self):
        print "--------------- New Task ---------------"
        desc  = self.input_task_field(self.gen_task_field_name("Description", self.field_len_16))
        owner = self.input_task_field(self.gen_task_field_name("Owner", self.field_len_16))
        dur   = self.input_task_field(self.gen_task_field_name("Duration", self.field_len_16))
        self.controller.add_task(desc, owner, dur)

    def gen_task_field_name(self, field, field_len):
        return (field_len[:(len(field_len) - len(field))] 
                + field + " ")
    
    def input_task_field(self, field):
        return raw_input(field)
      
    # update functions
    def update_task(self):
        task_id = self.input_task_field(self.gen_task_field_name("ID", self.field_len_16))
        task = self.controller.get_task_by_id(task_id)
        if task != None:
            print self.print_task(task)
            self.while_user_updates(task)
        else: 
            print "No task with that ID exists."
        
    def while_user_updates(self, task):
        #tid   = task.id_number
        desc  = task.description
        owner = task.owner
        dur   = str(task.duration)
        continue_update = True
        while continue_update: 
            action = self.menu_output(self.update_options)
            if   action == "1":
                desc = self.update_task_field("Description", desc)
            elif action == "2":
                owner = self.update_task_field("Owner", owner)
            elif action == "3":
                dur = self.update_task_field("Duration", str(dur))
            elif action == "0":
                self.controller.update_task(task, desc, owner, dur)
                continue_update = False # Just to be extra safe
                break
            else:
                print "Please choose a listed option"
        
    def update_task_field(self, field, value):
        print "Current Value: " + value
        task_action = raw_input(
            "Would you like to change this tasks " + field + "? (y/n) ")
        if task_action == "y":
            return self.input_task_field(self.gen_task_field_name(field, self.field_len_16))
        elif task_action == "n":
            print filed + " unchanged."
            return value
        else: 
            print "Valid options are y or n."

#-----------------------------------------------------------------------------
# Delete Task Functions
#-----------------------------------------------------------------------------
    def delete_task(self):
        task_id = self.input_task_field(self.gen_task_field_name("ID", self.field_len_16))
        task = self.controller.get_task_by_id(task_id)
        if task != None:
            print self.print_task(task)
            if raw_input("Would you like to delete this task? (y/n)") == "y":
                self.controller.delete_task(task)
        else: 
            print "No task with that ID exists."



#-----------------------------------------------------------------------------
# Search List Functions
#-----------------------------------------------------------------------------
    def search_list(self):
        action = self.menu_output(self.search_options)
        string = raw_input("Search for: ")
        if   action == "1":
            matches = self.find_tasks_by_desc(string)
        elif action == "2":
            matches = self.find_tasks_by_owner(string)
        else:
            print "You can search by that field."
        self.print_list(matches)
        
    def find_tasks_by_desc(self, string):
        return self.controller.find_tasks_by_desc(string)

    def find_tasks_by_owner(self, string):
        return self.controller.find_tasks_by_owner(string)



    
        

