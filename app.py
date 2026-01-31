from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Mini Habit Tracker")

class Habit(BaseModel):
    name: str
    emoji: str

habits: List[Habit] = []

@app.get("/")
def home():
    return {"message": "Welcome to Mini Habit Tracker"}

@app.get("/habits")
def get_habits():
    return habits

@app.post("/habits")
def add_habit(habit: Habit):
    habits.append(habit)
    return {"message": f"Habit added {habit.emoji} {habit.name}"}
