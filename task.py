import datetime, random
from developer import Developer

# Since I can't use the internet, I'm not sure if datetime is the right module for dates or how to work with it
# Therefore, the dates might not work


class Task:
    def __init__(
        self, description: str, work_days: int, project, developer: Developer = 0
    ) -> None:
        self._description = description
        self._project = project
        if type(work_days) != int or work_days < 0:
            raise TypeError("Workdays must be a round, positive integer.")
        else:
            self.work_days = work_days
        self.start_date = datetime.date
        self.end_date = self.start_date.day + work_days
        self.level = random.randint(1, 5)
        self.developer = developer
        if self.developer == 0:
            self.wage = 0
        else:
            self.wage = developer.seniority * (self.level / self.work_days)
        self.completion = False
        developer.tasks_in_progress.append(self)

    def task_completed(self, developer: Developer) -> bool:
        """
        Changes the completion status of the task to True,
        only if the developer that's attempting to make the change is the on assigned to the task
        """
        if developer._developer_name == self.developer._developer_name:
            self.completion = True
            return True
        else:
            return False

    def task_overdue(self):
        """
        Check if the project is overdue
        """
        if self.end_date - self.start_date > self.work_days:
            return True 
        else:
            return False