# Smart-Dots
My first implementation of a genetic algorithm using python and pygame. Inspired by this [video](https://youtu.be/BOZfhUcNiqk)

## About

This simulation spawns the dots in a specific point on the canvas, one generartion at a time. Each dot's purpose is to reach a goal (a green rectangle on the left side of the canvas). Every dot object has an array of random direction, and each frame it follows that direction for a given step_length, if a dot runs into a wall or an obstacle or it runs out of random directions to follow, it dies. Each time a generation reaches the goal an obstacle spawns and the later generations will have to learn how to overcome it.

### Fun Fact

I have made some changes to the generic genetic algorithm just to make the simulation more fun to watch, for example depending on the performance of the last generation's best dot, the dots of the current generation might exactly follow his directions up until a certain point and then "explode" in a swarm of dots. Also sometimes when creating the new generations some dots are initialized as "pioneer dots", this means that they will go explore either straight up down right or left

## Simulation Parameters

The main simulation parameters can be set in the Globals.py file, they are all pretty self-explanatory.

## Requirements

The [pygame](https://www.pygame.org) module is required, to install it:

  ```bash
  sudo pip install pygame
  ```

## Running the simulation

To run the simulation simply run:

```bash
  python smart-dots.py
  ```

## TODO

Sometimes dots reach a position that the best dot goes through in less steps, then for example they die by crashing on the walls, it would be interesting to try to optimize the best dot's directions so that it doesn't waste any time moving around and goes as straight as possible toward the goal.
