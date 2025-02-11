class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        if not isinstance(task, str):
            raise TypeError("Task must be a string.")
        if task == "":
            raise ValueError("Task cannot be an empty string.")
        self.task = task
        self.is_completed = False

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.is_completed = True