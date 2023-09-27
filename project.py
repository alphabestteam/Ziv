import datetime
from task import Task
from developer import Developer


class Project:
    def __init__(self, description: str, optional_tasks: list = []):
        self.description = description
        self.developer_list = []
        self.completed_tasks = []
        self.tasks_in_progress = optional_tasks
        self.start_date = datetime.date
        self.date = self.start_date.day + self.project_time()
        self.total_cost = 0
        self.completion = False

    def completed_project(self) -> None:
        """
        Checks if all the tasks of the project are done. If they are,
        the completion status will change to True
        """
        if self.tasks_in_progress is None:
            for current_task in self.completed_tasks:
                if current_task.completion is False:
                    print("Not all tasks were completed. The project isn't done!")
                    break
            else:
                self.completion = True
                print("Project completed!")

    def project_time(self) -> int:
        """
        The function calculates how many days are needed for this project
        """
        if self.tasks_in_progress is None:
            return 0
        else:
            work_days = 0
            for current_task in self.tasks_in_progress:
                work_days += current_task.work_days
            return work_days

    def project_cost(self) -> int:
        """
        The function calculates how much money is needed
        Based on the pay for each task
        """
        if self.completed_tasks is None:
            return 0
        else:
            total_cost = 0
            for current_task in self.completed_tasks:
                total_cost += current_task.total_salary
            return total_cost

    def task_finder(self, new_task: Task) -> bool:
        """
        Receives a project and iterates over all of its tasks, both completed and in progress
        If the task is associated with the project, the function returns true, otherwise false
        """
        in_project_flag = False
        # Checks if the task is in the tasks that aren't done
        for current_task in self.tasks_in_progress:
            if current_task.description == new_task.description:
                in_project_flag = True
        # Checks if the task has already been done
        for current_task in self.completed_tasks:
            if current_task.description == new_task.description:
                in_project_flag = True
        return in_project_flag

    def add_developer(self, new_developer: Developer) -> None:
        """
        The function receives a developer
        If they are already on this project, nothing will happen
        If they aren't, they'll be added
        """
        in_project_flag = False
        for current_developer in self.developer_list:
            if current_developer._developer_name == new_developer._developer_name:
                in_project_flag = True
                break
        if in_project_flag is False:
            self.developer_list.append(new_developer)

    def add_new_task(self, new_task: Task) -> None:
        """
        Receives task
        If it isn't already in this project ot another, it is added
        The task's developer
        """
        if new_task._project.description != self.description:
            print("The task is not meant for this project")
        elif self.task_finder(new_task) is True:
            print("The task is already associated with the project")
        else:
            self.tasks_in_progress.append(new_task)
            self.end_day += new_task.work_days
            self.add_developer(new_task.developer)

    def task_is_done(self, done_task: Task, task_developer: Developer) -> None:
        """
        Brings together all action that happen when a task is done
        Validates developer and marks the done
        Transfers task to completed list in both  the developer's and project's list
        """
        done_task_index = Developer.task_index(
            done_task, task_developer.tasks_in_progress
        )
        try:
            if self.tasks_in_progress[done_task_index].task_completed(task_developer):
                done_task = self.tasks_in_progress.pop(done_task_index)
                task_developer.task_completion(done_task)
                self.completed_tasks.append(done_task)
                self.total_cost += done_task.wage
                self.end_date.day += done_task.work_days
            else:
                raise Exception("The developer doesn't work on this project")
        except IndexError:
            print("The task doesn't exist in this project")

    def task_scraper(self, overdue_task: Task):
        """
        The function receives a task and a project
        If the task is overdue, it's scraped from the project and developer
        """
        done_task_index = Developer.task_index(
            overdue_task, self.tasks_in_progress
        )
        try:
            if overdue_task.task_overdue:
                self.tasks_in_progress.pop(done_task_index)
                in_developer_list = Developer.task_index(
            overdue_task, overdue_task.developer.tasks_in_progress
            )
                overdue_task.developer.tasks_in_progress.pop(in_developer_list)
        except IndexError:
            print("The task doesn't exist in this project")