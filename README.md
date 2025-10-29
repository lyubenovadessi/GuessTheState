# 🗺️GuessTheState 
This project is an interactive U.S. States Guessing Game built with Python’s Turtle graphics module and Pandas.
The goal is to name all 50 U.S. states before time runs out! Each correct guess labels the state on the map in its proper location.

# 🎯The game features:
- A live countdown timer (default 5 minutes)
- An interactive map using turtle graphics
- Data handling with Pandas
- Automatic CSV file creation with missed states

# 🧩How It Works
 - When you run the program, a blank U.S. map appears.
 - You have 5 minutes (300 seconds) to guess all 50 states.
 - Type your guesses into the pop-up prompt.
 - If you guess correctly, the state’s name appears in the right spot.
 - If time runs out, the game stops and displays your score.
 - You can exit early by typing Exit - the game saves all missed states to missed_states_file.csv.

# ⚙️ Requirements
 - Make sure you have the following installed:
    - python 3.x
    - pandas Install Pandas (if needed): pip install pandas

# 🚀 How to Run
  - Place all files (main.py, 50_states.csv, blank_states_img.gif) in the same directory.
  - Run the script: python main.py
  - Start guessing!

# 🧠 Learning Concepts
  - Using the Turtle Graphics library for GUIs
  - Implementing timers with ontimer()
  - Using Pandas for CSV reading/writing
  - Applying loops, conditionals, and dynamic updates
  - Handling user input and game state management
