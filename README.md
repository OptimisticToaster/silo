# silo

Project(s) to practice development in Python and possibly other web technologies with a team looking to learn or mentor together.

There will be initial goals such as establishing the main models and CRUD interface. Later goals will be expand for additional apps.

## Communication

Use a Discord chat for general chat purposes.

## Ticketing

Need a system that easily provides issue and bug ticketing. MantisBT has worked pretty nicely. Or if it's a small group, possibly Markdown files in a directory labeled `Ticketing`.

## Log Work

Always remember that a major focus for this project is to demonstrate how to build a project. All steps provided will be included in the work-log directory with files. Name each file by your date and time stamp. Then describe what you did sufficiently that any random user could step through this project and recreate it.

## Environment Setup

For these setups, all applications are installed. That is to mean that they are registered with the operating system. If you prefer to use decompressed folders or "portable" editions, you may need to manually configure additional items.

### Install Python

1. Open web browser to https://www.python.org/downloads/
2. Download the current version (3.10.2) appropriate for your system.
3. Install
  1. At the install screen, click to Add Python to PATH.
  2. Install Now
  3. When prompted for Disable Path Length Limit, ignore.
6. Check that the install was successful.
  1. Open command prompt
  2. Run `python --version` to check the installation was successful.

### Install Poetry

Using [Poetry](https://python-poetry.org) to manage the Python virtual enviroments.

https://dev.to/bowmanjd/getting-started-with-python-poetry-3ica#:~:text=Install%20Poetry&text=poetry%5Cbin%20is%20on%20your,environment%20variables%20for%20your%20account.%22&text=Then%20make%20sure%20%24HOME%2F.,is%20in%20your%20PATH%20variable.

1. Install Poetry (https://python-poetry.org/docs/#installation)
  1. On Linux
    1. Open terminal.
    2. `curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python`
    3. This will install Poetry to $HOME/.poetry/bin
    4. If it fails, maybe you need the command to be `python3`
    5. May need to configure path to Poetry.
      1. Run `poetry --version`. If it fails, try next step.
      2. Run `~/.poetry/bin/poetry --version`. If it succeeds, need to run next step.
      3. `export PATH=$PATH:$HOME/.poetry/bin`
  3. On Windows
    1. Open PowerShell.
    2. Change to desired download directory.
    3. `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py -UseBasicParsing).Content | python`

### Install Code Editor

Recommended is VS Code (https://code.visualstudio.com). Alternatively, could use a myriad of other text editors such as Notepad++, Atom, Brackets, CudaText.

### Install Git

Codebase will be coordinated via Github.

1. Download from https://git-scm.com/downloads
2. Run the installer, and select the default options.
  1. One exception is which editor is the default for Git to open.
  2. Set name for initial branches to `main`.

To run Git Bash, select it from the Start menu. Note that it operates like a Linux terminal (using BASH, not Windows).

For graphic interface, run Git Gui.

### Configure Git

Set username to associate with your work. It does not have to match your Github profile, but it can.

To set the username for all your Git work on the computer: 

`git config --global user.name "Some User Name"`

To set the username for a specific project, change to that project's directory:

`git config user.name "Some User Name"`

Set email address for commits.

`git config --global user.email "abc@lmnop.com"`

To set the email for a specific project, change to that project's directory:

`git config user.email "abc@lmnop.com"`

### Setup .gitignore

# Plan

1. Find team
  1. Participants
  2. Agree that we all have other lives but try to check in every couple days
  3. NO HOSTILITY! Diverse ideas are fine, but any name calling or rudeness will get a ban.
2. Plan systems
  1. Github (as needed)
  2. Messaging
  3. Ticketing system (together or on own)
3. Select project option
4. Develop roadmap
