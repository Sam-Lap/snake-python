# Snake Game Project
## Description
This is a classic Snake Game implemented in Python using the Pygame library. Players are challenged to guide a snake through a series of obstacles while collecting food. As the snake eats, it grows longer and faster, adding a layer of complexity and excitement to the gameplay. The objective is simple yet captivating: accumulate the highest score possible without colliding with the walls or the snake's own growing body.

## Features
- **Simple User Interface:** The game boasts a minimalist and easy-to-navigate user interface, ensuring a seamless gaming experience.
- **Dynamic Snake Movement:** Player navigates the snake across the screen using the arrow keys, providing an engaging and interactive experience.
- **Progressive Difficulty:** As the snake consumes food, it grows in length, making the game increasingly challenging and engaging.
- **Score Tracking and Display:** The player's score is dynamically updated, reflecting the number of foods the snake has consumed.
- **Replayability:** Post-game, players are given the option to either quit or restart the game, enhancing user engagement and replay value.


## Requirements and Setup
### System Requirements
- Installation of Python on computer. 
### Dependencies
- This game relies on the *Pygame* library for its game mechanics and graphical interface. Pygame can be easily installed using pip by running the following command in your terminal or command prompt:

   `pip install pygame`

### Setup
#### 1. Open Terminal or Command Prompt
- On macOS or Linux, open the Terminal. On Windows, open Command Prompt or Git Bash.
#### 2. Clone the Repository
- Navigate to the directory where you want to clone the game repository. 
- Run the following command to clone:

   `git clone https://github.com/Sam-Lap/snake-python.git`
   
#### 3. Navigate to the Repository:
- Change your directory to the cloned repository.
   
   `cd snake-python`

#### 4. Run the Game:
- Start the game by running the following command in your terminal or command prompt:

   `python snake.py`

## How to Play
- Use the arrow keys (↑, ↓, ←, →) to control the direction of the snake.
- Eat the green blocks (food) that appear randomly on the screen.
- Each time the snake eats food, it grows longer, and the score increases.
- Avoid colliding with the walls or the snake's own body.
- Press 'Q' to quit the game or 'C' to play again after losing.

## Game Mechanics
- The game window is set to 600 x 400 pixels.
- The snake moves at a consistent speed, determined by the `snake_speed` variable, which can be adjusted for different levels of difficulty.
- The food blocks spawn randomly across the screen within the playable area, never inside the snake.
- The player's score is tracked and incremented with each piece consumed. 

## Technical Implementations
- Employs basic game development concepts:
   - Game Loops
   - Score Keeping
   - Collision Detection
   - Random Number Generation *(random module)*
   - Object Movement + Control *(Pygame)*
   - Graphics Rendering *(Pygame)*
   - Frame Rate / Speed Control *(Pygame)*
   - Event Handling *(Pygame)*

## Contact
Samuel Lapidot

[Project Link](https://github.com/Sam-Lap/snake-python)
