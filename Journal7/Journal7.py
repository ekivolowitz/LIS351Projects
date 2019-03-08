
######################################################################
# Project           : Journal7
#
# Program name      : Journal7.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 03/05/2019
#
# Purpose           : To make searching for information easier.
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
# Date        Author     Ref    Revision 
# 03/07/2019  Author      1     Initial work.
#
######################################################################
from pymongo import MongoClient
import constants
import secrets
import requests
from pprint import pprint
import argparse
import sys
from termcolor import colored

client = MongoClient('localhost', 27017)
db = client.lis
collection = db['words']

ERROR = 'red'
UPDATE = 'yellow'
SELECTION = 'cyan'

def query(url):
    print(colored("Fetching data from canvas...", 'red'))
    request = requests.get(url, headers={"Authorization" : "Bearer " + secrets.AUTH_TOKEN})
    if request.ok:
        return request
    return None
def getCourses():
    url = constants.COURSES_URL
    request = query(url)
    if request is None:
        print("ERROR: Request for {} failed.".format(url))
        return None
    json = request.json()
    return json    

def selectCourse(courses):
    if courses is None:
        return
    user_input = ""
    while True:
        print(colored("You have {} courses. Which course would you like to choose?".format(str(len(courses))), UPDATE))
        for i, elem in enumerate(courses):
            print("{}) {}".format(str(i), elem['course_code']))
        user_input = input(colored("Selection: ", SELECTION))
        try:
            correct_index = int(user_input)
            if correct_index < len(courses) and correct_index >= 0:
                break
            print("Please enter a value between 0 and {}".format(len(courses)))
        except:
            print(colored("ERROR: You must enter an integer value between 0 and {}".format(len(courses)), ERROR))
    print("You have selected course: {}".format(str(courses[correct_index]['name'])))
    return courses[correct_index]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--view", action="store_true", help=constants.VIEW_HELP)
    args = parser.parse_args()

    courses = getCourses()
    if courses is None:
        sys.exit(1)
    course = selectCourse(courses)

    if args.view:
        pass
    else:
        pass

    # for color in ['grey','red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
    #    print(colored("This text is written in {}".format(color), color))


