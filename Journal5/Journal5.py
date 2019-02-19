
######################################################################
# Project           : Journal4
#
# Program name      : create.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 02/17/2019
#
# Purpose           : Project to create other LIS351 journal templates.
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
# 02/17/2019  Evan Kivolowitz      1     Created prototype of project.
#
######################################################################
import argparse
import textwrap
import os
import constants
import sys
import datetime
import json
def getDate():
    curr = datetime.date.today()
    return curr.strftime("%m/%d/%Y")

def handleC(args):
    pass
def handlePython(args):
    project = args.project
    program_name = "main.py"
    if args.file:
        program_name = args.file
    if args.dated:
        program_name = args.project + ".py"
    author = "Author"
    if args.author:
        author = args.author
    date_created = getDate()
    purpose = ""
    if args.purpose:
        purpose = args.purpose
    
    output = constants.FILE_HEADER.format(project, program_name, author, date_created, purpose, date_created, author)

    if args.flask:
        output += constants.FLASK_TEMPLATE
    with open("{}/{}".format(project, program_name), 'w') as f:
        f.write(output)
    

def handleHTML(args):
    pass
def createREADME(args):
    project_name = args.project
    URL = ""
    if args.URL:
        URL = args.URL
    dependency = ""
    usage = ""
    if args.language == "python":
        dependency += constants.DEPENDENCY_PYTHON
        usage += constants.USAGE_PYTHON
        if args.flask:
            dependency += constants.DEPENDENCY_FLASK
            usage += constants.USAGE_FLASK
    with open("{}/{}".format(args.project, "README.md"), 'w') as f:
        f.write(constants.README.format(project_name, URL, dependency, usage))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("project")
    parser.add_argument("language")
    parser.add_argument("--flask", action="store_true", help=constants.FLASK_HELP)
    parser.add_argument("--dated", action="store_true", help=constants.DATES)
    parser.add_argument("--file", help=constants.SUPPORTED_FILE_HELP)
    parser.add_argument("--purpose", help=constants.PURPOSE_HELP)
    parser.add_argument("--author", help=constants.AUTHOR_HELP)
    parser.add_argument("--URL", help=constants.URL_HELP)
    
    args = parser.parse_args()
    if args.dated:
        with open("dates.json", "r") as f:
            data = json.load(f)
            now = getDate()
            currDate = datetime.datetime.strptime(now, "%m/%d/%Y")
            journalName = "default"
            previous = None
            for i,date in enumerate(data.keys()):
                print(date)
                loadedDate = datetime.datetime.strptime(date, "%m/%d/%Y")
                if currDate < loadedDate:
                    if i > 0:
                        journalName = data[previous]
                    else:
                        journalName = data[date] # should be 0
                    break
                previous = date
            args.project = journalName

    if args.language not in ["python", "HTML", "C"]:
        print(constants.ERR_LANGAUGE)
        sys.exit(1)
    if os.path.exists(args.project):
        print(constants.ERR_PROJECT_EXISTS.format(args.project))
        sys.exit(1)

    # Create directory
    os.mkdir(args.project)
    createREADME(args)
    if args.language == "python":
        handlePython(args)
    elif args.language == "HTML":
        pass
    elif args.language == "C":
        pass
    else:
        print(constants.ERR_LANGAUGE)
        sys.exit(1)

