---

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Tech Stack](#tech-stack)
* [Tests](#tests)
* [Contributing](#contributing)
* [License](#license)
* [Credits](#credits)

---

## Features

Key functionalities of the project:

* Fully playable Battleship game in the terminal 
* Player name input and game setup system
* Difficulty scaling based on number of ships:

  * 1 ship → 5x5 board
  * 2 ships → 7x7 board
  * 3 ships → 9x9 board 
* Multiple ship placement without overlap
* Bonus attempt awarded for every successful hit
* Dynamic scoring system based on:

  * Ships destroyed
  * Attempts saved
  * Difficulty level
* Persistent local scoreboard saved to `score.txt`
* Menu-driven interface with:

  * Start game
  * Instructions screen
  * Scoreboard viewer
  * Exit option
* ASCII-styled menus and win/lose screens
* Improved board display with grid formatting
* Input validation for coordinates and menu choices

---

## Installation

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/battleship-cli.git
cd battleship-cli
```

### 2. Ensure Python is installed

Python 3.7+ is recommended.

Check your version:

```bash
python --version
```

### 3. Run the game

```bash
python main.py
```

No external libraries are required.

---

## Usage

After launching the program:

### 1. Select an option from the menu

```text
1. Start Game
2. Instructions
3. Scoreboard
4. Exit
```

### 2. Game setup

You will be prompted to:

```text
Enter your name
Enter number of ships (1–3)
```

This determines board size and starting attempts.

### 3. During gameplay

Enter coordinates when prompted:

```text
Enter row:
Enter column:
```

### 4. Objective

* Find and destroy all enemy ships
* Each hit grants a bonus attempt
* Score points based on efficiency and difficulty
* High scores are saved locally and viewable from the menu

---

## Tech Stack

Technologies used in this project:

* Python 3
* Standard libraries only:

  * `random` – ship placement logic
  * `time` – gameplay pacing and countdowns
  * `os` – terminal screen clearing 

---

## Tests

No automated tests are included yet.

You can manually test by running:

```bash
python main.py
```

Then verify:

* Difficulty scaling works correctly
* Multiple ships spawn without overlap
* Bonus attempts are granted on hits
* Scores are calculated and saved correctly
* Scoreboard displays top scores
* Restart and exit flows function properly

---

## Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

For major gameplay or feature changes, please open an issue first to discuss the proposal.

---

## License

MIT License

Copyright (c) 2026 SiddharthShah30

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Credits

* Built entirely using Python standard libraries
* Inspired by the classic Battleship board game
* Developed by SiddharthShah30

---
