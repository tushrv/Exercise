# Python Game Project

This project demonstrates a structured approach to building a Python game using packages and sub-packages for better organization and code reusability.

## Project Structure


### game/

This is the main package directory.

- **`__init__.py`**: This empty file (or with some initialization code) marks `game` as a package.

### game/characters/

This sub-package contains modules related to game characters.

- **`__init__.py`**: Marks `characters` as a sub-package.
- **`player.py`**: Module with classes/functions to define and manage player characters.
- **`enemy.py`**: Module for enemy character classes/functions.

### game/levels/

This sub-package contains modules related to game levels.

- **`__init__.py`**: Marks `levels` as a sub-package.
- **`level1.py`**: Module containing code for the first game level.
- **`level2.py`**: Module for the second game level.
