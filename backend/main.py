from fastapi import FastAPI
from pydantic import BaseModel
import redis

r = redis.Redis()

app = FastAPI()


class Reminder(BaseModel):
    text: str


@app.get("/")
def read_root():
    return "Welcome!"


@app.get("/get-reminders")
def get_reminders():
    return r.smembers("reminds")


@app.put("/add-reminder")
def add_reminder(reminder: Reminder):
    r.sadd("reminds", reminder.text)
