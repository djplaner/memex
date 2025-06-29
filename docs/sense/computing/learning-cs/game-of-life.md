---
backlinks:
- title: Theory of computing
  url: /sense/computing/learning-cs/theory-of-computing.html
tags:
- game-of-life
- theory-of-computing
- computing
- computer-science
title: Game of life
type: note
---
Playing with Conway's Game of Life.

## GoL rules

Assumes 8-connected neighbours with the following rules:

1. **Underpopulation**: A live cell that has < 2 live neighbouring cells will die
2. **Survival**: A live cell that has 2-3 live neighbouring cells will remain alive
3. **Overpopulation**: A live cell with more than 3 live neighbours will die
4. **Reproduction**: A dead cell with exactly 3 live neighbours will become alive

## Resources

- [Lifewiki](https://conwaylife.com/wiki/Main_Page) - includes a collection of over 5000+ patterns