
######################################################################
# Project           : Journal6
#
# Program name      : Journal6.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 02/26/2019
#
# Purpose           : Create a reusable python script to generate Journal code.
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
# 02/26/2019  Evan Kivolowitz      1     Created prototype of project.
# 03/03/2019  Evan Kivolowitz      2     Added API calls for automatically creating projects.
#
######################################################################
import argparse
from pprint import pprint
import textwrap
import os
import constants
import secrets
import requests
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
    program_name = args.project + ".py"
    if args.file:
        program_name = args.file
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
        usage += constants.USAGE_PYTHON.format(project_name)
        if args.flask:
            dependency += constants.DEPENDENCY_FLASK
            usage += constants.USAGE_FLASK
    with open("{}/{}".format(args.project, "README.md"), 'w') as f:
        f.write(constants.README.format(project_name, URL, dependency, usage))

def handleAutoFlag(args):
    request = requests.get(constants.COURSES_URL, headers={"Authorization" : "Bearer " + secrets.AUTH_TOKEN})
    data = []
    correct_index = 0
    for elem in request.json():
        if "LIS351" in elem['name']:
            data.append(elem)
    if len(data) == 0:
        print("ERROR: LIS351 not in any of your classes.")
        sys.exit(1)
    elif len(data) > 1:
        user_input = ""
        while True:
            print("You have {} courses that match LIS351. Which course would you like to choose?".format(str(len(data))))
            for i, elem in enumerate(data):
                print("{}) {}".format(str(i), elem['course_code']))
            user_input = input("Selection: ")
            try:
                correct_index = int(user_input)
                if correct_index > len(data) or correct_index < 0:
                    print("Please enter a value between 0 and {}".format(len(data)))
                    continue
                else:
                    print("Hello World")
                break
            except:
                print("ERROR: You must enter an integer value between 0 and {}".format(len(data)))
        print("You have selected course: {}".format(str(data[correct_index]['name'])))
    corr_elem = data[correct_index]
    course_id = corr_elem['id']
    request = requests.get(constants.MODULES_URL.format(course_id), headers = {"Authorization" : "Bearer " + secrets.AUTH_TOKEN})
    module_data = request.json()
    return constants.PROJECT_NAME.format(str(len(module_data)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("language")
    parser.add_argument("--project", help=constants.PROJECT_HELP)
    parser.add_argument("--flask", action="store_true", help=constants.FLASK_HELP)
    parser.add_argument("--auto", action="store_true", help=constants.DATES)
    parser.add_argument("--file", help=constants.SUPPORTED_FILE_HELP)
    parser.add_argument("--purpose", help=constants.PURPOSE_HELP)
    parser.add_argument("--author", help=constants.AUTHOR_HELP)
    parser.add_argument("--URL", help=constants.URL_HELP)
    
    args = parser.parse_args()
    if not args.auto and not args.project:
        print(constants.NO_AUTO_OR_PROJECT_NAME)
        sys.exit(1)
    if args.auto:
        args.project = handleAutoFlag(args)
    if args.language not in ["python", "HTML", "C"]:
        print(constants.ERR_LANGAUGE)
        sys.exit(2)
    if os.path.exists(args.project):
        print(constants.ERR_PROJECT_EXISTS.format(args.project))
        sys.exit(3)

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
        sys.exit(4)