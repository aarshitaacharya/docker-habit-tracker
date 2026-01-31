from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os


app = FastAPI(title="Mini Habit Tracker")

class Habit(BaseModel):
    name: str
    emoji: str

DATA_FILE = os.getenv("HABIT_FILE", "/app/data/habits.json")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_habits() -> List[dict]:
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_habits(habits: List[dict]):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f)


@app.get("/")
def home():
    return {"message": "Welcome to Mini Habit Tracker"}

@app.get("/habits")
def get_habits():
    return load_habits()

@app.post("/habits")
def add_habit(habit: Habit):
    habits = load_habits()
    habits.append(habit.dict())
    save_habits(habits)
    return {"message": f"Habit added {habit.emoji} {habit.name}"}
