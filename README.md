## The 24 Game
In this repository the 24 Game has been implemented in python.
The goal is for the player to enter an expression that (numerically) evaluates to 24.

Only the following operators/functions are allowed: multiplication, division, addition, subtraction 

# Requirements
To play the game only a basic python installation is necessary.
Intentionally in this implementation the use of libraries has been reduced to a minimum.

Solely the random library for the generation of pseudo-random numbers has been used.

# Start the game
To start the game just run\
```python3 run.py```

## Examples
> solve: 1 2 3 4  
> (4 * 3 * 2) + 1  
> no, this is 25  

> solve: 1 2 3 4  
> 4 * 3 * (1 + 1)  
> sorry, this is not a valid expression

> solve: 1 2 1 1  
> 12 * (1 + 1)  
> sorry, this is not a valid expression

> solve: 1 1 1 1  
> (1 + 1 + 1 + 1)!  
> sorry, this is not a valid expression

> solve: 8 4 7 4  
> (7 - (8 / 8)) * 4  
> yes, this is indeed 24