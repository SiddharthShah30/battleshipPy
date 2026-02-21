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
* Random ship placement with horizontal or vertical orientation 
* Grid-based coordinate guessing system
* Visual board updates showing hits and misses
* Limited attempts system for challenge-based gameplay
* Menu-driven interface with:

  * Start game
  * Instructions screen
  * Exit option
* ASCII-styled banners for menus and win/lose screens
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

```
1. Start Game
2. Instructions
3. Exit
```

### 2. During gameplay

You will be prompted to enter:

```
Enter row:
Enter column:
```

Coordinates must be within the board range.

### 3. Objective

* Guess the hidden ship’s coordinates
* Hit all parts of the ship before attempts run out
* Win if the entire ship is sunk

After each game you can restart or return to the main menu.

---

## Tech Stack

Technologies used in this project:

* Python 3
* Standard libraries only:

  * `random` – ship placement logic
  * `time` – gameplay pauses and countdowns
  * `os` – terminal screen clearing 

---

## Tests

No automated tests are included yet.

You can manually test by running:

```bash
python main.py
```

Then verify:

* Menu loads correctly
* Ship placement varies each game
* Board updates with hits and misses
* Input validation prevents invalid coordinates
* Restart and exit options function correctly

---

## Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

For larger gameplay changes, please open an issue first to discuss the proposal.

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

Tell me what you want next.
