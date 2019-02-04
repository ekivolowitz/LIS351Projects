# Journal 1
### URL
The URL for the source code of this project is available here: https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal2
### Assignment Writeup
#### Intentions
My intentions for this project were to create a webpage that allows you to upload any file and it will return to you the size of the file in bytes, kilobytes, megabytes, gigabytes, or terabytes.
#### Input Work Done
The input work done is this subdirectory of the repository.
#### Output Results
File selected from landing page
![File selected from landing page](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/Journal1_index_screen.png)

The content of the file is [here](https://github.com/ekivolowitz/LIS351Projects/blob/master/Journal2/test.txt)
```txt
This is a test file to test really cool things
```
Returned data from that file
![Returned data from that file](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/Journal2_size.png)
#### Approach
We were talking about bits this week and a natural extension of that are bytes. So, I created a new webserver that will return to you
the size of a file you upload in various factors of bytes by dividing the byte size by `2 ** 10,20,30,40` for kilo, mega, giga, and terabytes.

#### Thoughts on the results
This was a fun little project because it reminds me of how cool, and expressive binary is. Going up by factors of 10 in exponents makes
size math really easy to do, and is very smart.

### Dependencies
* [python3](https://www.python.org/download/releases/3.0/)
* [Flask](http://flask.pocoo.org/)
### Usage
```bash
$ python3 main.py
```
Now navigate to `localhost:5000` in your favorite web browser and use the letter counting program!

Note: The program only supports ASCII encoded files.

### References
* [Journal 1](https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal1)
