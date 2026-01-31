const API_URL = "/api/habits";

const habitList = document.getElementById("habit-list");
const addBtn = document.getElementById("add-btn");
const habitNameInput = document.getElementById("habit-name");
const habitEmojiInput = document.getElementById("habit-emoji");

// Load habits from API
async function loadHabits() {
    const res = await fetch(API_URL);
    const habits = await res.json();
    habitList.innerHTML = "";
    habits.forEach(habit => {
        const li = document.createElement("li");
        li.textContent = `${habit.emoji} ${habit.name}`;
        habitList.appendChild(li);
    });
}

// Add habit
addBtn.addEventListener("click", async (e) => {
    e.preventDefault(); 
    
    const name = habitNameInput.value;
    const emoji = habitEmojiInput.value;

    if (!name || !emoji) {
        alert("Enter name and emoji!");
        return;
    }

    await fetch("/api/habits", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, emoji })
    });

    habitNameInput.value = "";
    habitEmojiInput.value = "";
    loadHabits();
});

// Initial load
loadHabits();
