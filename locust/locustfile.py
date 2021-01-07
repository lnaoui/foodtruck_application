import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/", name="Index")

    @task(3)
    def view_item(self):
        item = ["fruit", "fruits", "tacos", "pizza", "test", "burger", ]
        for item_id in item:
            self.client.get(f"/search?q={item_id}", name="Search")
            time.sleep(1)

#    def on_start(self):
#        self.client.post("/login", json={"username":"foo", "password":"bar"})
