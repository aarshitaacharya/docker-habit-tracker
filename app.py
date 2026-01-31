from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import os, json

app = FastAPI(title="Mini Habit Tracker 💖")

# ---------- API ----------
class Habit(BaseModel):
    name: str
    emoji: str

DATA_FILE = os.getenv("HABIT_FILE", "/app/data/habits.json")
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_habits() -> List[dict]:
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_habits(habits: List[dict]):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f)

@app.get("/api/habits")
def get_habits():
    return load_habits()

@app.post("/api/habits")
def add_habit(habit: Habit):
    habits = load_habits()
    habits.append(habit.dict())
    save_habits(habits)
    return {"message": f"Habit added {habit.emoji} {habit.name}"}

# ---------- FRONTEND ----------
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
