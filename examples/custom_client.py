from locust import Locust, TaskSet, task

from myclient import CustomClient


class CustomClientLocust(Locust):
    """
    This is the abstract Locust class which should be subclassed.
    """
    def __init__(self, *args, **kwargs):
        super(CustomClientLocust, self).__init__(*args, **kwargs)
        self.client = CustomClient()


class UserBehavior(TaskSet):

    def login(self):
        user_id = "{:05}".format(int(self.locust.id))
        # login code

    def on_start(self):
        self.login()

    @task
    def task1(self):
        pass



class ClientUser(CustomClientLocust):
    task_set = UserBehavior
    # seconds after which stop client task
    stop_timeout = None
    min_wait = 2000
    max_wait = 5000