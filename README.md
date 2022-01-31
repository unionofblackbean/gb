# GB - MCDR Git Backup Plugin

## Installation

1. Install Python 3.9.10. (This plugin is developed with Python 3.9.10, other
   versions of Python may work but they are not tested, we do not assume
   responsibility or liability for any loss or damage.)

2. Clone the repository to MCDR's plugin directory.

   ```sh
   cd [MCDR path]/plugins # cd into MCDR's plugin directory
   git clone https://github.com/unionofblackbean/gb.git
   cd gb
   ```

3. Install dependencies.

   ```sh
   pip3 install -r requirements.txt
   ```

## Development Guideline
This project follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
`Pylint` is used for linting, `yapf` and `isort` are used for formatting.

### IDE/Editor Setup

#### Visual Studio Code

1. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Config file for Visual Studio Code (.vscode/settings.json) already present in
the project source. Required extension features should be enabled once the
project is opened.

You should format modified source files with `yapf` and `isort`.
