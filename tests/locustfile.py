from locust import between, HttpLocust, TaskSet, task

from configuration import email, password, dataset_uuid, catalog_uuid, distribution_uuid


class UserBehavior(TaskSet):
    token = ''

    def on_start(self):
        # 1. Prepare
        url = '/tokens'
        headers = {}
        req_body = ({"email": email, "password": password})
        # 2. Run
        res = self.client.post(url, headers=headers, json=req_body)
        # 3. Set token
        res_body = res.json()
        self.token = res_body["token"]

    @task(1000)
    def get_repository_detail(self):
        # 1. Prepare
        url = f'/'
        headers = self.auth_headers()
        # 2. Run
        self.client.get(url, headers=headers)

    @task(1000)
    def get_catalog_detail(self):
        # 1. Prepare
        url = f'/catalog/{catalog_uuid}'
        headers = self.auth_headers()
        # 2. Run
        self.client.get(url, headers=headers)

    @task(1000)
    def get_dataset_detail(self):
        # 1. Prepare
        url = f'/dataset/{dataset_uuid}'
        headers = self.auth_headers()
        # 2. Run
        self.client.get(url, headers=headers)

    @task(1000)
    def get_distribution_detail(self):
        # 1. Prepare
        url = f'/distribution/{distribution_uuid}'
        headers = self.auth_headers()
        # 2. Run
        self.client.get(url, headers=headers)

    @task(5)
    def create_catalog(self):
        # 1. Prepare
        url = f'/catalog'
        headers = self.auth_headers()
        data = load_file("catalog.ttl")
        # 2. Run
        self.client.post(url, headers=headers, data=data)

    @task(5)
    def create_dataset(self):
        # 1. Prepare
        url = f'/dataset'
        headers = self.auth_headers()
        data = load_file("dataset.ttl")
        # 2. Run
        self.client.post(url, headers=headers, data=data)

    @task(5)
    def create_distribution(self):
        # 1. Prepare
        url = f'/distribution'
        headers = self.auth_headers()
        data = load_file("distribution.ttl")
        # 2. Run
        self.client.post(url, headers=headers, data=data)

    def auth_headers(self):
        return {'Authorization': f'Bearer {self.token}'}


def load_file(file_name):
    return open(f'./data/{file_name}', 'r').read()


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 1.0)
