from fastapi import FastAPI
from pydantic import BaseModel
import redis

r = redis.Redis()

app = FastAPI()


class Reminder(BaseModel):
    text: str


r.set("reminders", "hey")


@app.get("/")
def read_root():
    return "Welcome!"


@app.get("/get-reminders")
def get_reminders():
    return r.get("reminders")


@app.put("/add-reminder")
def add_reminder(reminder: Reminder):
    pass
