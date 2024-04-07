# Flappy Bird Game

![Flappy Bird Gameplay](https://github.com/yuriysyt/Flappy-Bird/raw/main/readme_images/screen_1.png)


## Introduction
This code represents a simple implementation of the Flappy Bird game using the Pygame library. The game consists of a bird that the player can control to avoid obstacles and score points.

## Installation
To run the game, ensure you have Python installed, and then install the required dependencies from the `requirements.txt` file using the following command:
```bash
pip install -r requirements.txt
```

## How to Play
- Press the 'W' key to make the bird jump.
- Navigate the bird through the obstacles to avoid collisions.
- The game ends if the bird collides with an obstacle.

## Code Structure
### `GameLoop` Class
- Initializes game parameters and handles the game loop.
- Manages user input, such as quitting the game or restarting after losing.

### `calculations` Class
- Handles game calculations, including player movement, obstacle generation, and collision detection.

### `DrawingTool` Class
- Manages drawing elements on the screen, including the background, player, obstacles, and game over screen.

### Running the Game
```python
python main.py
```

## Game Elements
- The bird's position is controlled by the 'W' key for jumping.
- Obstacles, represented as tubes, move from right to left.
- The game features a scrolling background to create a sense of motion.

## Conclusion
Feel free to explore and modify the code to enhance the game or add new features. Have fun playing Flappy Bird!