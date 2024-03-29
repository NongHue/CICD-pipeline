
from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """HM on start is called when the Taskset is starting"""
        pass
    def on_stop(self):
        """.. on stop is called when the Taskset is stopping"""
        pass
    @task(1)
    def scale(self) :
        self.client.get("https://huent15-flask-app.azurewebsites.net")
    @task(2)
    def predict(self):
        self.client.post("https://huent15-flask-app.azurewebsites.net/predict",json= {"content":"2"})
