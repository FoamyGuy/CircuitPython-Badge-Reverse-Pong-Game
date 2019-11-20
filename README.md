# CircuitPython-Badge-Reverse-Pong-Game

This is a simple example game. It's like the classic pong, but you play as the ball instead of a paddle. Your job is to guide the ball up and down using the d-pad as needed to make sure you hit the paddles.

The game is broken into two files: 

 - code.py - contains the main loop, screen setup, and high-level game updating
 - pong_helpsers.py - contains some helper objects for the game elements. code.py imports, creates, and updates these objects to make the game chooch.
 
I have done my best to thoroughly comment both python files. Intention is that these scripts are basic enough for beginners to use to learn about building games with CircuitPython.

If you have additional questions or comments about this project please feel free to open an issue here on github.

# Programming Exersises:
If you are trying to practice programming games with CircuitPython here are a few basic exersises that you could try out by modifying the code in this project:

 - Change the FPS setting in code.py and observe how higher and lower values impact the game play. 
 - Change the code to increment the FPS setting the longer the player is "alive" so the game gets faster (harder) over time like Tetris. Don't forget to reset FPS back to default when the player "loses" by failing to hit a paddle.
 - Manipulate the size of the paddles and/or balls, observe the results. Is the game easier or harder if you make the ball bigger or smaller? Same question for the paddles.
 - Manipulate the speed that the ball moves at by changing how many pixels it moves by during each game update iteration.
 - Manipulate the speed that the paddles move at by changing how many pixels they move during each game update iteration.

# Quick Sample Video of Gameplay:
[![Youtube Video Link](https://github.com/FoamyGuy/CircuitPython-Badge-Reverse-Pong-Game/blob/master/yt_thumb.png?raw=true)](https://www.youtube.com/watch?v=y5f90KyQ64g)