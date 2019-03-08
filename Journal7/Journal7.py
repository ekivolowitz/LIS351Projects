
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
from bs4 import BeautifulSoup

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

def getAssignments(course_id):
    return query(constants.ASSIGNMENT_URL.format(course_id))

def buildReturnLine(line, search_term):
    if search_term in line:
        print("{} is in \"{}\"".format(search_term, line))
        data = ""
        for word in line.split(" "):
            if word != search_term:
                data += " "
            else:
                data += colored(word + " ", UPDATE)
        return data
    return None
def handleInsert(search_term, course):
    course_id = course['id']
    assignments = getAssignments(course_id)
    if assignments is None:
        print("ERROR: Assignments is None")
        return
    assignments = assignments.json()
    results = []

    for assignment in assignments:
        try:
            soup = BeautifulSoup(assignment['description'], 'html.parser')
        except:
            continue
        text = soup.get_text().split("\n")
        links = soup.find_all("a")

        printed = False

        for line in text:
            if search_term in line:
                if not printed:
                    print(colored("Found {} in {}. Here are all the words that match ".format(search_term, assignment['name']), 'green'))
                    printed = True
                for word in line.split(" "):
                    if word == search_term:
                        print(colored(word, UPDATE), end=" ")
                    else:
                        print(word, end=" ")
                print()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("search_term", help=constants.VIEW_HELP)
    args = parser.parse_args()

    courses = getCourses()
    if courses is None:
        sys.exit(1)
    course = selectCourse(courses)

    handleInsert(args.search_term, course)