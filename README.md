# Flappy Bird Game

![Flappy Bird Gameplay](https://github.com/yuriysyt/Flappy-Bird/raw/main/readme_images/screen_1.png)

# GitHub Repository
The source code for this project is available on GitHub: https://github.com/yuriysyt/Flappy-Bird

## Identification
- **Name:** Yuriy Sytnichenko
- **P-number:** P428742
- **Course code:** IY499

## Declaration of Own Work
I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.

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

### Running the Game
```python
python main.py
```

### Running Unit Tests
```python
python UnitTest.py
```

## Game Elements
- The bird's position is controlled by the 'W' key for jumping.
- Obstacles, represented as tubes, move from right to left.
- The game features a scrolling background to create a sense of motion.

## Libraries Used
The following libraries are used in this project:
- Pygame
- ConfigParser
- Unittest (for unit testing)

## Project Structure
- `ErrorHandling/`: Contains classes for handling various errors.
- `FileHandling/`: Handles configuration files and level completion status.
- `SortingAlgorithm/`: Sorts levels based on completion status.
- `gameloop/`: Contains game loop, calculations, input handling, drawing, and level rendering.
- `images/`: Stores game images.
- `levels/`: Defines game levels and obstacle positions.
- `menu/`: Handles main menu and level selection.
- `screen/`: Manages game display.
- `UnitTest.py`: Contains unit tests for the game.

## Unit Tests
The project includes a unit test suite in the `UnitTest.py` file. These tests cover various aspects of the game, including game loop calculations, collision detection, score calculation, and more.

To run the unit tests, navigate to the project directory and execute the following command:

```python
python UnitTest.py
```

This will run all the test cases defined in the `UnitTest.py` file.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.