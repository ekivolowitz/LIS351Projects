
# Journal6
### URL
The URL for the source code of this project is available here: https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal6
### Assignment Writeup
#### Intentions
Per Journal5's feedback, I wanted to make a way to correctly generate journal names.
#### Input Work Done
Read about the canvas api to find out the endpoints I need to hit to collect the right data.
#### Output Results
This program will look into the 'Modules' tab to find how many modules there are, and then create a journal called
`Journal<number of modules>.
#### Approach
I took the same approach as last week, just adding in a way to collect how many modules there are first and then setting the name that way.
Handling private authentication was interesting with the API key. I ended up creating a 'secret' python file called `secrets.py`. I then formatted it like so:
```python3
AUTH_TOKEN = "<auth>"
```
#### Thoughts on the results
This is pretty cool, and I hope it's reusable for future semesters. As this is a command line utility, this project is the result. There are no pictures to have. 
### Dependencies
* [python3](https://www.python.org/download/releases/3.0/)

### Usage
```bash
$ python3 Journal6.py language [--project] [--flask] [--auto] [--file] [--purpose] [--author] [--URL]
```
### References
* [canvas API](https://canvas.instructure.com/doc/api/)
* [requests](http://docs.python-requests.org/en/master/)
