# U.S. States Guessing Game (Python, Turtle & Pandas)

This project is an interactive U.S. states guessing game built with Python, the `turtle` graphics module, and `pandas`. It was my first project working with CSV files and data analysis, designed and coded by me after earlier experience with smaller turtle games. The goal is to mix geography, simple UI, and basic data handling to show how powerful Python can be for both visualization and learning.

---

## Game Overview

- A blank map of the United States is displayed on the screen.
- The player is repeatedly prompted to enter the name of a U.S. state.
- Correct guesses are written at the correct (x, y) location on the map.
- The title bar shows how many states you have guessed correctly out of 50.
- If the player types `Exit`, the game ends and a CSV of missed states is generated so they can study them later.

This makes the game both a fun quiz and a small data‑driven learning tool.

---

## Files in this Repository

- `main.py`  
  - Sets up the `turtle.Screen`, window title, and background shape using `blank_states_img.gif`.  
  - Loads state data from `50_states.csv` using `pandas.read_csv`.  
  - Converts the `state` column into a Python list for fast membership checks.  
  - Keeps track of `guessed_states` in a list.  
  - Main loop:
    - Shows an input box titled `X/50 States Correct` and asks for another state name.
    - Normalizes input using `.title()` so it matches CSV formatting.
    - If the user types `Exit`, calculates which states were not guessed, creates a `pandas.DataFrame` from them, and writes it to `states_to_learn.csv`, then exits.
    - If the answer is a valid state name, appends it to `guessed_states`, creates a new turtle, moves it to the state’s coordinates, and writes the state name on the map.
  - Uses `turtle.mainloop()` to keep the window open at the end.

- `50_states.csv`  
  - A CSV file with three columns: `state`, `x`, and `y`.  
  - Each row stores the name of a U.S. state and the coordinates where its label should appear on the map.  
  - This file is read by `pandas` to power the game’s logic.

- `blank_states_img.gif`  
  - The outline map of the United States used as the background / shape for the turtle window.
  - The state coordinates from `50_states.csv` are aligned to this image, so labels appear at the correct positions.

- `states_to_learn.csv` *(generated at runtime)*  
  - Created when the player types `Exit`.  
  - Contains a list of all the states that were **not** guessed during that session, so the player can review them later in a spreadsheet or another tool.

---

## Requirements

- Python 3.10 or higher.
- The following Python modules:
  - `turtle` (standard library)
  - `pandas` (needs to be installed via `pip`)

 ## How to Run
Make sure the following files are in the same folder:
1.main.py
2.50_states.csv
3.blank_states_img.gif
Open a terminal or command prompt in that folder.

Run:
bash
python main.py
In the input box that appears, type the name of a U.S. state and press Enter.
Correct answers will appear as labels on the map.
The title will update to show how many states you have guessed correctly.
Type Exit at any time to stop and generate states_to_learn.csv.

You can install `pandas` with:
```bash
pip install pandas












