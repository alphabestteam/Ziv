"""
Cannot import task model. It causes circular imports
"""


class Developer:
    def __init__(self, developer_name):
        self._developer_name = developer_name
        self.total_salary = 0
        self.completed_tasks = []
        self.tasks_in_progress = []
        self.seniority = 1

    @staticmethod
    def task_index(input_task, task_list: list) -> int:
        """
        Receives a task and a task list
        Returns the index of the task
        """
        for current_index in range(len(task_list)):
            if task_list[current_index]._description == input_task._description:
                return current_index
        return -1

    def task_completion(self, current_task) -> None:
        """
        The function receives a developer and an index of a task inside his task list
        If it is completed, it pops it out of the list
        The function then changes the developer's salary and seniority accordingly
        Finally, the developer adds them to the completed task list
        """
        current_task_index = self.task_index(current_task, self.tasks_in_progress)
        if current_task_index < 0:
            raise IndexError(
                "The index doesn't exist. The developer doesn't have this task"
            )
        elif self.tasks_in_progress[current_task_index].completion:
            completed_task = self.tasks_in_progress.pop(current_task_index)
            self.seniority += completed_task.level
            self.total_salary += completed_task.wage
            self.completed_tasks.append(completed_task)
