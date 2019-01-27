# Journal 1
### Assignment Writeup
#### Intentions
My intentions for this project were to create a webpage that allows you to upload any ASCII encoded file and returns a histogram of the characters used in that file. 
#### Input Work Done
The input work done is this subdirectory of the repository.
#### Output Results
File selected from landing page
![File selected from landing page](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/Journal1_index_screen.png)

The content of the file is [here](https://github.com/ekivolowitz/LIS351Projects/blob/master/Journal1/test.txt)
```txt
This is a test file to test really cool things
```
Histogram from that file
![Histogram from that file](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/Journal1_hist.png)
#### Approach
I have tinkered with several backend technologies, and one that I wanted to play around with again was Flask. I decided to whip together a quick little backend that accepts file input, which I've never handled before. Between Flask and HTML5, all of the complicated parts were taken care of (yay). I used to write some HTML back in High School when I first got interested in computers. Although I've never taken the time to become an expert on it, I can usually hack together what I have in mind. CSS sucks, I just wanted to throw that out there. Anyway, I've written some javascript in my day, although I'm not a big fan of it. I was going to use D3js to create the histogram, but decided against it in the name of brevity, and implemented a pure ASCII form instead - topical to our readings. 

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
* [Flask Documentation](http://flask.pocoo.org/)
* [Flask File Upload Example](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/)
* [ASCII Table](https://www.ascii.cl/htmlcodes.htm)

