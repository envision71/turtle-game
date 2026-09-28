# Turtle Goal Game

A small Python arcade game built with the standard `turtle` graphics library. The player controls a turtle and scores points by passing through goals circles placed across the screen.

## Features

- Simple turtle-based gameplay
- Randomized or shaped goal layouts
- Score tracking on screen
- Easy to run with Python's built-in libraries

## Project Structure

- `main.py` - entry point for the game
- `game.py` - instructor-owned board setup, goal placement, and scoring
- `classroom.py` - student player and movement code
- `drawer.py` - draws each goal circle
- `writer.py` - displays the current score

## Concepts

- The instructor configures the board in `main.py`.
- The student writes simple turtle commands in `classroom.py` using the provided `Player` class.
- `Player` inherits from `turtle.Turtle` and takes no arguments.
- Each goal scores once when the player reaches it; the game updates the score automatically.

## Modes

- Mode 0 places dots randomly placed around the screen
- Mode 1 makes a random polygon based on the seed
- Mode 2 makes a trapazoid
- Modes +3 make polygons with the mode number being the amount of size

## Requirements

- Python 3
- Standard library module: `turtle`

## Notes

Needs to have a launch.json to set default file to run. Otherwise will need to swap to main.py before every run.
