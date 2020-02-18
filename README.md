# MelonLand 

A Crossy Road inspired game developed in Python and Pygame for my ISS Assignment

## Let's Start Playing

Make sure you have Python 3 and Pygame installed then open terminal at project root and run the following: 
`python3 start.py`

## Design Choices

 - The game has been implemented using a 2 dimensional grid system
 - The entire game is scaled and proportionate to an X Factor and a Y factor that can be changed in the config file
 - The game also adjusts to different number of rows and columns which can be changed in the config file
 - The game has a level based system where every player plays a total of 5 levels each.
 - Number of obstacles and speed of obstacles increases per level
 - Obstacles start at a random location every level for each player
 - Player is awarded 5 points for crossing every lane with fixed obstacles and 10 points for crossing every lane with moving obstacles. Player is awarded 25 points for completion of a level.
 - 2 points are deducted for every second spent while playing and 50 points are deducted for dying
 - At the end of 5 levels the winner is declared
 - All point awards, penalties and number of levels can be edited from the config file
 - Both players use same arrow keys to move since only one player is moving at a time
 - Every single sprite is custom drawn by me
 - Added a start screen and an end screen 
 - Entire project follows Object Oriented Design principles
