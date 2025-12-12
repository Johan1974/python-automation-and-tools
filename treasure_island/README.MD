# Treasure Island – Python Adventure Demo

![Python Version](https://img.shields.io/badge/python-3.11-blue) 
![License: MIT](https://img.shields.io/badge/License-MIT-green) 
![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/treasure_island_ci.yml/badge.svg)

**Treasure Island** is a text-based adventure game in Python that demonstrates **interactive programming, branching logic, and clean, modular code structure**.  
While it’s a fun game, it also serves as a **portfolio example of Python fundamentals** relevant to automation, scripting, and freelance micro-projects.

**GitHub Repository:** [https://github.com/Johan1974/python-automation-and-tools/tree/main/treasure_island](https://github.com/Johan1974/python-automation-and-tools/tree/main/treasure_island)

---

## 🎮 Features

- Fully interactive console-based game with multiple story paths  
- Decision-making logic separated into **testable functions** for maintainable code  
- Input handling with `.strip()` and `.lower()` for smooth gameplay  
- ASCII-art visuals for professional presentation  
  - ASCII-art source: [https://ascii.co.uk/art](https://ascii.co.uk/art)  
- Easily extendable with new doors, challenges, or storylines  

---

## 🖥️ Example Gameplay

```text
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road, type 'left' or 'right':
> left
You've come to a lake. Type 'wait' for a boat or 'swim' to cross:
> wait
You arrive at a house with 3 doors: red, yellow, blue. Which color?
> yellow
You found the treasure! You Win!
````

---

## 🚀 Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools/treasure_island
```

2. Run the game:

```bash
python treasure.py
```

3. Follow the prompts in the terminal to navigate the adventure.

---

## 💡 Learning & Applications

This project highlights:

* **Input validation and user prompts**
* **Conditional statements and branching logic**
* **Modular Python coding practices**
* Skills directly relevant to **automation scripts, workflow tools, and interactive Python utilities**

It’s ideal for:

* Learning Python fundamentals
* Demonstrating problem-solving in a portfolio
* Workshops, educational demos, or gamified coding sessions

---

## 🔑 Key Benefits

* Interactive, engaging experience for players
* Clean and testable Python code
* Demonstrates practical coding skills to clients and collaborators
* Includes unit tests to verify decision logic and ensure reliability

---

## 🧪 Testing & CI

* Game logic is separated into functions (`choose_first_path`, `choose_second_path`, `choose_door`) for unit testing.
* Unit tests are in `treasure_island/tests/` and can be run via:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

* GitHub Actions workflow (`.github/workflows/treasure_island_ci.yml`) ensures **automated testing on push or pull request**.

---

## License

MIT License — free to use, modify, and study.

---

## Contact & Freelance

While Treasure Island is a demo, the same skills can be applied to:

* Interactive Python tools
* Custom automation scripts
* Educational or gamified Python projects

Reach out via GitHub for **freelance development** or tailored Python solutions.

