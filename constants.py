README = """
# {}
### URL
The URL for the source code of this project is available here: {}
### Assignment Writeup
#### Intentions

#### Input Work Done

#### Output Results

#### Approach

#### Thoughts on the results

### Dependencies
{}

### Usage
{}

### References

"""

FLASK_TEMPLATE = """
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
"""

FILE_HEADER = """
######################################################################
# Project           : {}
#
# Program name      : {}
#
# Author            : {}
#
# Date created      : {}
#
# Purpose           : {}
#
# Credit            :
#
# Use                                    Source
#
# Docstring template                     https://www.phusewiki.org/wiki/index.php?title=Program_Header
# Template creation                      https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal4/ 
#
# Revision History  :
#
# Date        Author              Ref    Revision 
# {}  {}      1     Created prototype of project.
#
######################################################################
"""

PROJECT_HELP = "Set the name of the assignment. Will be overwritten with any flag that automatically sets project name."

SUPPORTED_FILE_HELP = """
Main file that will be created. Note that only Python is currently supported.\n

Default:
*.py    :        <project>.py
*.html  :        <project>.html
                 <project>.css
                 <project>.js
*.c     :        <project>.c 
"""

FLASK_HELP = "Is this project using flask? Only works when language is python."

PURPOSE_HELP = """
Purpose of program that will be placed in --file

Default:

    Project created without default. Will decide what to put here later.
    
"""
AUTHOR_HELP = """
    Author of program.

    Default:

        Author
"""

URL_HELP = "URL for the project's github or other repository."

ERR_LANGAUGE = "ERR: programming language must be 'python', 'HTML', 'C'"
ERR_PROJECT_EXISTS = "ERR: project directory {} already exists."
NO_AUTO_OR_PROJECT_NAME = "ERR: Must specify either --auto or --project"

DEPENDENCY_PYTHON = "* [python3](https://www.python.org/download/releases/3.0/)\n"
DEPENDENCY_FLASK = "* [Flask](http://flask.pocoo.org/)\n"
USAGE_PYTHON = """
```bash
$ python3 {}.py language [--project] [--flask] [--auto] [--file] [--purpose] [--author] [--URL]
```
"""
USAGE_FLASK = """
Now navigate to `localhost:5000` in your favorite web browser!
"""

DATES = """
Journal name and main file will be named in accordance to the highest date less than the current date.
"""

MAIN_URL = "https://canvas.instructure.com"
COURSES_URL = MAIN_URL + "/api/v1/courses"
MODULES_URL = COURSES_URL + "/{}/modules" # course id goes in the brackets
PROJECT_NAME = "Journal{}"
