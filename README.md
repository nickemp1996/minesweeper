# minesweeper
My implementation of Minesweeper using Python
## Setup
To play a game of minesweeper you will need to clone the repository to your machine. You may need to install the Pillow library as this is used for displaying GIFs. Once on your machine, follow the "install-a-new-font.txt" instructions inside the DS-Digital folder to get the DS-Digital font installed on your machine. Once that is comlete simply run 'python main.py' to begin the game.
## Launch Game and Select Difficulty
When the gae launches you will be asked to choose a difficulty. The available options are Beginner, Intermediate, and Expert.
### Beginner Mode
Beginner mode will create a 9x9 playing field with 10 mines. One of the cells will be randomly selected to be a secial surprise.
### Intermediate Mode
Intermediate mode will create a 16x16 playing field with 40 mines. One of the cells will be randomly selected to be a secial surprise.
### Expert Mode
Expert mode will create a 16x30 playing field with 99 mines. One of the cells will be randomly selected to be a secial surprise.
## Playing
When the game field is rendered you can begin interacting with the cells. A left-click on a cell will open that cell. If the cell has no neighboring cells that are mines then all non-mine cells up to cells with neighboring cells that are mines will be opened. If a cell with a neighboring mine is opened then the number of neighboring mines will be displayed. If the cell is a mine, you lose and will be kindly blown up. A right-click will flag a cell. Flagging a cell indicates that you believe a mine is at that location; a subsequent right-click of a flagged cell will remove the flag. A flagged cell must be unflagged to be interacted with. A player is given the same number of flags as there are mines in the field. An indicator on the top-left of the screen will indicate remaining flags. When all non-mine cells have been cleared, you win! Congradulations, your prize is a small boost to your ego. At the end of a game you can either try again or quit. If you decide to try again you will be asked to select the difficulty.
## Special Surprise
In all modes, one cell is randomly selected to be a surprise cell. If the surprise cell is clicked you will be treated with the lovliests of GIFs. The cell must be clicked by a player to be activated; if the cell is opened as a result of a cascade open from opening an empty cell then the surpise is void for that game.
# Have Fun!
## And enjoy the surprise ;)