# Hangman Quiz Game

## Project Description
This is a simple Hangman-style quiz game where players must save "Nadhif" by answering questions correctly. The game is part of the **30 Days Marathon Python Code** challenge organized by **Bagus (Gede Tanock)**, specifically on **Day 14**.

### Game Rules:
1. You must answer the given question correctly to save Nadhif.
2. Nadhif has **6 lives**.
3. Each incorrect answer **reduces Nadhif's life by 1**.
4. The game continues until either:
   - The player answers correctly and wins the game.
   - The player makes 6 mistakes, and Nadhif is not saved.
5. After each question, the player can choose to continue or exit.

## Installation & Usage
### Requirements:
- Python 3.x
- The `bahan` module (custom module used for game assets like Hangman visuals and messages)
- `random` module (built-in)

### Running the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hangman-quiz-game.git
   ```
2. Navigate to the project folder:
   ```bash
   cd hangman-quiz-game
   ```
3. Run the script:
   ```bash
   python hangman.py
   ```

## File Structure
- `hangman.py`: The main Python script that runs the game.
- `bahan.py`: Main Program - Contains game assets such as Hangman visuals and messages.
- `pertanyaan.txt`: A text file containing quiz questions.
- `jawaban.txt`: A text file containing correct answers corresponding to `pertanyaan.txt`.

## Contribution
Feel free to contribute by improving the game, adding more questions, or enhancing the visuals!

## For Future Improvements
1. Add a Graphical User Interface (GUI):
Use a library like Tkinter or Pygame to make the game more interactive with buttons, images, and a better user experience.
2. Database Integration:
Store questions and answers in a database (like SQLite) instead of text files, allowing for easier updates and additions of new questions.
3. Multiple Difficulty Levels:
Add different difficulty levels (easy, medium, hard) to vary the number of questions, time limits, or the complexity of the questions.
4. Timer for Each Question:
Introduce a countdown timer for each question to add an element of pressure and excitement to the game.
5. Track High Scores:
Implement a system that tracks players’ high scores and displays a leaderboard.


## License
This project is open-source under the MIT License.

