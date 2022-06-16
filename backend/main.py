from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Reminder(BaseModel):
    text: str

reminders = []

@app.get("/")
def read_root():
    return "Welcome!"

@app.get("/get-reminders")
def get_reminders():
    return reminders

@app.put("/add-reminder")
def add_reminder(reminder: Reminder):
    reminders.append(reminder)
