from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import redis

r = redis.Redis()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
