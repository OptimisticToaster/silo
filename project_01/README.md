# Project 1: Quoter

Interface: Console

Purpose: Display famous quotes. Initially, provide a random quote, and later maybe more direction from the user.

## Structure

Database: Initially JSON, then possibly SQLite.

Programming Language: Python 3.10.2

Operating System: Windows

## Environment Setup

Most of the setup occurred with setting up the over-arching Silo system. The code base is fine to mix (ie Git), but want a separate environment for the application.

### Create Virtual Environment

Using [Poetry](https://python-poetry.org) to manage the virtual enviroment for this project.

https://dev.to/bowmanjd/getting-started-with-python-poetry-3ica#:~:text=Install%20Poetry&text=poetry%5Cbin%20is%20on%20your,environment%20variables%20for%20your%20account.%22&text=Then%20make%20sure%20%24HOME%2F.,is%20in%20your%20PATH%20variable.

1. Install Poetry
  1. On Linux
    1. Open terminal.
    2. `curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python`
    3. **Not tested any further**
  3. On Windows
    1. Open PowerShell.
    2. Change to desired download directory.
    3. `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py -UseBasicParsing).Content | python`
  4. Left Off

