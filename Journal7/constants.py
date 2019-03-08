MAIN_URL = "https://canvas.instructure.com"
COURSES_URL = MAIN_URL + "/api/v1/courses"
MODULES_URL = COURSES_URL + "/{}/modules" # course id goes in the brackets
PROJECT_NAME = "Journal{}"
VIEW_HELP = '''
Specify the --view flag if you would like to look in your database, 
instead of writing new data to it.

Default: FALSE
'''