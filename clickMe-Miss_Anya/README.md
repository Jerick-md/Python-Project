AnyaClick

A simple, fast-paced clicking game built with Python and Pygame. Test your reflexes by clicking on Anya as she floats up the screen before she disappears!



🎮 How to Play

Objective: Click on the Anya icon to score points.



Speed: Every time you successfully click Anya, her movement speed increases, making the game more challenging.



Health: You start with 5 Health.



You lose 1 health if you click the background and miss Anya.



You lose 1 health if Anya reaches the top of the screen without being clicked.



Game Over: The game ends when your health reaches 0.



🛠️ Requirements

To run this game, you need to have Python installed along with the pygame library.



Python 3.x



Pygame Library:



Bash



pip install pygame

📂 File Structure

For the game to run correctly, ensure your folder contains the following assets:



clickMe\_miss\_Anya.py (The main script)



anya.png (The target image)



backgroundimage.jpg (The game background)



cute-music-26476.mp3 (Background music)



🚀 Running the Game

Navigate to the directory containing the file and run:



Bash



python clickMe\_miss\_Anya.py

📝 Code Logic Overview

Target Class: Handles the movement, resetting, and drawing of the Anya character.



Collision Detection: Uses target.rect.collidepoint(event.pos) to check if the mouse click was inside the character's boundaries.



Game Loop: Updates the target position every 30 milliseconds and checks for "Game Over" conditions in real-time.



###### Author

Jerick T. Comedia

comediajerick22@gmail.com

09465481434

