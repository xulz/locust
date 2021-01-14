import logging

from locust import User, TaskSet, task, constant_pacing


class CustomClient:
    pass


class UserBehavior(TaskSet):

    def login(self):
        user_id = "{:05}".format(int(self.user.id))
        logging.info(f'user id: {user_id}')
        # login code

    def on_start(self):
        self.login()

    @task
    def task1(self):
        pass


class CustomClientLocust(User):
    tasks = [UserBehavior]
    wait_time = constant_pacing(3)
    host = 'http://127.0.0.1:8089'

    def __init__(self, *args, **kwargs):
        super(CustomClientLocust, self).__init__(*args, **kwargs)
        self.client = CustomClient()
