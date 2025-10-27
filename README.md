# 🐍 AI Snake Game — Smart Pathfinding Snake using Heaps & DSA

An intelligent Snake Game built in **Python** that demonstrates **data structures and algorithms** in action.  
The snake uses **heap-based shortest path logic** to find food intelligently while avoiding walls and itself.

---

## 🚀 Features
- 🎮 Minimal grid-based **UI** built with `pygame`
- 🧠 **AI-driven movement** using heaps (priority queues)
- 🧩 Modular structure with clear separation of logic (`grid`, `snake`, `ai`)
- ✅ Includes **unit tests** for validation (`tests/`)
- 📦 Object-oriented architecture (OOP principles)
- ⚡ Demonstrates DSA concepts practically (queues, heaps, pathfinding)

---

## 🧱 Project Structure
```
AI-Snake-Game/
├── src/
│   ├── main.py           # Entry point for the game
│   ├── grid.py           # Grid management and boundaries
│   ├── game.py           # Looks over the overall game
│   ├── pathfinding.py    # The AI logic (Finds shortest path)
│   ├── renderer.py       # Takes care of all the entities
│   ├── snake.py          # Snake logic (movement, growth, collision)
│   ├── food.py           # Food generation and placement
│   └── utils.py          # Helper functions
├── tests/
│   ├── test_grid.py
│   ├── test_pathfinding.py
│   ├── conftest.py
│   └── test_snake.py
├── demo/
│   └── run_demo.sh
└── requirements.txt
```

---

## 🧠 How the AI Works
The AI uses a **priority queue (heap)** to calculate the shortest path to the food:
1. Each move (up, down, left, right) is scored based on distance to food.
2. The **lowest-cost path** is chosen using a **min-heap**.
3. The AI avoids collisions by tracking snake body and walls as obstacles.
4. If trapped, fallback logic prevents random suicide moves.

This allows the snake to make human-like, optimal decisions every frame.

---

## ⚙️ Installation & Running

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AI-Snake-Game.git
cd AI-Snake-Game
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Game
```bash
python -m src.main
```

---

## 🧪 Run Tests
You can verify individual modules:
```bash
pytest tests/
```

---

## 🧰 Tech Stack
- **Language:** Python
- **Graphics:** pygame
- **Core DSA:** Heaps, Queues, BFS
- **Design:** Object-Oriented Programming

---

## 📸 Preview
<img width="749" height="788" alt="image" src="https://github.com/user-attachments/assets/7d6ace69-4a35-449e-b21f-c6621b540bd3" />


---

## 💡 Learning Outcomes
- Applying **DSA concepts** in real-time environments  
- Understanding **pathfinding algorithms**  
- Building **modular, testable** Python projects  
- Hands-on with **pygame** and event loops  

---

## 🧑‍💻 Author
**Vishal A A**  
💬 _"Making DSA fun through games and projects!"_

---

## ⭐ Contribute
If you like this project, don’t forget to **star 🌟 the repo** and share it with your friends!
