# Kemaru
A game similar to Sudoku developed using Python.

The game is played as follows:
1) Each group of cells (defined by a border) can have the values from 1 to the size of the cell. (Eg: A group of size 3 cells can have the values 1 ,2 and 3)
2) No two cells around each other can have the same value. (If a cell has a value 2 then none of the six cells surrounding that cell can have the value 2)
3) Each game has 10 hints. Using a hint will either fill in a blank cell or correct an incorrectly filled cell. Hints will be shown in green.
4) The check button will highlight any cells that have been incorrectly filled. There is no limit to usage if the check function.
5) The reset button will reset the current grid.
6) The new game button will launch a new grid.
7) You can enter values by selecting a cell with your mouse and then inputting values between 1 and 5 using the numbers on your keyboard or the numberpad on your keyboard.
8) Cell values can be overwritten by selecting them and entering a new value.

Game specifications:
On first launch a message box is displayed that reveals the instructions to play the game. The game begins when you close this message box.
The game includes 9 preset grids. Each time a new game begins, a grid is selected randomly.
The initial values are randomly filled each time a game begins.
One hint is randomly filled in each time the hint button is clicked. Hints are displayed in green. There are 10 hints available per game. Hints may fill in an empty cell or correct an incorrect cell.
The new game button launches a new grid.
The reset button resets the current grid.
The timer shows how long you've been playing this grid. It resets if you reset the grid or start a new game.
The check button will turn any cells that have incorrectly filled values red. There is no limit on the check usage.
A selected cell will turn yellow until a value has been filled in or another cell is selected.
When a grid is correctly completed a pop up message will launch showing you how long you took to complete the grid and offering you the choice to start a new game or quit.
The quit button will close the game.

The game is built entirely using **pygame** except for the instructions message box and the winner message box which uses **Tkinter**.
